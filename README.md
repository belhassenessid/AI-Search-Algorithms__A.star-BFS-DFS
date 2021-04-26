# A_star_search_algo___puzzle_3by3

```
Algorithme de recherche A* (matrice):
    0. Initialiser open avec le taquin de la matrice d’entrée et closed vide.
    Répéter (open_list n’est pas vide):
        1. choisissez le meilleur taquin à développer/explorer(le taquin avec le moins f(n)=g(n)+h(n) dans open_list).
        2. Ajoutez ce taquin père à closed_liste.
        3. Test-but: si la matrice de ce taquin père == état final --> succès --> return(chemin-solution)
        4. Étendez les fils de ce taquin choisi à open -avec conditions:
            il ne sert à rien de traiter un fils t si:
            c1. il a une matrice déjà traitée (se trouve dans closed_liste) -peut déclencher une boucle infinie-
            c2. il y a un taquin de même matrice que t qui sera traitée (se trouve deja dans open_liste),mais de meilleur f(n) que t.
        5. Supprimer le taquin père de open_liste.

```
**Avec:**
.G le coût (steps), du taquin à l'état initial --> à l'état du taquin n.

.H (heuristique) le coût estimé, du taquin n --> au taquin de l'etat final (calculé par la "distance de Manhattan") 

.opération_appliquée dans {"Up", "Down", "Left", "Right"}

.Objet Taquin(matrice, matrice_précédente, G, H, opération_appliquée)

.open_liste qui stocke les taquins à traiter, en commençant par le taquin initial donné.

.closed_liste qui stocke les taquins déjà choisis et traités.