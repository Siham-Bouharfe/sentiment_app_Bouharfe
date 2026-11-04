# Journal des versions

Le numéro de version suit les TP : 0.N.0 à la fin du TP N. Chaque version publiée porte une étiquette Git `v0.N.0`.

## Non publié

- Fiche modèle complète avec performances, biais, explication SHAP et contrôle humain.
- Compléments TP2/TP4/TP5 : explicabilité, bilan des biais et deux graphiques.
- Vérification reproductible avec sorties réelles, test HTTP et roue essayée hors du dépôt.
- Installation locale Python 3.11 ; PyArrow 17 compatible avec NumPy 1.26.

## 0.6.0 (TP6) : le paquet

- Paquet `sentiment-app` version 0.6.0 avec commande `sentiment`.
- Modèle configurable via `SENTIMENT_MODELE`, roue construite par la CI et testée hors du dépôt.
- `predict()` est désormais dans `sentiment_app/` ; un fichier de compatibilité conserve l'ancienne commande `python src/predict.py`.

## 0.5.0 (TP5) : l'interface

- Page Streamlit : un avis, ou un fichier d'avis ; le client HTTP traduit chaque réponse de l'API.

## 0.4.0 (TP4) : tests et qualité

- Contrat d'entrée testé, abstention `INDETERMINE`, jeu d'or, tests d'intégration, contrat typé, ruff, mypy, pre-commit.

## 0.3.0 (TP3) : l'API

- FastAPI : `/health`, `/predict`, contrat Pydantic ; la CI entraîne le modèle avant les tests.

## 0.2.0 (TP2) : le modèle

- TF-IDF et régression logistique ; les métriques sont versionnées, le modèle ne l'est pas.

## 0.1.0 (TP1) : le cadrage

- Environnement Python 3.11, structure du dépôt, trois fiches de cadrage, dépôt GitHub à deux auteurs.
