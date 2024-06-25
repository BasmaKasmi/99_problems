solution proposée pour la fonction set_et_match() :
    -j'assigne dans une variable max l'index maximum de ma liste.
    -je vérifie si ma liste contient au moins deux entiers. 
    -je trie ma liste du plus petit au plus grand.
    -je parcours une seule fois la liste d'entier en additionnant chaque nombre au nombre suivant (i) et (i+1). 
        -si j'obtiens le résultat attendu je retourne True.
        -si j'obtiens un résultat supérieur au nombre attendu:
            -si ma valeur max est toujours la valeur initiale je lui attribue la valeur de l'index de l'entier précedent les deux entiers additionnés (i-1).
            -puis je parcours le tableau en sens inverse depuis l'index de l'entier en question (i-1) jusqu'à l'index 0 pour additionner ce nombre à ses précédents.
                -j'interrompts cette boucle dés que la somme est inférieure au résultat attendu bien sur ce serait inutile d'aller plus loin.
                    -De cette maniére je restreint la quantité de comparaison nécessaire par le bas.
                -si j'obtiens le résultat attendu je renvoie true.
                -si la somme de mon entier comparé et de son précédent sont supérieurs à l'entier attendu on reassigne la variable max à l'index du précédent moins un, afin de restreindre la quantité de comparaison par le haut. en effet les prochains entiers à comparer seront supérieurs ou égaux à l'entier comparé, donc inutile de les recomparer aux précédents dont l'index est supérieur ou égal à y.
    -arrivé en fin de boucle je renvoie false


L'idée de ce programme est de cironscrire autant que possible la boucle imbriquée.


Nous allons donc comptabliliser les opérations élémentaires (indiquées par ligne) pour mesurer la compléxité algorithmique dans le pire des cas:
    
    l 2 : on calcule la longueur d'une liste qu'on soutrait puis qu'on assigne: O(3) 

    l 3 : on effectue une comparaison: O(1)

    l 5 : on utilise la fonction sort() pour se simplifier la vie: O(n)  

    l 6 : on rentre dans une boucle de longueur ( n - 1 )

        l 7: calcul de deux valeurs puis une addition puis une comparaison: O(4)

            l 8 : une comparaison et un calcul suivi d'une assignation, cette condition ne retournera n'apparaitra qu'une fois maximum O(3)
            
            l 10 : ici on va faire des boucles en sens inverse . O(??)  c'est ici le point le plus important de la démonstration : si ?? vaut n² l'exercice est un échec.

                l 11 : deux additions, deux calculs de valeurs depuis une chaine, une comparaison: O(5). on quitte la boucle.

                l 13 : pareil O(5). on quitte la fonction.

                l 15 : pareil O(5)

                    l 16: un calcul, une assignation: (3) cette éventualité est la seule qui se répétera au sein de la boucle imbriquée.
            
        l 17: calcul de deux valeurs puis une addition puis une comparaison: O(4) on quiite la fonction.
           
        
    calculons O(??):

    -démontrons par l'absurde: pour obtenir O(n²) il faudrait entamer la deuxième boucle dés l'index i = 0 , or dans ce cas l 9 max = -1 ; l 10 for y in range(-1,-1,-1) pas de boucles et max=-1 pour le rest du programme. la boucle principale aurait une longueur de (n-1) les boucles imbriquées une longueur de 0.

    -Maintenant Supposons un entier M : compris dans l'intervalle [ 1 , len(numbers) - 1 ], les boucles imbriquées démarrent à l'index M donc:
        - numbers[M] + numbers[M+1] > n et numbers[M] + numbers[M-1] < n
        - max = M - 1  ce sera sa valeur maximale qui ne saurait que diminuer au fil des boucles, et aussi la longueur maximale des boucles imbriquées.
        - la quantité de boucles imbriquées est égale à ( len - 1 - M )
        - la compléxité maximale vaudrait donc (len - 1 - M)(M - 1) = len*M - len - M + 1 - M² + M
        - M étant invariable pour éviter la compléxité quadratique il faut que j'arriver à prouver que 
        -  que lenM < len² donc que M < len pour len > 0 et que M > len pour len < 0 
        - or : M > 0  ;  M < len : len > 1


Malgré la boucle imbriqué nous pouvons ranger cette fonction dans la catégorie des complexités linéaire O(n)



