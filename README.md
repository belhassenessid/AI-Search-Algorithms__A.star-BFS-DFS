# A_star_search_algo___puzzle_3by3

```
Algorithme de recherche A* (matrice):
    0. initialise open avec le taquin input initial et closed vide
    Repeter: 
        1. Choisir le taquin à étendre, pour continuer dans cette branche du meilleur f(n)=g(n)+h(n) parmis open.
        2. Ajouter ce taquin père à closed_liste.
        3. Test-but: si la matrice de ce taquin père == état final --> succès --> return(chemin_solution)
                    si non :
        4. Ajouter les fils à la liste open pour être traités -avec conditions:
            il ne sert à rien de traiter un taquin t si:
            c1. il est déjà traités (se trouve dans closed_liste) -peut déclencher une boucle infinie-
            c2. il y a un taquin de même matrice que t qui sera traitée (se trouve deja dans open_liste),
                       mais de meilleur f(n) que t.
        5. Supprimer le taquin père de open_liste.
```
**Avec:**

.La matrice 3*3 contient des valeurs entre 0 et 8 (0 pour vide).

.G le coût (steps), du taquin à l'état initial --> à l'état du taquin n.

.H (heuristique) le coût estimé, du taquin n --> au taquin de l'etat final (calculé par la "distance de Manhattan") 

.opération_appliquée dans {"Up", "Down", "Left", "Right"}

.Objet Taquin(matrice, matrice_précédente, G, H, opération_appliquée)

.open_liste qui stocke les taquins à traiter, en commençant par le taquin initial donné.

.closed_liste qui stocke les taquins déjà choisis et traités.