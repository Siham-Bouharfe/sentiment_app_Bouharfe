# Fiche de cadrage : Ordonnances incomplètes en pharmacie

## Besoin en une phrase (obligatoire)

Détecter automatiquement les ordonnances auxquelles il manque une information obligatoire (dosage, posologie, durée, signature du prescripteur, etc.) avant la délivrance des médicaments.

## Utilisateur final (obligatoire)

Le pharmacien ou le préparateur en pharmacie, au comptoir, au moment de la réception de l'ordonnance.

## Approche retenue (obligatoire)

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(b) Les mentions obligatoires d'une ordonnance sont fixées par la réglementation, donc chaque alerte peut être vérifiée et expliquée par une règle précise. (d) Une erreur peut mettre en danger le patient, on veut donc un système prévisible et auditable plutôt qu'un modèle probabiliste. (c) Le coût par requête est quasi nul, et (a) on n'a pas besoin de données étiquetées.

## Données nécessaires et leur origine (obligatoire)

Le contenu de l'ordonnance (saisi ou extrait par OCR), la liste réglementaire des mentions obligatoires, et la base des médicaments (nom, dosages et formes existants) fournie par la pharmacie ou une base officielle.

## Métrique de succès et seuil d'acceptation (obligatoire)

Rappel (part des ordonnances incomplètes réellement détectées) ≥ 95 % sur un jeu de test d'ordonnances annotées à la main, avec moins de 10 % de fausses alertes pour ne pas agacer l'équipe.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un oubli d'incomplétude peut conduire à une mauvaise délivrance (risque pour la santé), une fausse alerte fait seulement perdre du temps. Le système ne bloque jamais la délivrance : il signale, et le pharmacien décide et contacte le médecin si besoin.

## Risques éthiques ou de confidentialité (obligatoire)

Les ordonnances sont des données de santé sensibles : traitement en local ou sur un hébergement conforme, accès restreint, pas de conservation inutile, anonymisation des données de test. Il faut aussi éviter que le pharmacien se repose trop sur l'outil.

## Approche écartée et pourquoi (facultatif)

Modèle génératif seul : il peut inventer ou « deviner » une information manquante, et ses décisions ne sont pas vérifiables, ce qui est trop risqué pour un contexte médical.