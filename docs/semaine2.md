# Semaine 2 — analyse des erreurs

Le modèle commet 7 erreurs sur 58 avis de test, et elles concernent les avis mitigés dont le sentiment final contredit le début de la phrase.
Ces erreurs s’expliquent par le modèle « sac de mots » : il compte les mots positifs et négatifs, mais ne comprend pas l’ordre ni les retournements comme « mais finalement ».
Pour les réduire, il faudrait un modèle capable de représenter le contexte et l’ordre des mots, par exemple avec des embeddings (vu en semaine 9).
