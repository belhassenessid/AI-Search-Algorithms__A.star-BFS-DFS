def coordonnees(taquin, cellule) :
    for ligne in range(3) :
        if cellule in taquin[ligne] :
            return (ligne, taquin[ligne].index(cellule))

etat_final = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def cout_heuristique(etat_courant) :
    cout = 0
    for ligne in range(3) :
        for col in range(3) :
            (ligne_final, col_final) = coordonnees(etat_final, etat_courant[ligne][col])
            cout += abs(ligne - ligne_final) + abs(col - col_final)
    return cout

print(cout_heuristique([[1,2,3],[4,5,0],[6,7,8]]))