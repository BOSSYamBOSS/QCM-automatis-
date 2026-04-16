# QCM-automatisé

Un fichier python pour créer le QCM.
Il demande le nom de l'évaluation, les points perdus pour une réponse fausse et les points gagnés pour une bonne réponse.
Un bouton permet d'ajouter une question.
La question se fait avec 4 zones de texte avec fillers.
L'écran propose de cocher la/les bonnes réponses de la question.
L'écran propose de changer le nombre de points perdus/gagnés pour une proposition en particulier.
Le fichier génère ensuite un dossier du nom de l'évaluation avec le QCM sous forme de PDF et un fichier JSON avec toutes les informations et un fichier pour la correction.

Le fichier JSON contient le nom de l'évaluation, toutes les questions avec les réponses correctes, les points perdus/gagnés pour chaque question.

Le fichier de correction : 
- repérer les réponses sélectionnées par la personne.
- comparer aux bonnes dans le fichier JSON.
- calculer la note.
- Faire la même chose pour tous les PDF dans le dossier (ce sont les évals scannées) et finit par créer un fichier html avec chaque nom d'élève (nom des PDF scannés) et leur note à côté et la note ramenée sur 20.

Le fichier HTML permet de voir le détail de la note par question si on passe le curseur de la souris dessus.
