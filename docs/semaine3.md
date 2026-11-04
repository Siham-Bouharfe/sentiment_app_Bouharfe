# Semaine 3 : exposer le modèle avec FastAPI

L'API charge le modèle une seule fois au démarrage, sans entraîner. GET /health
répond 200 avec status OK lorsque le modèle est chargé. POST /predict reçoit un
champ text et renvoie une étiquette, le score et les 100 premiers caractères.

Le modèle démo renvoie POSITIVE avec 0.777 pour l'avis « Livraison rapide, produit
conforme, très satisfait », et NEGATIVE avec 0.7465 pour « Produit cassé et service
injoignable, à fuir ». Le score représente la probabilité de la classe choisie par
le modèle, sans garantie de calibration.

Le contrat refuse un champ absent, un nombre, un texte vide ou dépassant 2000
caractères avec 422. Le TP4 complète le contrat pour les blancs, renvoie 503 si
le modèle n'est pas chargé et masque les pannes internes derrière un 500.
Les mots inventés reçoivent INDETERMINE après ajout du seuil de 0.60 au TP4.

La documentation /docs décrit les schémas et permet les essais. La CI reconstruit
le modèle avant les tests pour que ceux-ci vérifient réellement l'API.
Les preuves locales sont dans verification/ ; la CI distante est à observer après push.
