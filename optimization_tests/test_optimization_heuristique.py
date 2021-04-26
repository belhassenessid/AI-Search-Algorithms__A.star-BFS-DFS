import timeit
              #0  1  2
etat_final = [[1, 2, 3], #0
              [8, 0, 4], #1
              [7, 6, 5]] #2

#### OLD OLD
def coordonnees(taquin, cellule) :
    for ligne in range(3) :
        if cellule in taquin[ligne] :
            return (ligne, taquin[ligne].index(cellule))
def cout_heuristique(etat_courant) :
    cout = 0
    for ligne in range(3) :
        for col in range(3) :
            if etat_courant[ligne][col] != 0: #sauf la case vide
                (ligne_final, col_final) = coordonnees(etat_final, etat_courant[ligne][col])  # Coordonnées de la case à l'état final du taquin
                cout += abs(ligne - ligne_final) + abs(col - col_final)  # Formule de distance de Manhattan
    return cout

#### NEW NEW
def New_cout_heuristique(node):

    global v_0,v_1,v_2,v_3,v_4,v_5,v_6,v_7,v_8

    #Distance de Manhattan de deplacement de la v_j de sa position i à la case finale (i de 0 à 8 les indices des listes)
    #v_0 = (2, 1, 2, 1, 0, 1, 2, 1, 2)
    v_1 = (0, 1, 2, 1, 2, 3, 2, 3, 4) #distance de deplacement du 1, de i à la case final
    v_2 = (1, 0, 1, 2, 1, 2, 3, 2, 3)
    v_3 = (2, 1, 0, 3, 2, 1, 4, 3, 2)
    v_4 = (3, 2, 1, 2, 1, 0, 3, 2, 1)
    v_5 = (4, 3, 2, 3, 2, 1, 2, 1, 0)
    v_6 = (3, 2, 3, 2, 1, 2, 1, 0, 1)
    v_7 = (2, 3, 4, 1, 2, 3, 0, 1, 2)
    v_8 = (1, 2, 3, 0, 1, 2, 1, 2, 3)

    #c0=v_0[node.index(0)]
    c1=v_1[node.index(1)]
    c2=v_2[node.index(2)]
    c3=v_3[node.index(3)]
    c4=v_4[node.index(4)]
    c5=v_5[node.index(5)]
    c6=v_6[node.index(6)]
    c7=v_7[node.index(7)]
    c8=v_8[node.index(8)]
    valorTotal = c1+c2+c3+c4+c5+c6+c7+c8
    return valorTotal


#### TEST TEST
print(timeit.timeit("New_cout_heuristique([1,2,3,8,0,4,7,6,5])", "from __main__ import New_cout_heuristique", number=17000))
print(timeit.timeit("cout_heuristique([[1,2,3],[8,0,4],[7,6,5]])", "from __main__ import cout_heuristique", number=17000))
