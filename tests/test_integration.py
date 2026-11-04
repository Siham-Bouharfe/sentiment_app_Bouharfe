"""Tests d'intégration : l'API telle qu'elle tourne vraiment (TP4, étape D). À COMPLÉTER.

Les tests du TP3 vérifient des réponses ; ceux-ci vérifient le démarrage de l'API
et son comportement quand le modèle manque ou tombe en panne.
"""
from pathlib import Path

import pytest

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")


def test_demarrage_reel_charge_le_modele():
    """D.1 (donné en exemple) : un client ouvert par « with » exécute le lifespan."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")
    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


def test_modele_absent_refuse_le_demarrage(monkeypatch):
    import predict
    from api.model import load_model

    chemin_original = predict.chemin_modele()
    monkeypatch.setattr(predict, "chemin_modele", lambda: chemin_original.with_name("modele-inexistant.joblib"))
    predict.charger_modele.cache_clear()
    with pytest.raises(FileNotFoundError):
        load_model()
    predict.charger_modele.cache_clear()


def test_modele_non_charge_repond_503(monkeypatch):
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", None)
        assert client.get("/health").status_code == 503
        assert client.post("/predict", json={"text": "avis"}).status_code == 503


@pytest.mark.parametrize("exception", [RuntimeError("panne"), ValueError("bug interne")])
def test_panne_du_modele_repond_500(monkeypatch, exception):
    from fastapi.testclient import TestClient

    from api.main import app

    class ModeleEnPanne:
        model_name = "test"

        def predict(self, text: str):
            raise exception

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", ModeleEnPanne())
        reponse = client.post("/predict", json={"text": "avis valide"})
    assert reponse.status_code == 500
    assert "bug interne" not in reponse.text


def test_classes_inattendues_refusent_le_demarrage(monkeypatch):
    from types import SimpleNamespace

    from fastapi.testclient import TestClient

    from api import model
    from api.main import app

    monkeypatch.setattr(model, "charger_modele", lambda: SimpleNamespace(classes_=["neutral"]))
    with pytest.raises(ValueError, match="Classes du modèle incompatibles"), TestClient(app):
        pass
