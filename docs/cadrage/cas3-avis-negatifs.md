# Fiche de cadrage : Priorisation des avis négatifs

## Besoin en une phrase (obligatoire)

Classer automatiquement les avis clients négatifs par urgence (produit dangereux, client très mécontent, simple remarque) pour que l'équipe traite d'abord les plus importants.

## Utilisateur final (obligatoire)

L'équipe service client ou la responsable e-réputation de l'entreprise.

## Approche retenue (obligatoire)

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(a) L'entreprise dispose d'un historique d'avis déjà traités, qu'on peut étiqueter par niveau d'urgence pour entraîner un classifieur. (c) Le coût par avis est très faible une fois le modèle entraîné, ce qui compte avec un gros volume d'avis. (d) Une erreur reste modérée, car un avis mal classé est seulement traité plus tard, et un humain relit de toute façon.

## Données nécessaires et leur origine (obligatoire)

Les avis clients (site, réseaux sociaux, plateformes d'avis) avec leur note, et un échantillon de 500 à 1 000 avis étiquetés à la main par l'équipe service client selon le niveau d'urgence.

## Métrique de succès et seuil d'acceptation (obligatoire)

Rappel ≥ 90 % sur la classe « urgent » (on ne veut presque jamais rater un avis grave), avec une précision d'au moins 70 %, mesurés sur un jeu de test non utilisé à l'entraînement.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un avis urgent classé en faible priorité peut retarder une réponse à un problème grave (sécurité, client très en colère). Le modèle ne répond jamais seul : il propose un classement, et l'équipe relit la liste, en vérifiant en priorité les avis où le modèle est peu sûr.

## Risques éthiques ou de confidentialité (obligatoire)

Les avis peuvent contenir des noms ou des informations personnelles : anonymisation avant l'entraînement et accès limité à l'équipe. Il faut aussi vérifier que le modèle ne traite pas moins bien certains types d'avis (langue, dialecte, style d'écriture).

## Approche écartée et pourquoi (facultatif)

Règles métier : une liste de mots-clés (« danger », « arnaque ») rate les formulations indirectes et l'ironie, et elle devient difficile à maintenir.