import timeit

etat_final = [1, 2, 3,
              8, 0, 4,
              7, 6, 5]  # etat but, soit le 0 qui symbolise la case vide
operateurs_de_transformations = {"U" : -3, "D" : 3, "L" : -1, "R" : 1}
# + l'état initial sera entré dans le module Main.py, le test but est implémenté ci-dessus dans la fonction main()

# Définissons une classe taquin (noeud), caractérisée par sa matrice de valeurs, la matrice du taquin antécédent et l'operation resultante
class Taquin :
    # Constructeur de la classe
    def __init__(self, matrice_courante, matrice_precedente, operation) :
        self.matrice_courante = matrice_courante
        self.matrice_precedente = matrice_precedente
        self.operation = operation

# Définissons une fonction qui retourne les coordonnées (ligne,col) d'une case dans un taquin 3*3 donné
def coordonnees(taquin, cellule) :
    for ligne in range(3) :
        if cellule in taquin[ligne] :
            return (ligne, taquin[ligne].index(cellule))

#Définissons une fonction qui renvoie une liste des nouveaux états des taquins après avoir appliqué toutes les opérations possibles {U,D,R,L} sur un taquin donné
# operations(taquin_père) --> liste(taquins_fils)
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


# Définissons une fonction qui renvoie le chemin_solution/la branche_solution des taquins choisis de l'état initial à l'état final
# une liste contenant des dictionnaires {'operation':opération effectuée, 'taquin':matrice résultant}
def chemin_solution(closed_liste) : #input == dictionnaire des taquins deja choisis et parcourus de la forme {str(matrice):Objet Taquin(),...}
    taquin = closed_liste[str(etat_final)]
    branche = list()

    while taquin.operation :
        branche.append({
            'operation' : taquin.operation,
            'taquin' : taquin.matrice_courante
        })
        taquin = closed_liste[str(taquin.matrice_precedente)]
    branche.append({
        'operation' : 'taquin initial sans opération de transformation',
        'taquin' : taquin.matrice_courante
    })
    branche.reverse()
    #print(len(branche_solution))

    return branche


def main(puzzle_initial) : #input == matrice (liste de 3 listes de 3 entiers entre 0 et 8)

    start_algo=timeit.default_timer() #commencer de compter le temps d'exe

    #Soit l'open_liste qui stocke les noeuds à traiter, en commençant par le t initial.
    # un dictionnaire sous la forme {clé0:valeur0,...} avec str(matrice) comme clé, un Objet Taquin comme valeur
    # Un dict Python peut servir de File et aussi de Pile, dans cet algo on le traite comme une File (FIFO)
    open_liste = {str(puzzle_initial) : Taquin(puzzle_initial, puzzle_initial, "")}

    #Soit le close_liste qui stocke les taquins déjà choisis et traités
    closed_liste = {}

    while True :

        taquin_a_traiter = list(open_liste.values())[0] #I. choisir le taquin à étendre (FIFO)

        closed_liste[str(taquin_a_traiter.matrice_courante)] = taquin_a_traiter #II. ajouter ce taquin à la liste closed
        if taquin_a_traiter.matrice_courante == etat_final :#III. Test-but
            stop_algo = timeit.default_timer()
            time = stop_algo-start_algo
            return chemin_solution(closed_liste), len(closed_liste), format(time, '.8f') #chemin,noeuds explorés,temps

        appliquer_operations(taquin_a_traiter,open_liste,closed_liste) #IV. étendre ce taquin père dans une Liste_fils

        #VI. Supprimer le taquin père (taquin_a_traiter) de la liste open
        del open_liste[str(taquin_a_traiter.matrice_courante)]