import operator
import timeit

class Taquin :
    def __init__(self, matrice_courante, matrice_precedente, g, h, operation) :
        self.matrice_courante = matrice_courante
        self.matrice_precedente = matrice_precedente
        self.g = g
        self.h = h
        self.operation = operation
    def f(self):
        return self.g + self.h


input_defaut = [[8, 4, 2],
                [5, 6, 1],
                [3, 0, 7]]
input_defaut2=[[7, 4, 2],
                [5, 0, 1],
                [3, 8, 7]]

open_liste={str(input_defaut): Taquin(input_defaut, input_defaut, 0, 11, ""),
            str(input_defaut2): Taquin(input_defaut2, input_defaut, 1, 156, "U")}

#### OLD OLD
def meilleur_taquin(open_liste) :
    first_iter = True

    for taquin in open_liste.values() :
        if first_iter or taquin.f() < bestF :
            first_iter = False
            meilleur_taquin = taquin
            bestF = meilleur_taquin.f()
    return meilleur_taquin

### NEW NEW


### TEST TEST
print(timeit.timeit("min(open_liste, key=lambda x: open_liste[x].f())", "from __main__ import open_liste", number=14))

print(timeit.timeit("meilleur_taquin(open_liste)","from __main__ import meilleur_taquin, open_liste", number=14))

print(min(open_liste, key=lambda x: open_liste[x].f()),'==',meilleur_taquin(open_liste).matrice_courante)