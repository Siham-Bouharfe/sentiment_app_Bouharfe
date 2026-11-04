# Analyse de sentiment - TP1 à TP6

Application pédagogique en français : entraînement TF-IDF et régression logistique,
API FastAPI, interface Streamlit et paquet installable `sentiment-app` 0.6.0.

## Installation sous Windows

Python **3.11** est recommandé.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-tp6.txt
pip install -e .
python src/make_demo.py
python src/train.py
```

## Utilisation

Dans un terminal avec l'environnement activé :

```powershell
sentiment --version
sentiment predict "Livraison rapide, produit conforme, très satisfait"
sentiment predict "xqzvb wlkptr grombu"
sentiment serve
```

L'API est disponible sur <http://127.0.0.1:8000/docs>.

Dans un deuxième terminal, avec l'environnement activé :

```powershell
sentiment ui
```

La page analyse un avis ou [le fichier d'exemple](data/avis_exemple.csv),
permet de télécharger les résultats et affiche la répartition des verdicts et des confiances.
Une confiance inférieure à 60 % produit `INDETERMINE` : un humain doit trancher.

## Tests et validation

```powershell
python -m pytest -q
python -m ruff check .
python -m mypy api
python -m pytest --cov=api --cov-fail-under=95 -q
python src/evaluate.py
python src/courbe_seuil.py
python src/bilan_jeu_or.py
python src/expliquer.py
python src/biais.py
python -m build --wheel
```

## Installation de la roue (.whl) hors du dépôt

```powershell
pip install "dist/sentiment_app-0.6.0-py3-none-any.whl"
$env:SENTIMENT_MODELE = "chemin\vers\models\sentiment.joblib"
sentiment predict "Livraison rapide, produit conforme, très satisfait"
```

Le modèle est entraîné et relu avec scikit-learn. Il n'est inclus ni dans la
roue ni dans Git. La variable d'environnement `SENTIMENT_MODELE` fournit son chemin.

## Organisation et livrables

- [src/](src/) : données, entraînement, évaluation, biais et SHAP.
- [sentiment_app/](sentiment_app/) : version, commande CLI et prédiction empaquetée.
- [api/](api/) : contrat, abstention et routes HTTP.
- [ui/](ui/) : interface Streamlit et client HTTP.
- [tests/](tests/) : suite de tests automatisés.
- [docs/cadrage/](docs/cadrage/) : trois fiches du TP1.
- [docs/fiche-modele.md](docs/fiche-modele.md) : mesures et limites du modèle.
- [docs/journal-tp1-tp6.md](docs/journal-tp1-tp6.md) : suivi des contrôles.
- [docs/semaine6.md](docs/semaine6.md) et [CHANGELOG.md](CHANGELOG.md) : compte rendu et version.
