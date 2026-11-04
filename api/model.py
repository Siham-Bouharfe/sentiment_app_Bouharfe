"""Raccord entre l'API et le modèle entraîné au TP2.

L'API n'entraîne rien et ne connaît pas scikit-learn : elle appelle la fonction
predict() de src/predict.py, qui charge le modèle une seule fois.
"""
import sys
from pathlib import Path
from typing import Literal, TypedDict

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from predict import charger_modele  # noqa: E402
from predict import predict as _predict  # noqa: E402

SEUIL_ABSTENTION = 0.60
Label = Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]
CORRESPONDANCE: dict[str, Label] = {"positive": "POSITIVE", "negative": "NEGATIVE"}


class Prediction(TypedDict):
    label: Label
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        pipeline = charger_modele()
        classes = set(pipeline.classes_)
        if classes != set(CORRESPONDANCE):
            raise ValueError(f"Classes du modèle incompatibles : {sorted(classes)}")

    def predict(self, text: str) -> Prediction:
        """Renvoie le verdict, la confiance et un aperçu du texte."""
        r = _predict(text)  # lève ValueError si le texte est vide
        score = float(r["score"])
        label = CORRESPONDANCE[r["label"]]
        verdict: Label = (
            "INDETERMINE" if score < SEUIL_ABSTENTION else label
        )
        return {"label": verdict, "score": score, "text": text[:100]}


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans le paquet)."""
    return SentimentClassifier()
