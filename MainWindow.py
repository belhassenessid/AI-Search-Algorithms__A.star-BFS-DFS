from A_star_algo import main
import tkinter  as tk
from random import shuffle
from time import sleep
from colorama import Fore, Back, Style  # Fore et Back pour colorer l'écriture et son font, Style à son style

global n,branche,etapes


# Définissons les éléments de décoration graphiques dans le Terminal (couleurs, styles, formes et matrices) :
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


# Définissons une fonction pour dessiner un taquin donné dans le terminal
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
# FIN éléments de décoration graphiques dans le Terminal.

def melanger():
    global input_defaut
    L = list(i for j in input_defaut for i in j)
    shuffle(L)
    input_defaut= [[L[0],L[1],L[2]],[L[3],L[4],L[5]],[L[6],L[7],L[8]]]
    print(input_defaut,type(L[0]))
    for i in range(9) :
        ListeT = list(i for j in input_defaut for i in j)
        ligne, col = i // 3, i % 3
        can.create_image(30 + 200 * col, 30 + 200 * ligne, anchor=tk.NW, image=img[ListeT[i]])

def next():
    global n
    n+=1

    for i in range(9) :
        ListeT = list(i for j in branche[n]['taquin'] for i in j)
        ligne, col = i // 3, i % 3
        texte.delete("1.0", tk.END)
        texte.insert(tk.END, "Nœud{}/{}, {} déplacement effectué parmis {}".format(n+1,etapes+1,n,etapes))
        texte.pack(side=tk.LEFT)
        can2.create_image(30 + 200 * col, 30 + 200 * ligne, anchor=tk.NW, image=img[ListeT[i]])


def solve_A_star():
    global branche
    global etapes
    global n
    global img
    global can2
    global texte
    n=0
    branche = main(input_defaut)
    etapes = len(branche) - 1
    # Affichage dans le terminal
    print('coût total (steps) : ', etapes, end='\n')
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

    print(tiret + tiret + croisement_droit, 'FIN Recherche A* avec {} étapes'.format(etapes),
          croisement_gauche + tiret + tiret)
    # Fin Affichage terminal.
    mainWindow.destroy()
    # créer la fenetre
    AstarWindow = tk.Tk()
    AstarWindow['bg'] = 'black'
    AstarWindow.title('IA - Algo A*')
    AstarWindow.geometry("700x700+300+0")
    # créer une zone Canvas destinée à placer les images des cases
    can2 = tk.Canvas(height=600, width=600, bg='black')
    can2.pack(side=tk.BOTTOM)
    can2.pack()
    # importer les images dans une liste d'objets tkinter.PhotoImage
    img = []
    for i in range(9) :
        img.append(tk.PhotoImage(file="./img/" + str(i) + ".png"))
    #Noeud && next
    tk.Button(text='-Nœud suivant->',font=("Courier New",11),relief=tk.FLAT,command=next).pack(side=tk.RIGHT)
    texte=tk.Text(font=("Courier New", 11),width=45,height=1)
    texte.insert(tk.END, "Nœud1 initial, 0 déplacement")
    texte.pack(side=tk.LEFT)
    for i in range(9) :
        ListeT = list(i for j in branche[0]['taquin'] for i in j)
        ligne, col = i // 3, i % 3
        can2.create_image(30 + 200 * col, 30 + 200 * ligne, anchor=tk.NW, image=img[ListeT[i]])

    AstarWindow.mainloop()

#main main main

#Tkinter graphic interface
#créer la fenetre
mainWindow = tk.Tk()
mainWindow['bg']= 'black'
mainWindow.title ('IA - jeu de taquin')
mainWindow.geometry("700x700+300+0")

#créer une zone Canvas destinée à placer les images des cases
can=tk.Canvas(height=600, width=600, bg='black')
can.pack(side =tk.BOTTOM)

#importer les images dans une liste d'objets tkinter.PhotoImage
img=[]
for i in range(9):
        img.append(tk.PhotoImage(file="./img/"+str(i)+".png"))

#Initialisation de la zone Canvas, placer les images de l'input par defaut dans la zone Canvas

input_defaut = [[0, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]]

for i in range(9) :
    ListeT = list(i for j in input_defaut for i in j)
    ligne, col = i // 3, i % 3
    afficher = can.create_image(30 + 200 * col, 30 + 200 * ligne, anchor=tk.NW, image=img[ListeT[i]])

#Menu des Commandes résoudre et mélanger

menu = tk.Menu(mainWindow)
menu.add_command(label="Mélanger", command=melanger)
menu.add_command(label="Résolution DFS", command=None)
menu.add_command(label="Résolution BFS", command=None)
menu.add_command(label="Résolution A*", command=solve_A_star)
mainWindow.config(menu=menu)

mainWindow.mainloop()
#Fin Tkinter graphic interface.
