import timeit

etat_final = [1, 2, 3,
              8, 0, 4,
              7, 6, 5]  # etat but, soit le 0 qui symbolise la case vide
operateurs_de_transformations = {"U": -3, "D": 3, "L": -1, "R": 1}
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

#Définissons une fonction qui renvoie la valeur de l'heuristique H qui est l'estimation à vol d'oiseau de la distance
# à quelle se trouve le but (calculé par Manhattan algo: H=|xf-x0|+|yf-y0|)
#C'est-à-dire le coût total du déplacement de chaque case -sauf la case vide- de son état actuel dans un taquin i à son état final dans
# le taquin f, en négligeant la présence d'autres cases (murs) entre le chemin_solution des 2 états qui peuvent empecher ce mouvement
def cout_heuristique(matrix) :

    # Distance de Manhattan de deplacement de la v_j de sa position i à la case finale (i de 0 à 8 les indices des listes)
    v_1 = (0, 1, 2, 1, 2, 3, 2, 3, 4)  # distance de deplacement du "1", de la case i à la case final
    v_2 = (1, 0, 1, 2, 1, 2, 3, 2, 3) # H2(de i à 1)=v_2[i]
    v_3 = (2, 1, 0, 3, 2, 1, 4, 3, 2)
    v_4 = (3, 2, 1, 2, 1, 0, 3, 2, 1)
    v_5 = (4, 3, 2, 3, 2, 1, 2, 1, 0)
    v_6 = (3, 2, 3, 2, 1, 2, 1, 0, 1)
    v_7 = (2, 3, 4, 1, 2, 3, 0, 1, 2)
    v_8 = (1, 2, 3, 0, 1, 2, 1, 2, 3)

    return v_1[matrix.index(1)]+v_2[matrix.index(2)]+v_3[matrix.index(3)]+v_4[matrix.index(4)]+v_5[matrix.index(5)]+v_6[matrix.index(6)]+v_7[matrix.index(7)]+v_8[matrix.index(8)]


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


def main(puzzle_initial) : #input: liste simple
    # 0. Initialisation
    start_algo=timeit.default_timer() #commencer de compter le temps d'exe

    #Soit l'open_liste qui stocke les noeuds à traiter, en commençant par le t initial.
    # un dictionnaire sous la forme {clé0:valeur0,...} avec str(matrice) comme clé, un Objet Taquin comme valeur
    open_liste = {str(puzzle_initial) : Taquin(puzzle_initial, puzzle_initial, 0, cout_heuristique(puzzle_initial), "")}

    #Soit le close_liste qui stocke les taquins déjà choisis et traités
    closed_liste = {}
    #FIN 0.

    #print(open_liste)
    while True :
        #I. choisir le taquin à étendre de meilleur f(n)  # Recherche seq
        v = True
        for taquin in open_liste.values():
            if v or taquin.f() < bestF:
                v = False
                meilleur_taquin = taquin
                bestF = meilleur_taquin.f()
        #FIN I.

        # II. ajouter ce taquin à la liste closed
        closed_liste[str(meilleur_taquin.matrice_courante)] = meilleur_taquin
        #FIN II.

        # III. Test-but
        if meilleur_taquin.matrice_courante == etat_final :
            stop_algo=timeit.default_timer()
            time=stop_algo-start_algo
            return 0 #chemin_solution(closed_liste), len(open_liste)-1+len(closed_liste), format(time, '.8f') #chemin,noeuds explorés,temps
        # FIN III.

        # IV. étendre ce taquin père dans open
         # ajouter dans open les nouveaux états après avoir appliqué toutes les opérations possibles {U,D,R,L} sue le taquin pere
        matrix_pere=meilleur_taquin.matrice_courante
        pos_vide = matrix_pere.index(0)
        for operation in operateurs_de_transformations.values():
            new_pos = pos_vide + operation
            if 0 <= new_pos <= 8:  # Vérifier la possibilité d'opération
                new_matrix = matrix_pere[:]
                # Switcher les deux cases
                new_matrix[new_pos], new_matrix[pos_vide] = new_matrix[pos_vide], new_matrix[new_pos]
                # Ajouter un Objet Taquin à la liste OPEN
                if not (str(new_matrix) in closed_liste.keys() or \
                        str(new_matrix) in open_liste.keys() and open_liste[str(new_matrix)].f() < meilleur_taquin.f()):
                    # Ajouter un Objet Taquin à la liste open avec des conditions:
                        # il ne sert à rien de traiter un taquin t si:
                            # c1. il est déjà traités (se trouve dans closed_liste) -peut déclencher une boucle infinie-
                            # c2. il y a un taquin de même matrice que pere qui sera traitée (se trouve deja dans open_liste), mais de meilleur f(n) que t.
                    open_liste[str(new_matrix)] = Taquin(new_matrix, matrix_pere, meilleur_taquin.g + 1,
                                                         cout_heuristique(new_matrix), operation)
                    #si les conditions de traitement sont correctes, on ajoute le fils à la liste open
        # FIN IV.

        #V. Supprimer le taquin père (taquin_a_traiter) de la liste open
        del open_liste[str(meilleur_taquin.matrice_courante)]
        #FIN V.

        #print(open_liste.keys(), "**", open_liste.values())

print(timeit.timeit("main([1, 3, 2, 5, 4, 7, 0, 6, 8])","from __main__ import main",number=1000))