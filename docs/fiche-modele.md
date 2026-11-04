# Fiche modèle : sentiment-app

> Une fiche modèle dit, en une page, ce que fait le modèle, sur quelles données il a appris, ce qu'il
> vaut, où il se trompe et dans quelles conditions on peut s'en servir. Remplacez chaque consigne par
> votre texte ; les lignes qui commencent par « > » ne comptent pas. Les tests vérifient que chaque
> rubrique est remplie et que les chiffres cités sont ceux du dépôt.

## Identité du modèle

sentiment-app 0.6.0, entraîné le 4 novembre 2026 avec scikit-learn 1.5.2.
Le pipeline associe un TF-IDF de mots et bigrammes à une régression logistique.

## Usage prévu

Aider une équipe de relation client à trier des avis en français, avec une classe
positive, négative ou un renvoi vers un humain lorsque la confiance est insuffisante.

## Usages exclus

Ne pas utiliser pour diagnostiquer une maladie, prendre une décision juridique,
évaluer une personne ou sanctionner automatiquement un client. Les autres langues,
le dialecte et les domaines différents du jeu de démonstration ne sont pas validés.

## Données d'entraînement

Jeu synthétique généré localement par make_demo.py : 290 avis, 145 positifs et
145 négatifs, dont 100 avis mitigés et 30 neutres. Le découpage stratifié, graine 42,
réserve 232 avis à l'entraînement et 58 au test. Ce corpus pédagogique ne représente
pas la diversité d'une clientèle réelle ; il ne constitue pas une validation en production.

## Performances mesurées

Mesures du modèle démo dans metrics.json : F1 macro **0.879**, rappel des négatifs
**0.931**, exactitude 0.8793. Matrice de confusion : 27/2 pour les négatifs, 5/24
pour les positifs. Au seuil d'abstention 0.60, le modèle traite 42 avis sur 58 (72 %),
avec une exactitude de 0.952 sur ces avis ; 16 vont vers un humain et 2 erreurs restent.

## Limites connues

Les 7 erreurs du test démo concernent des retournements de sentiment, par exemple
« Taille trop petite et retour payant au déballage, sauf que ensuite produit conforme
à la description, très satisfait. », classé négatif avec 0.5335 avant abstention.
Le jeu d'or local contient 20 avis : 13 justes, 7 abstentions et aucune erreur franche.
Ce petit jeu ne suffit pas à garantir l'absence d'erreurs sur de nouveaux avis.

## Biais mesurés

Sur le test démo, les 17 avis avec retournement ont une exactitude de 0.588 contre
1.000 pour les 41 avis directs. Les 27 avis longs atteignent 0.741 contre 1.000 pour
les 31 courts (médiane : 9 mots). Après abstention, 15 retournements vont à un humain
et 2 erreurs subsistent. Ces groupes de formulation ne mesurent pas l'équité démographique.

## Explicabilité

SHAP explique la sortie en log-odds de la classe positive. Pour l'avis mitigé cité,
la base vaut -0.0114 et la base plus les contributions vaut -0.1343, comme la sortie
du modèle. « produit cassé » pousse vers le négatif, « impeccable » vers le positif.
Les mots sont pondérés sans compréhension globale du retournement ; l'explication
éclaire la prédiction sans démontrer qu'elle est correcte ou causale.

## Conditions d'usage

Un humain relit tous les avis INDETERMINE et contrôle un échantillon des autres,
en priorité les textes longs, ironiques ou mitigés. Aucun refus de service ni sanction
ne doit découler du seul verdict. Le score exprime une confiance du modèle, pas une
probabilité garantie de justesse. Les avis transmis ne doivent pas contenir de secrets.

## Maintenance

Réentraîner si les données, le domaine ou les performances changent, avec
scikit-learn 1.5.2 pour rester compatible avec la roue. Versionner les métriques,
rejouer les tests, la courbe, les biais et SHAP, puis actualiser cette fiche.
Hors du dépôt, renseigner SENTIMENT_MODELE ; le fichier joblib reste hors de Git.
