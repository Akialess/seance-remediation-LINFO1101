"""
Un nombre est un palindrome si, en lisant les chiffres dont ce nombre est composé de gauche à droite 
ou de droite à gauche, on obtient exactement le même nombre. 

Par exemple, les nombres 363, 1221 et 9985899 sont des palindromes, mais 1451 ne l'est pas. 
Les nombres composés d'un seul chiffre comme 0, 1, 2, 3 sont trivialement des palindromes également.
"""

def is_palindrome(n) :
    """
    @pre:  n est un entier
    @post: retourne True si le nombre n est un palindrome
           sinon retourne False
    """

    ### VOTRE CODE ICI

def palindrome_chiffres(n) :
    """
    @pre:  n est un entier
    @post: retourne le premier entier p > n qui est un palindrome
    """

    ### VOTRE CODE ICI


print(is_palindrome(1))             # True
print(is_palindrome(12321))         # True
print(is_palindrome(1451))          # False


print(palindrome_chiffres(1))       # 2
print(palindrome_chiffres(100))     # 101
print(palindrome_chiffres(123))     # 131