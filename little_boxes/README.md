## Exercice 8/13 : little boxes

Dans cet exercice, j'ai créé une fonction, nommée little_boxes, qui trie les caractères d'une chaîne en se basant sur leur valeur ASCII. Cette tâche met en évidence non seulement les compétences en manipulation de chaînes de caractères mais aussi en optimisation algorithmique.

L'objectif principal de little_boxes est de réarranger les caractères d'une entrée donnée selon l'ordre ASCII croissant. Pour ce faire, la fonction procède en trois étapes majeures :

- La première étape consiste à parcourir la chaîne d'entrée et à compter le nombre d'occurrences de chaque caractère ASCII. Cette opération est réalisée à l'aide d'un tableau de taille fixe, initialisé à zéro, où chaque indice correspond à un caractère ASCII possible.

- Ensuite, la fonction itère sur le tableau des occurrences pour construire une nouvelle chaîne. Cette chaîne est formée en ajoutant chaque caractère un nombre de fois équivalent à son comptage, garantissant ainsi un tri par valeur ASCII.

- La chaîne ainsi triée est finalement retournée comme résultat de la fonction.

Cette méthode a été choisie pour sa capacité à répondre aux contraintes de complexité imposées par l'exercice :

- Le parcours initial pour compter les occurrences des caractères ainsi que la reconstruction de la chaîne triée se font en temps linéaire par rapport à la longueur de la chaîne d'entrée.

- L'utilisation d'un tableau de taille fixe pour le comptage des caractères ASCII assure une complexité mémoire constante, indépendante de la taille de la chaîne d'entrée.

Ces caractéristiques font de l'algorithme little_boxes une solution optimale en termes d'efficacité et de respect des contraintes de performance.
