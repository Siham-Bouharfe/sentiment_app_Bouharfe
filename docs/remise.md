# Remise du projet

Exécuter `python scripts/verifier_tp6.py --roue` dans l'environnement Python 3.11.
Consulter les sorties et le rapport JSON dans [verification/](verification/).
Le modèle est régénéré ici, jamais copié depuis un autre projet.

## Actions du binôme et de GitHub

1. Renseigner les deux membres et l'adresse réelle du dépôt dans le journal.
2. Relire et personnaliser les fiches et comptes rendus ; chaque membre doit
   comprendre et pouvoir expliquer sa contribution.
3. Enregistrer les captures des manipulations réellement réalisées dans
   [captures/](captures/). Les sorties texte ne remplacent pas les captures demandées.
4. Commiter chacun avec sa vraie identité, puis rejouer les tests d'historique.
5. Configurer le dépôt GitHub privé et les accès du binôme et de l'enseignant.
6. Pousser et vérifier la CI, puis créer et pousser l'étiquette `v0.6.0`.

```powershell
git add README.md CHANGELOG.md pyproject.toml pytest.ini requirements*.txt .gitignore .env.example .editorconfig .pre-commit-config.yaml .github .vscode api app data docs models scripts sentiment_app src tests ui
git status
git commit -m "TP1 à TP6 : application, paquet et vérifications"
# Chaque membre apporte ensuite une vraie contribution avec sa propre identité.
# Configurer origin avec l'adresse réelle du dépôt, puis :
git branch -M main
git push -u origin main
git tag -a v0.6.0 -m "TP6 : paquet installable"
git push origin v0.6.0
```

Ne pas annoncer une CI verte avant de l'avoir observée sur GitHub.
Le modèle de démonstration sert aux contrôles reproductibles. Allociné nécessite
un téléchargement et un entraînement distinct (`python src/train.py --allocine`).
Revenir ensuite au modèle démo et actualiser la fiche si le modèle livré change.
