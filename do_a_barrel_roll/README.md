
Pour le problème "Do a barrel roll !", j'ai développé une fonction qui effectue des rotations vers la gauche d'un tableau d'entiers, basée sur un entier k spécifié. Voici comment j'ai abordé le défi et pourquoi mon algorithme satisfait les contraintes du sujet.

J'ai développé une fonction, do_a_barrel_roll, qui prend deux paramètres : une liste d'entiers et un entier k. L'objectif était d'effectuer k rotations vers la gauche du tableau.

 Comme première étape, j'ai normalisé k en le modulant avec la longueur de la liste. Cela garantit que même si k est plus grand que la taille de la liste, nous pouvons toujours effectuer un nombre de rotations valide.
 Ensuite, j'ai réalisé la rotation en utilisant le découpage de liste pour diviser la liste en deux à l'index k et les réassembler dans l'ordre inverse. Si k est 2, par exemple, les deux premiers éléments sont déplacés vers la fin, et le reste est déplacé vers le début.

 Cette méthode garantit une complexité temporelle de O(n), où n est la longueur du tableau. Le slicing de liste en Python est une opération efficace, et le réassemblage des deux parties de la liste s'effectue également en temps linéaire.

 En respectant la contrainte de complexité O(n), mon algorithme offre une solution optimale pour réaliser des rotations de tableau, même pour de grandes valeurs de k.

L'approche adoptée évite les boucles inutiles et les opérations répétitives, résultant en un code plus propre et plus facile à comprendre.
