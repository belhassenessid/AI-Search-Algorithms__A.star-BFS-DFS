import A_star_algo
import BFS
import tkinter  as tk
from random import shuffle
from time import sleep
from colorama import Fore, Back, Style  # Fore et Back pour colorer l'écriture et son font, Style à son style

# Une mainWindow est définie dans le programme principal, elle affiche l'entrée par défaut [0..8] qui peut
# être mélangée avec le bouton (Mélanger), puis vous choisissez l'algorithme de recherche à appliquer, vous cliquez sur
# (DFS), (BFS) ou (A*) en suite la fonction appropriée sera appelée pour créer une nouvelle fenêtre dans laquelle nous
# avons d'abord l'entrée par défaut ou melangé, et un bouton (suivant) pour afficher le nœud suivant (en affichant le
# numéro du nœud et le nombre de déplacements n)

global n,branche,etapes,Nbr_total_noeuds_explores


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
    for i in range(9) :
        ListeT = list(i for j in input_defaut for i in j)
        ligne, col = i // 3, i % 3
        can.create_image(30 + 200 * col, 30 + 200 * ligne, anchor=tk.NW, image=img[ListeT[i]])

def next():
    global n
    n+=1

    for i in range(9) :
        if n>etapes:
            break
        else:
            ListeT = list(i for j in branche[n]['taquin'] for i in j)
            ligne, col = i // 3, i % 3
            if n==etapes:
                texte.delete("1.0", tk.END)
                texte.insert(tk.END,"FIN, C'est le dernier nœud BUT {}/{} du chemin-solution ||\n{}+1 total de nœuds explorés à la fin de l'exécution".format(n,etapes,Nbr_total_noeuds_explores))
                texte.pack(side=tk.LEFT)
            else:
                texte.delete("1.0", tk.END)
                texte.insert(tk.END,"C'est le nœud {}/{} du chemin-solution ||\n{}+1 nœuds à explorer au total pour arriver au but".format(n,etapes,Nbr_total_noeuds_explores))
                texte.pack(side=tk.LEFT)
            can2.create_image(30 + 200 * col, 30 + 200 * ligne, anchor=tk.NW, image=img[ListeT[i]])


def solve_A_star():
    global branche,etapes,img,can2,texte,n,Nbr_total_noeuds_explores
    n=0
    branche,Nbr_total_noeuds_explores = A_star_algo.main(input_defaut)
    etapes = len(branche) - 1
    # Affichage dans le terminal
    print('Chemin-solution de {} noeuds',etapes+1 ,end='\n')
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

    print(tiret + tiret + croisement_droit, 'FIN Rech A* | {}+1 noeuds explorés en total | chemin-solution ci-dessus'.format(Nbr_total_noeuds_explores-1),
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
    tk.Button(text='-Nœud-solution suivant->',font=("Courier New",11),relief=tk.FLAT,command=next).pack(side=tk.RIGHT)
    texte=tk.Text(font=("Courier New", 11),width=51,height=3)
    texte.insert(tk.END, "C'est le nœud initial 1/{} du chemin-solution ||\n{}+1 nœuds à explorer au total pour arriver au but".format(etapes,Nbr_total_noeuds_explores))
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

input_defaut = [[1, 2, 3],
                    [8, 6, 0],
                    [7, 5, 4]]

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
