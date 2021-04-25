from copy import deepcopy
import timeit
etat_final = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]  # etat but, soit le 0 qui symbolise la case vide
operateurs_de_transformations = {"U" : [-1, 0], "D" : [1, 0], "L" : [0, -1], "R" : [0, 1]}

class Taquin :
    # Constructeur de la classe
    def __init__(self, matrice_courante, matrice_precedente, operation) :
        self.matrice_courante = matrice_courante
        self.matrice_precedente = matrice_precedente
        self.operation = operation


#### OLD OLD
def coordonnees(taquin, cellule) :
    for ligne in range(3) :
        if cellule in taquin[ligne] :
            return (ligne, taquin[ligne].index(cellule))

def appliquer_operations(taquin,open,closed) :
    pos_vide = coordonnees(taquin.matrice_courante, 0)

    for operation in operateurs_de_transformations.keys() :
        new_pos = ( pos_vide[0] + operateurs_de_transformations[operation][0], pos_vide[1] + operateurs_de_transformations[operation][1] )
        if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3 : # Vérifier la possibilité d'opération
            new_matrix = deepcopy(taquin.matrice_courante)
            # Switcher les deux cases
            new_matrix[pos_vide[0]][pos_vide[1]] = taquin.matrice_courante[new_pos[0]][new_pos[1]]
            new_matrix[new_pos[0]][new_pos[1]] = 0
            # Ajouter un Objet Taquin à la liste OPEN
            if str(new_matrix) not in closed.keys():
            #conditions : on doit pas ajoutés tous les taquins à la liste open pour être traités :: car il ne sert à rien de traiter un taquin t:
            # 1. déjà traités (se trouve dans closed_liste) -peut déclencher une boucle infinie-
                open[str(new_matrix)] = Taquin(new_matrix, taquin.matrice_courante, operation)
                #si les conditions de traitement sont correctes, on ajoute le fils à la liste open

#### NEW NEW
def New_appliquer_operations(pere_matrix,open,closed):

    # pos de 0
    index = pere_matrix.index(0)

    for operation in operateurs_de_transformations:
        new_matrix = pere_matrix[:]  # fi blassit il deepcopy nestaamlou [:]

        if (index == 0):
            if (operation == 'D'):
                new_matrix[0], new_matrix[3] = new_matrix[3], new_matrix[0]
            if (operation == 'R'):
                new_matrix[0], new_matrix[1] = new_matrix[1], new_matrix[0]
        if (index == 1):
            if (operation == 'D'):
                new_matrix[1], new_matrix[4] = new_matrix[4], new_matrix[1]
            if (operation == 'L'):
                new_matrix[0], new_matrix[1] = new_matrix[1], new_matrix[0]
            if (operation == 'R'):
                new_matrix[1], new_matrix[2] = new_matrix[2], new_matrix[1]
        if (index == 2):
            if (operation == 'D'):
                new_matrix[5], new_matrix[2] = new_matrix[2], new_matrix[5]
            if (operation == 'L'):
                new_matrix[1], new_matrix[2] = new_matrix[2], new_matrix[1]
        if (index == 3):
            if (operation == 'U'):
                new_matrix[0], new_matrix[3] = new_matrix[3], new_matrix[0]
            if (operation == 'D'):
                new_matrix[3], new_matrix[6] = new_matrix[2], new_matrix[1]
            if (operation == 'R'):
                new_matrix[3], new_matrix[4] = new_matrix[4], new_matrix[3]
        if (index == 4):
            if (operation == 'U'):
                new_matrix[1], new_matrix[4] = new_matrix[4], new_matrix[1]
            if (operation == 'D'):
                new_matrix[4], new_matrix[7] = new_matrix[7], new_matrix[4]
            if (operation == 'L'):
                new_matrix[4], new_matrix[3] = new_matrix[3], new_matrix[4]
            if (operation == 'R'):
                new_matrix[4], new_matrix[5] = new_matrix[5], new_matrix[4]
        if (index == 5):
            if (operation == 'U'):
                new_matrix[5], new_matrix[2] = new_matrix[2], new_matrix[5]
            if (operation == 'D'):
                new_matrix[5], new_matrix[8] = new_matrix[8], new_matrix[5]
            if (operation == 'L'):
                new_matrix[5], new_matrix[4] = new_matrix[4], new_matrix[5]
        if (index == 6):
            if (operation == 'U'):
                new_matrix[6], new_matrix[3] = new_matrix[3], new_matrix[6]
            if (operation == 'R'):
                new_matrix[6], new_matrix[7] = new_matrix[7], new_matrix[6]
        if (index == 7):
            if (operation == 'U'):
                new_matrix[7], new_matrix[4] = new_matrix[4], new_matrix[7]
            if (operation == 'L'):
                new_matrix[6], new_matrix[7] = new_matrix[7], new_matrix[6]
            if (operation == 'R'):
                new_matrix[7], new_matrix[8] = new_matrix[8], new_matrix[7]
        if (index == 8):
            if (operation == 'U'):
                new_matrix[5], new_matrix[8] = new_matrix[8], new_matrix[5]
            if (operation == 'L'):
                new_matrix[7], new_matrix[8] = new_matrix[8], new_matrix[7]

        open[str(new_matrix)] = Taquin(new_matrix,pere_matrix, operation) if str(new_matrix) not in closed else None

#### TEST TEST

print(timeit.timeit("New_appliquer_operations([1,2,3,8,0,4,7,6,5],{},{})", "from __main__ import New_appliquer_operations", number=14))

print(timeit.timeit(
    '''appliquer_operations(Taquin([[1,2,3],[8,0,4],[7,6,5]],[[1,2,3],[0,8,4],[7,6,5]],'L'),{},{})''',
    "from __main__ import appliquer_operations, Taquin", number=14))

