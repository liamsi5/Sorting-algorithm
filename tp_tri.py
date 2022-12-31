# -*- coding: utf-8 -*-

# Nom(s) : ismail chaf-i
# Date de création : 14/03/2020.
# Objet : 'TP5'

# ici avant le if __name__ ... les diverses définitions de fonctions ou autres.



from random import shuffle
#question
n=10
l= list (i for i in range (0,n))



def liste_alea (n):
    """  param: un entier n,
         fonction qui construit une liste de longueur n contenant les entiers 0 à n-1 mélangés.
    """

    l= list (i for i in range (n))
    shuffle(l)
    return l


# with line ca sert à faire des graphes avec des lignes
def formate():
    for i in range (101):
        print ('{:4d}' .format(i),';','{:^5d}'.format(int((i*(i-1))/2)) )


#la fonction ne renvoie rien
    
#
from timeit import timeit    
from tris import tri_select
TAILLE_MAX = 100

def chronométrage():
    res = []
    for i in range(0,TAILLE_MAX) :
        res += [timeit(stmt='{}'.format(tri_select(liste_alea(i))), setup='', number=5000)]
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

    # ici sous la portée du if __name__ ... tous les essais que vous voulez (autre que les doctests)


