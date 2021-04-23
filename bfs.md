# Breadth First Search (BFS) Algorithm

```
Algorithme de recherche BFS:
    1. initialiser la file OPEN
    2. Ajouter le taquin initial à closed_liste.
    3. Test-but: si la matrice de ce taquin père == état final --> succès --> return(chemin)
                    si non :
    4. Ajouter les fils de ce taquin père à la liste open pour être traités -avec conditions:
            il ne sert à rien de traiter un taquin t si:
            c1. il est déjà traités (se trouve dans closed_liste) -peut déclencher une boucle infinie-
    5. Supprimer le taquin père de open_liste.
    
```