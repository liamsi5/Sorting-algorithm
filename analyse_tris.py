#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`analyse_tris` module
:author: FIL - Faculté des Sciences et Technologies - Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: janvier 2017
:dernières révisions: février 2018, février 2019

Analyse empirique des tris

"""
from random import shuffle
from compare import compare, gen_compteur_compare
from tris import *

################################################
#  ANALYSE EMPIRIQUE DES TRIS                  #
################################################


def analyser_tri(tri, n, t):
    """
    :param tri: (fonction) fonction de tri
    :param n: (int) nombre de listes aléatoires à trier
    :param t: (int) taille des listes à trier
    :return: (float) le nombre moyen de comparaisons effectués par l'algo tri
         pour trier des listes de taille t, la moyenne étant calculée
         sur n listes aléatoires.
    :CU: n > 0, t >= 0
    """
    res = 0
    comp = gen_compteur_compare(compare)
    for i in range(n):
        comp(reset=True)
        l = [k for k in range(t)]
        shuffle(l)
        tri(l, comp=comp)
        res += comp(nb=True)
    return res / n


if __name__ == '__main__':    
    from matplotlib import pyplot as plt
    
    # Calcul de nombres moyens de comparaison pour des listes
    # de tailles comprises entre 0 et TAILLE_MAX
    NB_ESSAIS = 50
    TAILLE_MAX = 100
    c_select = [0] * (TAILLE_MAX + 1)
    c_insert = [0] * (TAILLE_MAX + 1)
    
    for t in range(TAILLE_MAX + 1):
        c_select[t] = analyser_tri(tri_select, 1, t)
        # inutile de moyenner pour le tri par sélection
        c_insert[t] = analyser_tri(tri_insert, NB_ESSAIS, t)

    # Sauvegarde des données calculées dans un fichier au format CSV
    prem_ligne = 'taille;"tri séléction";"tri insertion"\n'
    ligne = '{:3d};{:8.2f};{:8.2f}\n'
    with open('analyse_tris.csv', 'wt', encoding='utf8') as sortie:
        sortie.write(prem_ligne)
        for t in range(TAILLE_MAX + 1):
            sortie.write(ligne.format(t,
                                      c_select[t],
                                      c_insert[t]))

    # Représentation graphique
    plt.plot(list(range(TAILLE_MAX + 1)), c_select, 'b.', label='Tri sélection')
    plt.plot(list(range(TAILLE_MAX + 1)), c_insert, 'r.', label='Tri insertion')
    plt.title('Tris : nbre de comparaisons')
    plt.legend()
    plt.xlabel('n = taille des listes')
    plt.ylabel('c(n) = nbre de comparaisons')
    plt.savefig('tris_nbcomp.png')
    plt.show()

