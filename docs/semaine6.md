# Semaine 6 : le paquet, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi le modèle n'est-il pas dans la roue ? Comment le paquet le trouve-t-il ?

Le modèle n'est pas dans la roue car il est volumineux, généré par l'entraînement et exclu de Git. Le paquet cherche le fichier standard dans `models/` ou utilise le chemin fourni par `SENTIMENT_MODELE`.

## 2. Qu'est-ce qui a changé dans api/model.py quand predict() est entré dans le paquet, et pourquoi est-ce mieux ?

`predict.py` vit maintenant dans `sentiment_app/`, et `api/model.py` l'importe comme un vrai paquet au lieu de modifier `sys.path`. Cela rend les imports identiques dans le dépôt, la roue et l'installation éditable.

## 3. La roue installée hors du dépôt : qu'a-t-il fallu lui fournir, et pourquoi scikit-learn est-il épinglé dans pyproject.toml ?

La roue contient le code et ses dépendances déclarées, mais pas le modèle : il faut donc fournir le chemin du modèle avec `SENTIMENT_MODELE`. Scikit-learn est limité à la version 1.5 pour garantir la compatibilité du fichier joblib.
