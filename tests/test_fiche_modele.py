"""Tests de la fiche modèle (TP6, étape G).

Ils échouent tant que la fiche n'est pas remplie : c'est voulu, comme les fiches de cadrage du TP1.
"""
import json
import re
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
FICHE = RACINE / "docs" / "fiche-modele.md"
METRIQUES = RACINE / "models" / "metrics.json"

RUBRIQUES = ["Identité du modèle", "Usage prévu", "Usages exclus", "Données d'entraînement",
             "Performances mesurées", "Limites connues", "Biais mesurés", "Explicabilité",
             "Conditions d'usage", "Maintenance"]


def rubrique(titre: str) -> str:
    """Le texte rédigé d'une rubrique, sans les lignes de consigne."""
    texte = FICHE.read_text(encoding="utf-8")
    m = re.search(rf"^## {re.escape(titre)}.*?$\n(.*?)(?=^## |\Z)", texte, re.M | re.S)
    corps = m.group(1) if m else ""
    return "\n".join(ligne for ligne in corps.splitlines()
                     if ligne.strip() and not ligne.lstrip().startswith(">"))


def nombre_ecrit(valeur: float, texte: str) -> bool:
    """Vrai si la valeur figure dans le texte, avec un point ou une virgule (0.879 ou 0,879)."""
    ecrit = f"{valeur:.3f}"
    return ecrit in texte or ecrit.replace(".", ",") in texte


def test_la_fiche_existe():
    assert FICHE.exists(), "docs/fiche-modele.md absent : copiez-le depuis le kit"


@pytest.mark.parametrize("titre", RUBRIQUES)
def test_chaque_rubrique_est_remplie(titre):
    assert len(rubrique(titre)) >= 40, f"rubrique « {titre} » vide ou trop courte"


def test_la_version_citee_est_celle_du_paquet():
    from sentiment_app import __version__

    assert __version__ in rubrique("Identité du modèle"), f"citer la version {__version__}"


def test_les_performances_citees_sont_celles_du_depot():
    metriques = json.loads(METRIQUES.read_text(encoding="utf-8"))
    texte = rubrique("Performances mesurées")
    assert nombre_ecrit(metriques["f1_macro"], texte), f"citer le F1 macro {metriques['f1_macro']:.3f}"
    assert nombre_ecrit(metriques["recall_negative"], texte), \
        f"citer le rappel des négatifs {metriques['recall_negative']:.3f}"


def test_les_conditions_d_usage_prevoient_un_humain():
    assert "humain" in rubrique("Conditions d'usage").lower()
