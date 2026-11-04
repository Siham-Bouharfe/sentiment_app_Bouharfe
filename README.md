# Analyse de sentiment - TP1 à TP6

Application pédagogique en français : entraînement TF-IDF et régression logistique,
API FastAPI, interface Streamlit et paquet installable `sentiment-app` 0.6.0.
Le projet complet se trouve dans ce dossier, sans dépendance envers les projets voisins.

## Installation sous Windows

Python **3.11** est requis pour reproduire l'environnement du guide.

```powershell
powershell -ExecutionPolicy Bypass -File scripts/installer-tp6.ps1
.\.venv311\Scripts\Activate.ps1
```

Le script installe les dépendances des TP1 à TP6, le paquet en mode éditable,
génère les 290 avis de démonstration et entraîne le modèle localement.
`requirements.txt` conserve les dépendances du semestre ; `requirements-tp6.txt`
permet d'éviter les outils des semaines suivantes. La ligne pyarrow 21 a été retirée
du fichier du semestre conformément au guide, car elle contredit MLflow 2.17.

## Utilisation

Dans un terminal avec l'environnement activé :

```powershell
sentiment --version
sentiment predict "Livraison rapide, produit conforme, très satisfait"
sentiment predict "xqzvb wlkptr grombu"
sentiment serve
```

L'API est disponible sur <http://127.0.0.1:8000/docs>.
Dans un deuxième terminal, depuis ce dossier :

```powershell
.\.venv311\Scripts\Activate.ps1
sentiment ui
```

La page analyse un avis ou [le fichier d'exemple](data/avis_exemple.csv),
permet de télécharger les résultats et affiche la répartition des verdicts et des confiances.
Une confiance inférieure à 60 % produit `INDETERMINE` : un humain doit trancher.

## Vérification

```powershell
python scripts/verifier_tp6.py
python scripts/verifier_tp6.py --roue
```

Le premier contrôle entraîne le modèle et vérifie les tests, les types, la qualité,
la couverture, l'explicabilité, les biais et les réponses HTTP d'un vrai serveur.
Le second construit aussi la roue, l'installe dans un environnement neuf hors du
dépôt et vérifie les prédictions avec et sans `SENTIMENT_MODELE`.
Les sorties réelles sont conservées dans [docs/verification/](docs/verification/).

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

## Installation de la roue ailleurs

```powershell
pip install "chemin/vers/sentiment_app-0.6.0-py3-none-any.whl"
$env:SENTIMENT_MODELE = "C:\chemin\vers\ce-projet\models\sentiment.joblib"
sentiment predict "Livraison rapide, produit conforme, très satisfait"
```

Le modèle est entraîné et relu avec scikit-learn 1.5. Il n'est inclus ni dans la
roue ni dans Git. `SENTIMENT_MODELE` fournit son chemin hors du dépôt.
Pour l'interface, installer la roue avec l'extra `[ui]`.

## Organisation et livrables

- [src/](src/) : données, entraînement, évaluation, biais et SHAP.
- [sentiment_app/](sentiment_app/) : version, commande et prédiction empaquetée.
- [api/](api/) : contrat, abstention et routes HTTP ; aucun entraînement.
- [ui/](ui/) : interface et client HTTP ; aucun accès direct au modèle.
- [tests/](tests/) : contrôles du cours et compléments.
- [docs/cadrage/](docs/cadrage/) : trois fiches du TP1.
- [docs/fiche-modele.md](docs/fiche-modele.md) : mesures et limites du modèle.
- [docs/journal-tp1-tp6.md](docs/journal-tp1-tp6.md) : suivi des contrôles.
- [docs/semaine6.md](docs/semaine6.md) et [CHANGELOG.md](CHANGELOG.md) : compte rendu et version.

Les kits restent dans `ressources/`, exclu de Git et des analyses statiques.
L'ancienne interface TP3 qui chargeait directement le modèle y est archivée ;
l'interface livrée passe exclusivement par HTTP.

## Travail du binôme et publication

Cette reconstruction reprend les ressources du cours et le code local disponible.
Elle n'invente ni commits de deux auteurs, ni captures historiques, ni CI distante.
Les deux premiers commits authentiques du binôme sont conservés comme base,
avec leurs auteurs d'origine. Les tests d'historique vérifient ces contributions.
Chaque nouvelle contribution doit être commitée avec l'identité de son auteur réel.
Les six commits TP1 à TP6 ont été poussés sur la branche
[`reconstruction-tp1-tp6`](https://github.com/Siham-Bouharfe/sentiment_app_Bouharfe_a_Igoulalen_b/tree/reconstruction-tp1-tp6)
du dépôt existant ; les six pipelines GitHub sont verts. La roue se télécharge aussi
dans l'artefact `preuves-tp6` du [run TP6](https://github.com/Siham-Bouharfe/sentiment_app_Bouharfe_a_Igoulalen_b/actions/runs/41876358543).
L'étiquette de cette version est
[`v0.6.0-reconstruction`](https://github.com/Siham-Bouharfe/sentiment_app_Bouharfe_a_Igoulalen_b/releases/tag/v0.6.0-reconstruction) ;
l'ancienne étiquette `v0.6.0` du dépôt est préservée.
Voir [le bilan de publication](docs/verification/publication.md).
