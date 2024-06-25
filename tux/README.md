solution proposée pour la fonction tux() :

    -je produis un Dictionnaire vide une valeur max.
    -je parcours la liste en rajoutant dans mon dictionnaire une paire clé / valeur => index de ma liste / valeur dans ma liste.
    -je trie le dictionnaire par ses valeurs.
    -je parcours en parralléle ma liste et le dictionnaire trié, si je retrouve un index qui n'a pas changé de position je peux le retourner comme résultat si et seulement si il est supérieur à tous les index précents. 
        -l'index atteint (i) doit être supérieur à tous les index trié précedents, sinon cela signifie qu'une ou plusieurs valeurs inférieures au pivot situées plus loin dans la liste a ou ont changés de position avec la même quantité de valeurs supérieures au pivot situées avant lui dans la liste.
    
    -pour vérifier cette supériorité, à chaque nouvel index trié qui est parcouru je vérifie s'il est supérieur à max, si c'est le cas max est réassigné à cet index trié. Max est initialement assigné à -1 dans l'éventualité où le pivot serait à l'index 0


Maintenant on calcule la compléxité algorithmique:

    l 2 à 3 : O(2)
    l 4 : une boucle de longueur n:
        l 5 : des assignations pour une valeur totale systématique de O(n)
    l 6 : un tri sur un dictionnaire de longueur n donc O(n)
    l 7 : une boucle de longueur n:
        l 8 : une comparaison avec deux calculs: O(3)
            l 9 : une comparaison O(1)
        l 11 : une comparaison avec un calcul O(2):
            l 12 : une assignation et un calcul O(2)
        
        Dans le pire des cas la boucle initiée ligne 7 mesurera donc O(8n)

Dans le pire des cas on reste donc à O(10n+2), sur une compléxité linéaire donc.
