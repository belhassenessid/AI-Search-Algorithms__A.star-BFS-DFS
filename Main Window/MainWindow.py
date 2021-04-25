from Algorithms import A_star_algo, BFS_algo, DFS_algo
import tkinter  as tk
from random import shuffle

# Une mainWindow est définie dans le programme principal, elle affiche l'entrée par défaut [0..8] qui peut
# être mélangée avec le bouton (Mélanger), puis vous choisissez l'algorithme de recherche à appliquer, vous cliquez sur
# (DFS), (BFS) ou (A*) en suite la fonction appropriée sera appelée pour créer une nouvelle fenêtre dans laquelle nous
# avons d'abord l'entrée par défaut ou melangé, et un bouton (suivant) pour afficher le nœud suivant (en affichant le
# numéro du nœud et le nombre de déplacements n)

global n, branche_solution, etapes_solution, Nbr_total_noeuds_explores, temps

def melanger():
    global input_defaut
    L = list(i for j in input_defaut for i in j)
    shuffle(L)
    input_defaut= [[L[0],L[1],L[2]],[L[3],L[4],L[5]],[L[6],L[7],L[8]]]
    for i in range(9) :
        ListeT = list(i for j in input_defaut for i in j)
        ligne, col = i // 3, i % 3
        can.create_image(30 + 200 * col, 30 + 200 * ligne, anchor=tk.NW, image=img[ListeT[i]])

def noeud_suivant():
    global n
    n+=1

    for i in range(9) :
        if n>etapes_solution:
            break
        else:
            ListeT = list(i for j in branche_solution[n]['taquin'] for i in j)
            ligne, col = i // 3, i % 3
            if n==etapes_solution:
                texte.delete("1.0", tk.END)
                texte.insert(tk.END,"FIN, C'est le dernier nœud BUT {}/{} du chemin_solution ||\n{}+1 total de nœuds explorés à la fin de l'exécution".format(n, etapes_solution+1, Nbr_total_noeuds_explores))
                texte['fg']='green'
                texte.pack(side=tk.LEFT)
            else:
                texte.delete("1.0", tk.END)
                texte.insert(tk.END,"C'est le nœud {}/{} du chemin_solution ||\n{}+1 nœuds à explorer au total pour arriver au but".format(n, etapes_solution+1, Nbr_total_noeuds_explores))
                texte.pack(side=tk.LEFT)
            can2.create_image(30 + 200 * col, 30 + 200 * ligne, anchor=tk.NW, image=img[ListeT[i]])
def DFS():
    solve('DFS')
def BFS():
    solve('BFS')
def A_star():
    solve('A*')

def solve(algo):
    global branche_solution, etapes_solution, img, can2, texte, n, Nbr_total_noeuds_explores
    n=0
    if algo=='A*':
        branche_solution, Nbr_total_noeuds_explores, temps = A_star_algo.main(input_defaut)
    elif algo=='BFS':
        branche_solution, Nbr_total_noeuds_explores, temps = BFS_algo.main(input_defaut)
    elif algo=='DFS':
        branche_solution,Nbr_total_noeuds_explores, temps=DFS_algo.main(input_defaut)


    etapes_solution = len(branche_solution) - 1

    # Affichage dans le terminal
    print("chemin-solution vers le BUT: se trouve dans un fichier .txt cree apres cette execution && vous pouvez parcourir ce chemin dans l'interface graphique")
    print("cout du chemin-solution (steps): {}".format(etapes_solution))
    print("total de noeuds explores/developpes a la fin de l'execution: {}".format(Nbr_total_noeuds_explores))
    print("temps d'execution: {}".format(temps))
    # FIN affichage dans le terminal

    # Interface graphique
    mainWindow.destroy()
    # créer la fenetre
    AstarWindow = tk.Tk()
    AstarWindow['bg'] = 'black'
    AstarWindow.title('IA - Algo {}'.format(algo))
    AstarWindow.geometry("800x700+300+0")
    # créer une zone Canvas destinée à placer les images des cases
    can2 = tk.Canvas(height=600, width=600, bg='black')
    can2.pack(side=tk.BOTTOM)
    can2.pack()
    # importer les images dans une liste d'objets tkinter.PhotoImage
    img = []
    for i in range(9) :
        img.append(tk.PhotoImage(file="../img/" + str(i) + ".png"))
    #Noeud && noeud_suivant
    tk.Button(text='-Nœud-solution suivant->', font=("Courier New",11,'bold'), fg='green', relief=tk.FLAT, command=noeud_suivant).pack(side=tk.RIGHT)
    texte=tk.Text(font=("Courier New", 11),fg='white',bg='black',border=0,padx=10,width=60,height=3)
    texte.insert(tk.END, "C'est le nœud initial 1/{} du chemin_solution-solution ||\n{}+1 nœuds à explorer au total pour arriver au but".format(etapes_solution, Nbr_total_noeuds_explores))
    texte.pack(side=tk.LEFT)
    for i in range(9) :
        ListeT = list(i for j in branche_solution[0]['taquin'] for i in j)
        ligne, col = i // 3, i % 3
        can2.create_image(30 + 200 * col, 30 + 200 * ligne, anchor=tk.NW, image=img[ListeT[i]])

    AstarWindow.mainloop()
    # FIN Interface graphique

    # Générer un fichier de sortie pour la comparaison
    if algo == 'A*' :
        file = open('A_star_OutPut.txt', 'w')
    else :
        file = open(algo + '_OutPut.txt', 'w')
    file.write("chemin-solution vers le BUT: " + str(list(i['operation'] for i in branche_solution[1 : :])) + "\n")
    file.write("cout du chemin-solution (steps): " + str(etapes_solution) + "\n")
    file.write("total de noeuds explores/developpes a la fin de l'execution: " + str(Nbr_total_noeuds_explores) + "\n")
    file.write("temps d'execution: " + temps + "\n")
    file.close()
    # FIN fichier de sortie


#MAIN WINDOW
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
        img.append(tk.PhotoImage(file="../img/"+str(i)+".png"))

#Initialisation de la zone Canvas, placer les images de l'input par defaut dans la zone Canvas

input_defaut = [[8, 4, 2],
                [5, 6, 1],
                [3, 0, 7]]

for i in range(9) :
    ListeT = list(i for j in input_defaut for i in j)
    ligne, col = i // 3, i % 3
    afficher = can.create_image(30 + 200 * col, 30 + 200 * ligne, anchor=tk.NW, image=img[ListeT[i]])

#Menu des Commandes résoudre et mélanger

menu = tk.Menu(mainWindow)
menu.add_command(label="Mélanger", command=melanger)
menu.add_command(label="Résolution DFS", command=DFS)
menu.add_command(label="Résolution BFS", command=BFS)
menu.add_command(label="Résolution A*", command=A_star)
mainWindow.config(menu=menu)

mainWindow.mainloop()
#Fin Tkinter graphic interface.
