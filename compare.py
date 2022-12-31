#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`compare` module
:author: FIL - FST - Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: 2016, january
:dernière révision: février 2018

Fonction de comparaison 
pour l'analyse des algos de recherche et de tri

"""
from functools import wraps

def compare(x, y):
    """
    :param x, y: (quelconque) deux données de mêmes types
    :return: (int) 
      - -1 si x < y
      - 0 si x == y
      - 1 si x > y
    :CU: x et y doivent être d'un type pour lequel les opérateurs de comparaison <, <=, == 
         peuvent s'appliquer
    :Exemples:

    >>> compare(1, 3)
    -1
    >>> compare(3, 1)
    1
    >>> compare(3, 3)
    0
    """
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

def seq_compare_deuxieme(x, y):
    """
    :param x, y: (tuples ou listes) deux structures séquentielles
    :return: (int) 
      - -1 si x[1] < y[1]
      - 0 si x[1] == y[1]
      - 1 si x[1] > y[1]
    :CU: x et y doivent être des structures séquentielles de longueurs au moins égales à deux,
         et dont les deuxièmes éléments sont tels que  les opérateurs de comparaison <, <=, == 
         peuvent s'appliquer
    :Exemples:

    >>> seq_compare_deuxieme((4, 3), (1, 5))
    -1
    >>> seq_compare_deuxieme([1, 5], [4, 3])
    1
    >>> seq_compare_deuxieme([3, 4], [1, 4])
    0
    """
    if x[1] < y[1]:
        return -1
    elif x[1] > y[1]:
        return 1
    else:
        return 0


def gen_compteur_compare(comp):
    """
    :param comp: (fonction) une fonction de comparaison. 
    :return: (fonction) une fonction de comparaison identique à ``comp``,
          mais dotée d'un paramètre optionnel permettant d'obtenir le
          nombre d'appels qui a été fait à cette fonction.
    :CU: aucune
    :Exemples:

    >>> comp1 = gen_compteur_compare(compare)
    >>> comp1(1, 2)
    -1
    >>> comp1(1, 1)
    0
    >>> comp1(1, 0)
    1
    >>> comp1(nb=True)
    3
    >>> comp2 = gen_compteur_compare (compare)
    >>> comp2(1, 2)
    -1
    >>> comp2(nb=True)
    1
    >>> comp1(nb=True)
    3
    >>> comp1(reset=True)
    >>> comp1(nb=True)
    0
    """
    cpt = {'nb' : 0}
    @wraps(comp)
    def f(x=0, y=0, nb=False, reset=False):
        if nb:
            return cpt['nb']
        elif reset:
            cpt['nb'] = 0
        else:
            cpt['nb'] += 1
            return comp(x,y)
    return f

compare = gen_compteur_compare(compare)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
