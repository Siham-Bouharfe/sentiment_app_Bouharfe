# Fiche de cadrage : Questions sur le règlement intérieur

## Besoin en une phrase (obligatoire)

Permettre aux employés (ou étudiants) d'obtenir rapidement une réponse fiable à leurs questions sur le règlement intérieur, sans avoir à lire tout le document ni solliciter les RH.

## Utilisateur final (obligatoire)

Les employés (ou étudiants) de l'organisation, avec les RH (ou l'administration) comme responsables du contenu du règlement.

## Approche retenue (obligatoire)

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(b) Le RAG permet de citer l'article exact du règlement utilisé pour répondre, donc la réponse est vérifiable. (a) Il n'exige aucune donnée étiquetée : il suffit d'indexer le document. (d) Une erreur a des conséquences modérées (mauvaise information sur les congés, horaires, sanctions), ce qui reste acceptable avec les sources affichées. (c) Le coût par requête est faible, car seuls quelques passages sont envoyés au modèle.

## Données nécessaires et leur origine (obligatoire)

Le texte officiel et à jour du règlement intérieur (PDF ou Word), fourni par les RH ou l'administration, découpé en passages et indexé. Un petit jeu de questions-réponses de test, écrit à la main, pour évaluer le système.

## Métrique de succès et seuil d'acceptation (obligatoire)

Au moins 90 % de réponses correctes et appuyées sur le bon article, mesurées sur 30 à 50 questions de test, avec 0 réponse inventée quand l'information n'existe pas dans le règlement (le système doit alors dire « je ne sais pas »).

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une mauvaise réponse peut induire quelqu'un en erreur sur ses droits ou obligations, mais l'impact reste limité. Chaque réponse affiche l'article cité, et en cas de doute ou de sujet sensible (sanction, litige), l'utilisateur est renvoyé vers les RH, qui ont le dernier mot.

## Risques éthiques ou de confidentialité (obligatoire)

Le règlement est un document interne, mais les questions posées peuvent révéler des situations personnelles : pas de conservation des questions liées à une identité, accès limité aux membres de l'organisation. Il faut aussi préciser que l'outil est une aide et non une source juridique officielle.

## Approche écartée et pourquoi (facultatif)

Modèle génératif seul : il répondrait de mémoire, sans connaître le règlement propre à l'organisation, et risquerait d'inventer des règles non vérifiables.