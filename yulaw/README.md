
Yulaw vise à développer une fonction capable de transformer une chaîne de caractères donnée en éliminant tous les doublons, tout en préservant la première occurrence de chaque caractère. 

Pour atteindre cet objectif, j'ai conçu une fonction yulaw qui reçoit une chaîne de caractères en entrée et produit une nouvelle chaîne, résultat de l'union des caractères sans doublons. L'aspect clé de notre solution réside dans l'utilisation d'une structure de données de type ensemble (set) pour suivre les caractères déjà rencontrés lors du parcours de la chaîne initiale.

J'ai initialisé un ensemble vide pour garder une trace des caractères uniques rencontrés au fur et à mesure de ma progression dans la chaîne.

En itérant sur chaque caractère, j'ai utilisé cet ensemble pour vérifier si un caractère avait déjà été ajouté. Cette méthode m'a permis de filtrer efficacement les doublons.

La chaîne de sortie a été construite en accumulant uniquement les premières occurrences de chaque caractère, préservant ainsi leur unicité.

J'ai choisi cette méthode car elle me permettait de respecter strictement la contrainte de complexité en temps tout en simplifiant la logique nécessaire pour filtrer les doublons. L'utilisation d'un ensemble s'est avérée être la solution la plus efficace pour atteindre cet objectif, grâce à sa capacité à effectuer des vérifications et des ajouts en temps constant moyen.

J'espère que mon approche inspirera d'autres à explorer des solutions créatives pour leurs propres défis de programmation.