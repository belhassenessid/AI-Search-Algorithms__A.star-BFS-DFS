from A_star_algo import main
import tkinter  as tk
from colorama import Fore, Back, Style  # Fore et Back pour colorer l'écriture et son font, Style à son style


# Définissons les éléments de décoration graphiques (couleurs, styles, formes et matrices) :
coin_bas_gauche = '\u2514'  # └
coin_bas_droit = '\u2518'  # ┘
coin_haut_droit = '\u2510'  # ┘
coin_haut_gauche = '\u250C'  # ┌

croisement_milieu = '\u253C'  # ┼
croisement_haut = '\u252C'  # ┬
croisement_bas = '\u2534'  # ┴
croisement_droit = '\u2524'  # ┤
croisement_gauche = '\u251C'  # ├

barre = Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '\u2502' + Fore.RESET + Style.RESET_ALL  # │ colorée en magenta et bold
tiret = '\u2500'  # ─

# ┌───┬───┬───┐ :
premiere_ligne = Style.BRIGHT + Fore.CYAN + coin_haut_gauche + tiret + tiret + tiret + croisement_haut + tiret + tiret + tiret + croisement_haut + tiret + tiret + tiret + coin_haut_droit + Fore.RESET + Style.RESET_ALL
# ├───┼───┼───┤ :
milieu_ligne = Style.BRIGHT + Fore.CYAN + croisement_gauche + tiret + tiret + tiret + croisement_milieu + tiret + tiret + tiret + croisement_milieu + tiret + tiret + tiret + croisement_droit + Fore.RESET + Style.RESET_ALL
# └───┴───┴───┘ :
derniere_ligne = Style.BRIGHT + Fore.CYAN + coin_bas_gauche + tiret + tiret + tiret + croisement_bas + tiret + tiret + tiret + croisement_bas + tiret + tiret + tiret + coin_bas_droit + Fore.RESET + Style.RESET_ALL


# Définissons une fonction pour dessiner un taquin donné
def dessiner_taquin(matrice) :
    print(premiere_ligne)
    for ligne in range(3) :
        for col in matrice[ligne] :
            if col == 0 :
                print(barre, Back.LIGHTBLUE_EX + ' ' + Back.RESET, end=' ')
            else :
                print(barre, col, end=' ')
        print(barre)
        if ligne == 2 :
            print(derniere_ligne)
        else :
            print(milieu_ligne)


if __name__ == '__main__' :
# condition pour empecher l'exécution de cette partie de code, en dehors de ce module 'Main.py'

    branche = main([[1, 2, 3], [4, 5, 0], [6, 7, 8]])

    etapes=len(branche)-1

    # Affichage dans le terminal
    print('coût total (steps) : ',etapes ,end='\n')
    print(tiret + tiret + croisement_droit, "Taquin Entré", croisement_gauche + tiret + tiret)
    for noeud in branche :
        if noeud['operation'] != '' :
            letter = 'avant opération'
            if noeud['operation'] == 'U' :
                letter = 'En Haut'
            elif noeud['operation'] == 'R' :
                letter = "À Droite"
            elif noeud['operation'] == 'L' :
                letter = 'À Gauche'
            elif noeud['operation'] == 'D' :
                letter = 'Vers le Bas'
            print(tiret + tiret + croisement_droit, letter, croisement_gauche + tiret + tiret)
        dessiner_taquin(noeud['taquin'])
        print()

    print(tiret + tiret + croisement_droit, 'FIN Recherche A* avec {} étapes'.format(etapes), croisement_gauche + tiret + tiret)
    # Fin Affichage terminal.

    #Tkinter graphic interface
    window = tk.Tk()
    window['bg']='white'
    window.title (' Taquin resolution IA')
    can=tk.Canvas( width=500,height=500,bg='white')
    can.pack( side =tk.TOP, padx =20, pady =20)
    # fenetre['bg']='white'
    # fenetre.title (' Taquin resolution IA')

    window.mainloop()
    #Fin Tkinter graphic interface.
