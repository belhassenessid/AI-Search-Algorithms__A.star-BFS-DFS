from Algorithms import A_star_algo, BFS_algo, DFS_algo
from Algorithms.A_star_algo import etat_final
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
        can.create_image(30 + 110 * col, 30 + 110 * ligne, anchor=tk.NW, image=img[ListeT[i]])

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
                texte.insert(tk.END,"FIN! Voilà le dernier nœud {}/{} BUT (Vous trouvez les détails\ndans le fichier {}_OutPut.txt)".format(n+1, etapes_solution+1,algorith))
                texte['fg']='green'
                texte.pack()
            else:
                texte.delete("1.0", tk.END)
                texte.insert(tk.END,"Ci-dessous est le nœud {}/{} du chemin_solution".format(n+1, etapes_solution+1, Nbr_total_noeuds_explores))
                texte.pack()
            can2.create_image(30 + 110 * col, 30 + 110 * ligne, anchor=tk.NW, image=img[ListeT[i]])
def DFS():
    solve('DFS')
def BFS():
    solve('BFS')
def A_star():
    solve('A_star')

def solve(algo):
    global branche_solution, etapes_solution, img, can2, texte, n, Nbr_total_noeuds_explores,algorith
    n=0
    algorith=algo
    if algo=='A_star':
        branche_solution, Nbr_total_noeuds_explores, temps = A_star_algo.main(input_defaut)
    elif algo=='BFS':
        branche_solution, Nbr_total_noeuds_explores, temps = BFS_algo.main(input_defaut)
    elif algo=='DFS':
        branche_solution,Nbr_total_noeuds_explores, temps=DFS_algo.main(input_defaut)


    etapes_solution = len(branche_solution) - 1

    # Affichage dans le terminal
    print("chemin-solution vers le BUT: se trouve dans un fichier .txt cree apres cette execution && vous pouvez parcourir ce chemin dans l'interface graphique")
    print("cout du chemin-solution (steps): {}".format(etapes_solution))
    print("total de noeuds explores/developpes a la fin de l'execution: {} noeuds +1 noeud-initial".format(Nbr_total_noeuds_explores-1))
    print("temps d'execution: {}".format(temps))
    # FIN affichage dans le terminal

    # Générer un fichier de sortie pour la comparaison
    file = open(algo+'_OutPut.txt', 'a')
    file.write("Chemin-solution: input-> "+str(branche_solution)+" <-BUT\n\n")
    file.write("cout du chemin-solution (steps): "+str(etapes_solution)+"\n")
    file.write("total de noeuds explores/developpes a la fin de l'execution: "+str(Nbr_total_noeuds_explores)+"\n")
    file.write("temps d'execution: "+temps+"\n\n")
    file.write("++++++++++++++++++"+"\n\n")
    file.close()
    # FIN fichier de sortie

    # Interface graphique
    mainWindow.destroy()
    # créer la fenetre
    AstarWindow = tk.Tk()
    AstarWindow['bg'] = 'white'
    AstarWindow.title('IA - Algo {}'.format(algo))
    AstarWindow.geometry("520x560-400-150")
    # créer une zone Canvas destinée à placer les images des cases
    can2 = tk.Canvas(height=380, width=380, bg='ghost white')
    can2.pack(side=tk.BOTTOM)
    can2.pack()
    # importer les images dans une liste d'objets tkinter.PhotoImage
    img = []
    for i in range(9) :
        img.append(tk.PhotoImage(file="../img/" + str(i) + ".png"))
    #Noeud && noeud_suivant

    tk.Label(text="Total des nœuds explorés à la fin de l'exécution: {} noeuds +1 noeud-initial\nCoût du chemin-solution(steps): {}\nTemps d'exécution: {}".format(
                     Nbr_total_noeuds_explores-1,etapes_solution, temps),bg='white',width=70,height=5,font=("Arial",10,"bold")).pack()

    texte=tk.Text(font=("Arial", 10,"bold"),fg='black',bg='white',border=1,padx=10,width=60,height=3)
    texte.insert(tk.END, "Ci-dessous est le neud initial.\nParcourez le chemin-solution en cliquant sur le bouton\n'Nœud suivant' (il se trouve aussi dans un fichier {}_OutPut.txt)".format(algo))
    texte.pack()
    tk.Button(text='Nœud suivant', font=("Arial", 11), fg='black',bg='ghost white', relief=tk.RAISED,
              command=noeud_suivant).pack()#light pink

    for i in range(9) :
        ListeT = list(i for j in branche_solution[0]['taquin'] for i in j)
        ligne, col = i // 3, i % 3
        can2.create_image(30 + 110 * col, 30 + 110 * ligne, anchor=tk.NW, image=img[ListeT[i]])

    AstarWindow.mainloop()
    # FIN Interface graphique

#MAIN WINDOW
#Tkinter graphic interface
#créer la fenetre
mainWindow = tk.Tk()
mainWindow['bg']= 'white'
mainWindow.title ('IA - jeu de taquin')
mainWindow.geometry("440x500-400-150")
tk.Label(text="Choisissez l'algorithme pour résoudre dans le menu ci-dessus.\nVous pouvez également mélanger le puzzle.",bg='white',width=50,height=5,font=("Arial",10,"bold")).pack(side=tk.TOP)

#créer une zone Canvas destinée à placer les images des cases
can=tk.Canvas(height=380, width=380, bg='ghost white')
can.pack(side =tk.TOP)

#importer les images dans une liste d'objets tkinter.PhotoImage
img=[]
for i in range(9):
        img.append(tk.PhotoImage(file="../img/"+str(i)+".png"))

#Initialisation de la zone Canvas, placer les images de l'input par defaut dans la zone Canvas

input_defaut = [[1, 2, 3],
                [8, 6, 0],
                [7, 5, 4]]



for i in range(9) :
    ListeT = list(i for j in input_defaut for i in j)
    ligne, col = i // 3, i % 3
    afficher = can.create_image(30 + 110 * col, 30 + 110 * ligne, anchor=tk.NW, image=img[ListeT[i]])

#Menu des Commandes résoudre et mélanger

menu = tk.Menu(mainWindow)
menu.add_command(label="Mélanger", command=melanger)
menu.add_command(label="Résolution DFS", command=DFS)
menu.add_command(label="Résolution BFS", command=BFS)
menu.add_command(label="Résolution A*", command=A_star)
mainWindow.config(menu=menu)

mainWindow.mainloop()
#Fin Tkinter graphic interface.
