solution proposée pour la fonction yin_yang() :

    -je parcours la chaine une seule fois.
    -je suis ce parcours avec une liste compteur qui posséde un seul caractére au départ pour ne jamais être vide.
    -si j'arrive à l'un des caractéres que je cherche je regarde  si c'est un ouvrant et j'ajoute son fermant au compteur.
    -si c'est un fermant je le compare à la derniére entrée du compteur, s'ils sont similaire je supprime cette derniére entrée de compteur, les caractéres se sont fermés.
    -les caractéres " et ' sont à la fois ouvrants et fermants, je méle donc ces deux fonctionnalités.

chaque caractére ouvrant aumgent le compteur de 1, s'il trouve son fermant la chaine est réduite de 1. Si en fin de boucle, la liste contient plus que le caractére initial je return false.

Nous allons donc comptabliliser les opérations élémentaires (indiquées par ligne) pour mesurer la compléxité algorithmique dans le pire des cas:

l 2 à 4: trois opérations d'assignement: T = 3

l 5 : début d'une boucle for pour la longueur de la chaine s + 1 donc les opérations suivantes devront être comptabiliséses ( n + 1 ) fois.

    l 6 : une comparaison : T = n + 1

    l 7 - 9 - 11 - 16 : une suite de 6 comparaisons en quatre if elif donc au pire T = 6(n + 1)

        l 8 - 10 : un assignement pour les deux premiéres éventualités donc au pire T = n+1

        l 12 - 17 : une comparaison à un élément extrait d'un tableau (deux opérations élémentaires donc) pour les deux derniéres éventualités: T = 2(n+1). On est donc dans le pire des cas sur ces deux éventualités.

            l 13 - 15 : un assignement pour chacune des éventualités: T = n+1 

            l 18 : un assignement pour cette derniére éventualité, mais qui n'est envisageable que si l'une des éventualités l 7 ou 9 a été atteinte donc nous ne sommes plus dans le pire des cas. 

l 21 : un calcul et une comparaison : T = 2


calculons pour être sur chaque cas par itéation dans la boucle en étudiant les sorties de boucle: 

T = 1 ( l 6 == False)
    T = 1 + 1 + 1  sortie en l8 ou en l10 : 3 opérations élémentaires
    T = 1 + 4 + 2 + 1 sortie en l13 ou en l15: 8 oe
    T = 1 + 6 + 2 + 1 sortie en l18 Attention cette sortie implique une sortie en l8 ou l10 auparavant. ( 10 + 3) / 2 =6.5 opérations élémentaires.

donc le pire des cas au sein de la boucle serait  la sortie systématique en l13 ou l15 avec 
T = (n+1) * ( 1 + 4 + 2 + 1)
T = 8n + 8 
avec les autre opérations autour de la boucle on monte à
T = 8n + 13

On reste donc sur une compléxité linéaire.



