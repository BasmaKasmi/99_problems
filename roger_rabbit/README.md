## Exercice 9/13 : Roger Rabbit

roger_rabbit est une fonction python qui effectue une conversion simple des nombres entiers naturels en binaire.
Les résultats sont retournés en tant que liste de chaînes de caractères triées par ordre croissant.

La fonction roger_rabbit s'appuie sur un processus itératif pour convertir chaque nombre entier en sa représentation binaire à travers une approche récursive. Pour atteindre cet objectif, je me suis appuyée sur une méthode en plusieurs étapes :

- J'ai commencé par créer une liste vide. Cette liste est destinée à accueillir les représentations binaires des nombres de 1 à n.

- J'ai ensuite écrit une fonction récursive nommée to_binary qui convertit un entier naturel en sa représentation binaire sous forme de chaîne de caractères. Cette fonction s'appelle elle-même jusqu'à ce que le nombre à convertir soit 0 ou 1, les cas de base de la récursion.

- À l'aide d'une boucle for, je parcours chaque nombre de 1 à n, je convertis chaque nombre en binaire grâce à la fonction to_binary et je stocke le résultat dans la liste précédemment initialisée.

- Finalement, la liste contenant toutes les représentations binaires est renvoyée. Ces dernières sont déjà dans l'ordre croissant grâce à la manière dont elles sont générées.

J'ai choisi cette méthode spécifiquement pour sa conformité avec les contraintes de performance dans l'énoncé du problème :

- La boucle principale et la fonction de conversion ont une complexité linéaire O(n), ce qui signifie que le temps d'exécution augmente de manière linéaire avec la valeur de n. Cette efficacité est cruciale pour traiter de grands ensembles de nombres dans des délais raisonnables.

- L'utilisation d'une liste pour stocker les résultats et d'une fonction récursive pour la conversion en binaire garantit une utilisation optimale de la mémoire. La complexité mémoire reste ainsi contrôlée et efficace, respectant l'exigence d'une complexité mémoire constante.
