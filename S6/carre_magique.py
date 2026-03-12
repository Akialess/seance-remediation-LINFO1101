"""
L'objectif de cet exercice est de vérifier si une matrice  (liste de listes) est un 
"carré magique".

Un carré est dit "magique" si la somme des nombres de chaque ligne, 
de chaque colonne, et des deux diagonales principales donne exactement 
le même résultat. 

On considérera que le carré fourni est toujours parfait (même nombre de 
lignes que de colonnes, c'est-à-dire de taille n x n).
"""

def est_carre_magique(carre):
    """
    @pre:  carre est une liste de listes d'entiers (matrice carrée n x n)
    @post: retourne True si le carré est magique, sinon retourne False
    """
    
    ### VOTRE CODE ICI


# Tests pour vérifier votre code

carre_ok = [ 
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8] 
] 
print(est_carre_magique(carre_ok)) # : True (la somme est toujours 15)

carrex = [ 
    [2, 7, 4], 
    [4, 5, 4], 
    [4, 1, 9] 
]
print(est_carre_magique(carrex)) # : False

carre_4x4_ok = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
]
print(est_carre_magique(carre_4x4_ok))# : True (la somme est toujours 34)