**Ce code est en cours d'optimisation vous trouverez les modules de test d'optimisation dans le dossier optimization_tests.**

# A* search algo
```
Algorithme de recherche A* (matrice):
    0. Initialiser open_liste avec le taquin de la matrice d’entrée et closed_liste vide.
    Répéter (open n’est pas vide):
        1. choisissez le meilleur taquin à développer/explorer(le taquin avec le moins f(n)=g(n)+h(n) dans open_liste).
        2. Ajoutez ce taquin père à closed.
        3. Test-but: si la matrice de ce taquin père == état final --> succès --> return(chemin-solution)
        4. Étendez les fils de ce taquin choisi dans open -avec conditions:
            il ne sert à rien de traiter un fils t si:
            c1. il a une matrice déjà traitée (se trouve dans closed_liste) -peut déclencher une boucle infinie-
            c2. il y a un taquin de même matrice que t qui sera traitée (se trouve deja dans open),mais de meilleur f(n) que t.
        5. Supprimer le taquin père de open_liste.
```
# BFS search algo
```
Algorithme de recherche BFS (matrice):
    0. Initialiser open_file avec le taquin de la matrice d’entrée et closed_file vide.
    Répéter (open n’est pas vide):
        1. sélectionnez le taquin à développer/explorer (FIFO, la tete de la File open).
        2. Ajoutez ce taquin père à closed.
        3. Test-but: si la matrice de ce taquin père == état final --> succès --> return(chemin-solution)
        4. Étendez les fils de ce taquin choisi dans open -avec condition:
            c1.il ne sert à rien de traiter un fils t s'il a une matrice déjà traitée (se trouve dans closed) 
               -peut déclencher une boucle infinie-    
        5. Supprimer ce taquin père de open_file.
```
# DFS search algo
```
Algorithme de recherche DFS (matrice):
    0. Initialiser open_pile avec le taquin de la matrice d’entrée et closed_pile vide.
    Répéter (open n’est pas vide):
        1. sélectionnez le taquin à développer/explorer (LIFO, la tete de la Pile open).
        2. Ajoutez ce taquin père à closed.
        3. Test-but: si la matrice de ce taquin père == état final --> succès --> return(chemin-solution)
        4. Étendez les fils de ce taquin choisi dans open -avec condition:
            c1.il ne sert à rien de traiter un fils t s'il a une matrice déjà traitée (se trouve dans closed) 
               -peut déclencher une boucle infinie-    
        5. Supprimer ce taquin père de open_pile.
```

**Remarque** Une simple list, dict ou tuple en Python peut également servir de File (FIFO) et de Pile (LIFO).

**Avec:**

.G le coût (steps), du taquin à l'état initial --> à l'état du taquin n.

.H (heuristique) le coût estimé, du taquin n --> au taquin de l'etat final (calculé par la "distance de Manhattan") 

.opération_appliquée dans {"Up", "Down", "Left", "Right"}

.open qui stocke les taquins à traiter, en commençant par le taquin initial donné.

.closed qui stocke les taquins déjà choisis et traités.
