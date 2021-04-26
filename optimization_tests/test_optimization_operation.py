import timeit
etat_final = [1, 2, 3,
              8, 0, 4,
              7, 6, 5]  # etat but, soit le 0 qui symbolise la case vide


operateurs_de_transformations = {"U": -3, "D": 3, "L": -1, "R": 1}

class Taquin :
    # Constructeur de la classe
    def __init__(self, matrice_courante, matrice_precedente, operation) :
        self.matrice_courante = matrice_courante
        self.matrice_precedente = matrice_precedente
        self.operation = operation


#### NEW NEW
def appliquer_operations(matrix_pere,open,closed) :
    pos_vide = matrix_pere.index(0)
#{"U" : [-3], "D" : [3], "L" : [-1], "R" : [1]}
    for operation in operateurs_de_transformations.values() :
        new_pos = pos_vide+operation
        if 0 <= new_pos <= 8 : # Vérifier la possibilité d'opération
            new_matrix = matrix_pere[:]
            # Switcher les deux cases
            new_matrix[new_pos],new_matrix[pos_vide]=new_matrix[pos_vide],new_matrix[new_pos]
            # Ajouter un Objet Taquin à la liste OPEN
            if str(new_matrix) not in closed.keys():
            #conditions : on doit pas ajoutés tous les taquins à la liste open pour être traités :: car il ne sert à rien de traiter un taquin t:
            # 1. déjà traités (se trouve dans closed_liste) -peut déclencher une boucle infinie-
                open[str(new_matrix)] = Taquin(new_matrix, matrix_pere, operation)
                #si les conditions de traitement sont correctes, on ajoute le fils à la liste open

#### TEST TEST

print(timeit.timeit("appliquer_operations([1,2,3,8,0,4,7,6,5],{},{})","from __main__ import appliquer_operations", number=26))
