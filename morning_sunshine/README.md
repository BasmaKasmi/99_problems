solution proposée pour la fonction morning_sunshine() :

    -je produis une nouvelle liste qui contient le dernier entier de la liste en entrée
    -je parcours la liste en entrée à l'envers, depuis l'avant dernier entier
    -si la valeur obtenue est inférieure ou égale au dernier élément de la nouvelle liste:
        -je passe à la suite sans rien faire
    -sinon:
        -je rajoute la valeur obtenue dans la nouvelle liste
    -je retourne la nouvelle liste


De cette maniére, pour chaque valeur observée, elle est comparée à la valeur maximale parmi les entiers qui la suivent dans la chaine en entrée. si elle lui est supérieure elle remplit la condition pour rentrer dans la nouvelle chaine.

Nous allons donc comptabliliser les opérations élémentaires (indiquées par ligne) pour mesurer la compléxité algorithmique dans le pire des cas:

l3 : une comparaison. T = 1

l 4 : un assignement et une opération sur tableau T = 2

l 5 : début d'un boucle de longueur n - 1:

    l 6 : deux calculs et une comparaison donc 3(n-1)

        l 9 : une opération et un calcul 2(n-1)

l 10: fonction reverse: T = n


On calcule la quantité d'opérations dans le pire des cas:

T = 1 + 2 + 3(n - 1) + 2(n - 1) + n

T = 6n -2

On reste sur une compléxité algorithmique linéaire.