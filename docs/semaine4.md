# Semaine 4 : tests approfondis et qualité, notes du binôme

> Une à deux pages. Uniquement des chiffres issus de VOS exécutions.

## 1. Couverture

- Avant (étape A) : 91 %, six lignes de `api/main.py` non exécutées.
- Ces lignes correspondaient aux modèles absents, aux pannes de prédiction et aux erreurs internes.
- Après (étape D) : 97 % de couverture ; aucune exclusion abusive, seul le bloc de lancement direct reste non couvert.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| Texte composé uniquement d'espaces accepté | tests de limites et Hypothesis | Validateur Pydantic avec `strip()` dans `PredictRequest` |
| Panne du modèle renvoyée en 422 | test d'intégration | Toute exception interne est maintenant renvoyée en 500 |

## 3. Seuil d'abstention

- Deux points de la courbe : seuil 0,50 = 58 avis traités, 0,879 d'exactitude ; seuil 0,60 = 42 avis traités, 0,952 d'exactitude.
- Seuil retenu : 0,60 ; 16 avis sur 58 sont envoyés à un humain, ce qui réduit les erreurs de 7 à 2.

## 4. Jeu d'or

- Bilan mesuré ici : 13 avis justes, 7 abstentions et aucune erreur franche sur 20 avis du jeu d'or.
- Le modèle sait signaler une partie de ses incertitudes, mais les avis ambigus restent à surveiller par un humain.

## 5. Outils statiques

- Remarques au départ : ruff signalait plusieurs problèmes de style et d'import ; mypy ne signalait aucun problème.
- Après correction, `ruff check` et `mypy api` sont silencieux. Les outils sont complémentaires : ruff contrôle surtout la forme et mypy les contrats de types.
