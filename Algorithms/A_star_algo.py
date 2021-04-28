from copy import deepcopy
import timeit

etat_final = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]  # etat but, soit le 0 qui symbolise la case vide
operateurs_de_transformations = {"U" : [-1, 0], "D" : [1, 0], "L" : [0, -1], "R" : [0, 1]}
# + l'état initial sera entré dans le module MainWindow.py, le test but est implémenté ci-dessus dans la fonction main()

# Définissons une classe taquin (noeud), caractérisée par sa matrice de valeurs, la matrice du taquin antécédent, l'operation resultante et les valeurs de l'algorithme A*, F=G+H.
class Taquin :
    # Constructeur de la classe
    def __init__(self, matrice_courante, matrice_precedente, g, h, operation) :
        self.matrice_courante = matrice_courante
        self.matrice_precedente = matrice_precedente
        self.g = g  # Coût (steps), du point de départ --> à l'etat du taquin n
        self.h = h  # Coût heuristique estimé, du taquin n --> au taquin à l'etat final (calculé par la "distance de Manhattan")
        self.operation = operation

    # L'agorithme de recherche A* sélectionne le chemin_solution qui minimise la fonction: f(taquin) = G(taquin)+H(taquin)
    # définissons une methode qui calcule ce paramètre
    def f(self) :
        return self.g + self.h


# Définissons une fonction qui retourne les coordonnées (ligne,col) d'une case dans un taquin 3*3 donné
def coordonnees(taquin, cellule) :
    for ligne in range(3) :
        if cellule in taquin[ligne] :
            return (ligne, taquin[ligne].index(cellule))


#Définissons une fonction qui renvoie la valeur de l'heuristique H qui est l'estimation à vol d'oiseau de la distance
# à quelle se trouve le but (calculé par Manhattan algo: H=|xf-x0|+|yf-y0|)
#C'est-à-dire le coût total du déplacement de chaque case -sauf la case vide- de son état actuel dans un taquin i à son état final dans
# le taquin f, en négligeant la présence d'autres cases (murs) entre le chemin_solution des 2 états qui peuvent empecher ce mouvement
def cout_heuristique(etat_courant) :
    cout = 0
    for ligne in range(3) :
        for col in range(3) :
            if etat_courant[ligne][col] != 0: #sauf la case vide
                (ligne_final, col_final) = coordonnees(etat_final, etat_courant[ligne][col])  # Coordonnées de la case à l'état final du taquin
                cout += abs(ligne - ligne_final) + abs(col - col_final)  # Formule de distance de Manhattan
    return cout

#Définissons une fonction qui insere les fils de t dans open après avoir appliqué toutes les opérations possibles {U,D,R,L}
def appliquer_operations(taquin,open,closed) :
    pos_vide = coordonnees(taquin.matrice_courante, 0)

    for operation in operateurs_de_transformations:
        new_pos = ( pos_vide[0] + operateurs_de_transformations[operation][0], pos_vide[1] + operateurs_de_transformations[operation][1] )
        if 0 <= new_pos[0] <3 and 0 <= new_pos[1] < 3 : # Vérifier la possibilité d'opération
            new_matrix = deepcopy(taquin.matrice_courante)
            # Switcher les deux cases
            new_matrix[pos_vide[0]][pos_vide[1]] = taquin.matrice_courante[new_pos[0]][new_pos[1]]
            new_matrix[new_pos[0]][new_pos[1]] = 0
            # Ajouter un Objet Taquin à la liste open avec des conditions:
                #il ne sert à rien de traiter un taquin t si:
                    #c1. il est déjà traités (se trouve dans closed_liste) -peut déclencher une boucle infinie-
                    #c2. il y a un taquin de même matrice que t qui sera traitée (se trouve deja dans open_liste), mais de meilleur f(n) que t.
            g,h=taquin.g+1, cout_heuristique(new_matrix)
            if not ( str(new_matrix) in closed.keys() or \
            str(new_matrix) in open.keys() and open[str(new_matrix)].f() < h+g ) :
                open[str(new_matrix)] = Taquin(new_matrix, taquin.matrice_courante,g,h, operation)


# Définissons une fonction qui renvoie le meilleur taquin de l'ensemble des taquins fils -meilleur c.-à-d plus petite f(n)=g(n)+h(n)
def meilleur_taquin(open_liste) : #input == dictionnaire des taquins prets à traiter de la forme {str(matrice):Objet Taquin(),...}
    first_iter = True

    for taquin in open_liste.values() :
        if first_iter or taquin.f() < bestF :
            first_iter = False
            meilleur_taquin = taquin
            bestF = meilleur_taquin.f()
    return meilleur_taquin

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

    return branche


def main(puzzle_initial) : #input == matrice (liste de 3 listes de 3 entiers entre 0 et 8)

    start_algo=timeit.default_timer() #commencer de compter le temps d'exe

    #Soit l'open_liste qui stocke les noeuds à traiter, en commençant par le t initial.
    # un dictionnaire sous la forme {clé0:valeur0,...} avec str(matrice) comme clé, un Objet Taquin comme valeur
    open_liste = {str(puzzle_initial) : Taquin(puzzle_initial, puzzle_initial, 0, cout_heuristique(puzzle_initial), "")}

    #Soit le close_liste qui stocke les taquins déjà choisis et traités
    closed_liste = {}
    i=0
    while True :
        #test print("iter", i, " : open : ", open_liste.keys(), "** closed :", closed_liste.keys())
        #test i+=1
        taquin_a_traiter = meilleur_taquin(open_liste) #I. choisir le taquin à étendre, pour continuer dans cette branche_solution du meilleur f(n)
        closed_liste[str(taquin_a_traiter.matrice_courante)] = taquin_a_traiter #II. ajouter ce taquin à la liste closed

        if taquin_a_traiter.matrice_courante == etat_final : #III. Test-but
            stop_algo=timeit.default_timer()
            time=stop_algo-start_algo
            #TEST print("iter fin", i, " : open : ", open_liste.keys(), "** closed :", closed_liste.keys())
            return chemin_solution(closed_liste), len(open_liste)-1+len(closed_liste), format(time, '.8f') #chemin,noeuds explorés,temps

        appliquer_operations(taquin_a_traiter,open_liste,closed_liste) #IV. étendre ce taquin père dans open
        
        #V. Supprimer le taquin père (taquin_a_traiter) de la liste open
        del open_liste[str(taquin_a_traiter.matrice_courante)]
        #print(open_liste.keys(), "**", closed_liste.keys())


#print(timeit.timeit("main([[1, 2, 3], [8, 6, 4], [7, 5, 0]])","from __main__ import main",number=1000))