## Exercice 7/13 : Falafel/ Vérification de Palindrome

J'ai développé la fonction falafel pour vérifier si une chaîne de caractères peut être réarrangée pour former un palindrome. Mon approche repose sur deux règles clés qui caractérisent les palindromes :

Pour une séquence de longueur paire, il est nécessaire que tous les caractères soient présents en nombre pair pour former un palindrome.
Pour une séquence de longueur impaire, il est possible d'avoir un seul caractère en nombre impair, les autres devant obligatoirement avoir des occurrences paires.

J'ai implémenté une logique qui compte la fréquence de chaque caractère au sein d'un dictionnaire. Après avoir comptabilisé ces fréquences, je procède à une vérification pour m'assurer que la chaîne de caractères respecte les conditions nécessaires à la formation d'un palindrome.

La méthode choisie garantit une complexité temporelle de O(n), où n est la longueur de la chaîne de caractères.

- La chaîne est parcourue une seule fois pour établir le décompte des caractères, rendant l'opération efficace.
- Une seconde itération, tout aussi linéaire, sert à confirmer la possibilité de former un palindrome.
- Les opérations sur le dictionnaire, telles que l'insertion et la vérification, sont en temps constant, de même pour l'incrémentation du compteur d'occurrences impaires.

En conclusion, l'algorithme falafel que j'ai conçu examine si une permutation de la séquence fournie peut constituer un palindrome tout en respectant strictement la contrainte de performance imposée par le sujet.
La logique employée et la structure de données utilisée permettent d'assurer une efficacité optimale et une exécution conforme aux attentes du problème posé.
