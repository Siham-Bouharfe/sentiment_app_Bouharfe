"""Rejoue les contrôles locaux du guide et conserve leurs sorties réelles."""
from __future__ import annotations

import argparse
import json
import os
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
SORTIES = RACINE / "docs" / "verification"
POSITIF = "Livraison rapide, produit conforme, très satisfait"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--roue", action="store_true", help="essayer aussi la roue hors du dépôt")
    args = parser.parse_args()
    SORTIES.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    env.pop("SENTIMENT_MODELE", None)
    resultats: list[dict] = []

    def enregistrer(nom: str, contenu: str, conforme: bool, **details) -> None:
        (SORTIES / f"{nom}.txt").write_text(contenu, encoding="utf-8")
        resultats.append({"controle": nom, "conforme": conforme, **details})
        print(f"{'OK' if conforme else 'ECHEC'} : {nom}", flush=True)

    def lancer(nom: str, commande: list[str], *, cwd=RACINE, environnement=env,
               code_attendu: int = 0, timeout: int = 300) -> str:
        execution = subprocess.run(commande, cwd=cwd, env=environnement, capture_output=True,
                                   text=True, encoding="utf-8", errors="replace", timeout=timeout)
        contenu = (f"Commande : {subprocess.list2cmdline(commande)}\n"
                   f"Dossier : {cwd}\nCode : {execution.returncode}\n\n"
                   + execution.stdout + execution.stderr)
        enregistrer(nom, contenu, execution.returncode == code_attendu,
                     code=execution.returncode, code_attendu=code_attendu)
        return execution.stdout + execution.stderr

    python = sys.executable
    for nom, options in [
        ("donnees", ["src/make_demo.py"]),
        ("entrainement", ["src/train.py"]),
        ("diagnostic", ["scripts/check_setup.py"]),
        ("evaluation", ["src/evaluate.py"]),
        ("seuil", ["src/courbe_seuil.py"]),
        ("jeu-or", ["src/bilan_jeu_or.py"]),
        ("biais", ["src/biais.py"]),
        ("explicabilite", ["src/expliquer.py"]),
        ("pytest", ["-m", "pytest", "-q", "--junitxml=docs/verification/pytest.xml"]),
        ("ruff", ["-m", "ruff", "check", "."]),
        ("mypy", ["-m", "mypy", "api"]),
        ("couverture", ["-m", "pytest", "--cov=api", "--cov-fail-under=95", "-q"]),
        ("version", ["-m", "sentiment_app", "--version"]),
        ("cli-positif", ["-m", "sentiment_app", "predict", POSITIF]),
        ("cli-abstention", ["-m", "sentiment_app", "predict", "xqzvb wlkptr grombu"]),
    ]:
        lancer(nom, [python, *options])

    with socket.socket() as reservation:
        reservation.bind(("127.0.0.1", 0))
        port = reservation.getsockname()[1]
    with (SORTIES / "serveur.txt").open("w", encoding="utf-8") as journal:
        serveur = subprocess.Popen([python, "-m", "sentiment_app", "serve", "--port", str(port)],
                                   cwd=RACINE, env=env, stdout=journal, stderr=subprocess.STDOUT)
        try:
            base = f"http://127.0.0.1:{port}"
            for _ in range(100):
                try:
                    with urllib.request.urlopen(base + "/health", timeout=1) as reponse:
                        sante = json.load(reponse)
                    break
                except (OSError, urllib.error.URLError):
                    if serveur.poll() is not None:
                        raise RuntimeError("Le serveur s'est arrêté au démarrage") from None
                    time.sleep(0.2)
            else:
                raise TimeoutError("Le serveur ne répond pas")
            requete = urllib.request.Request(base + "/predict",
                data=json.dumps({"text": POSITIF}).encode("utf-8"),
                headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(requete, timeout=5) as reponse:
                prediction = json.load(reponse)
            enregistrer("http-reel", json.dumps({"health": sante, "predict": prediction},
                         ensure_ascii=False, indent=2),
                         sante["status"] == "OK" and prediction["label"] == "POSITIVE")
        finally:
            serveur.terminate()
            serveur.wait(timeout=15)

    if args.roue:
        lancer("construction", [python, "-m", "build", "--wheel"])
        roue = RACINE / "dist" / "sentiment_app-0.6.0-py3-none-any.whl"
        with zipfile.ZipFile(roue) as archive:
            fichiers = archive.namelist()
        dossiers = sorted({f.split("/")[0] for f in fichiers})
        attendu = {"api", "sentiment_app", "ui", "sentiment_app-0.6.0.dist-info"}
        conforme = set(dossiers) == attendu and not any(f.endswith(".joblib") for f in fichiers)
        enregistrer("contenu-roue", "\n".join(fichiers), conforme)
        ailleurs = Path(tempfile.mkdtemp(prefix="verification-roue-tp6-"))
        environnement_roue = ailleurs / "venv"
        lancer("venv-roue", [python, "-m", "venv", str(environnement_roue)], cwd=ailleurs)
        executable = environnement_roue / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        commande = environnement_roue / ("Scripts/sentiment.exe" if os.name == "nt" else "bin/sentiment")
        env_roue = dict(env)
        env_roue.pop("PYTHONPATH", None)
        lancer("installation-roue", [str(executable), "-m", "pip", "install", str(roue)],
               cwd=ailleurs, environnement=env_roue, timeout=600)
        erreur = lancer("roue-sans-modele", [str(commande), "predict", POSITIF],
                        cwd=ailleurs, environnement=env_roue, code_attendu=1)
        enregistrer("message-modele-absent", erreur,
                     "SENTIMENT_MODELE" in erreur and "src/train.py" in erreur)
        env_roue["SENTIMENT_MODELE"] = str(RACINE / "models" / "sentiment.joblib")
        sortie = lancer("roue-avec-modele", [str(commande), "predict", POSITIF],
                         cwd=ailleurs, environnement=env_roue)
        prediction_roue = json.loads(sortie)
        enregistrer("prediction-roue", sortie, prediction_roue["label"] == "POSITIVE"
                     and abs(prediction_roue["score"] - 0.777) < 0.001)
        lancer("origine-roue", [str(executable), "-c",
               "import sentiment_app; print(sentiment_app.__file__)"],
               cwd=ailleurs, environnement=env_roue)

    rapport = {"date_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version,
               "racine": str(RACINE), "controles": resultats,
               "limites": ["CI GitHub à vérifier après chaque push ; historique original du binôme conservé",
                           "Captures historiques et entraînement Allociné non simulés"]}
    (SORTIES / "rapport.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=2) + "\n",
                                          encoding="utf-8")
    echecs = sum(not resultat["conforme"] for resultat in resultats)
    print(f"{len(resultats) - echecs}/{len(resultats)} contrôles locaux conformes", flush=True)
    return int(echecs > 0)


if __name__ == "__main__":
    raise SystemExit(main())
