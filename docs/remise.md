# Remise du projet

Exécuter `python scripts/verifier_tp6.py --roue` dans l'environnement Python 3.11.
Consulter les sorties et le rapport JSON dans [verification/](verification/).
Le modèle est régénéré ici, jamais copié depuis un autre projet.

## Publication réalisée

Les six étapes sont poussées sur la branche `reconstruction-tp1-tp6` du dépôt
GitHub du binôme. Chaque étape a été suivie d'un pipeline vert ; les liens sont
dans [verification/publication.md](verification/publication.md). La roue est dans
`dist/` localement et comme artefact du run TP6. L'étiquette publiée est
`v0.6.0-reconstruction`, car `v0.6.0` désignait déjà une autre version du dépôt.
La branche `main` existante n'a pas été modifiée.

## Actions restantes du binôme

1. Renseigner les deux membres et l'adresse réelle du dépôt dans le journal.
2. Relire et personnaliser les fiches et comptes rendus ; chaque membre doit
   comprendre et pouvoir expliquer sa contribution.
3. Enregistrer les captures des manipulations réellement réalisées dans
   [captures/](captures/). Les sorties texte ne remplacent pas les captures demandées.
4. Chaque nouvelle contribution doit être commitée avec l'identité réelle de son auteur.
5. Donner à l'enseignant l'accès au dépôt et le lien de la branche de reconstruction.
6. Si une intégration dans `main` est demandée, examiner la divergence entre les
   deux branches et créer une pull request. Aucun push forcé n'a été utilisé.

Le modèle de démonstration sert aux contrôles reproductibles. Allociné nécessite
un téléchargement et un entraînement distinct (`python src/train.py --allocine`).
Revenir ensuite au modèle démo et actualiser la fiche si le modèle livré change.
