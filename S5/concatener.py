"""
L'objectif de regrouper les valeurs consécutives identiques  d'une liste en les "collant" ensemble.

Par exemple, si on a la liste [1, 1, 1, 2, 2], on colle les 1 ensemble et les 2 ensemble.
Le résultat attendu est donc une nouvelle liste contenant [111, 22].
"""

def concatener_similaires(lst):
    """
    @pre:  lst est une liste d'entiers
    @post: retourne une nouvelle liste où les entiers consécutifs identiques 
           ont été concaténés pour former un seul entier.
    """
    
    ### VOTRE CODE ICI

# Tests pour vérifier votre code
k = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4]
print(concatener_similaires(k)) # : [111, 22, 333, 44]

e = [11, 11, 123, 123, 55, 55]
print(concatener_similaires(e)) # : [1111, 123123, 5555]

print(concatener_similaires([1, 2, 3, 1])) # : [1, 2, 3, 1]

print(concatener_similaires([])) # : []