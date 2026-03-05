def combien(n):    
    """
    @pre:  n est un nombre entier > 0
    @post: retourne le nombre de series d'entiers consecutifs
           strictement positifs dont la somme est egale a n
    """
    pass



print(combien(1))   # attendu: 1  -> (1)
print(combien(2))   # attendu: 1  -> (2)
print(combien(3))   # attendu: 2  -> (3), (1+2)
print(combien(4))   # attendu: 1  -> (4)
print(combien(5))   # attendu: 2  -> (5), (2+3)
print(combien(6))   # attendu: 2  -> (6), (1+2+3)
print(combien(7))   # attendu: 2  -> (7), (3+4)
print(combien(8))   # attendu: 1  -> (8)
print(combien(9))   # attendu: 3  -> (9), (4+5), (2+3+4)
print(combien(10))  # attendu: 2  -> (10), (1+2+3+4)
print(combien(15))  # attendu: 4  -> (15), (7+8), (4+5+6), (1+2+3+4+5)
