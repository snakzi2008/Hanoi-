#c'est celui la qu'il faut lancer de base car il contient main 



from hanoi_moteur import * # le moteur
import tkinter as tk # la fenetre ( c'est pour fen )
from tkinter import messagebox, simpledialog # pour fair les pop-up 

class TourDeHanoi:
    def __init__(self, nb_disques, canvas):
        """
        Initialise le jeu de la Tour de Hanoi avec le nombre de disques spécifié.
        /

        """
        self.nb_disques = nb_disques
        assert nb_disques < 15 ," le nombre de disque est trop gros pour l'affichage graphique " # bloque le nombre de disque
        # la résolution est fonctionelle mais trop longue; et compliquer a mettre en place graphiquement
        assert nb_disques >= 1, " le nombre de disque doit être positif "
        if nb_disques > 9 :
            messagebox.showinfo("Information", "tu as choisi un nombre de disque trop grand\nça va prendre beaucoup de temps et ça vas depasser de l'affichage de l'ecran. ")
            pass # on continue car le max sera 16 
        self.tours = [Pilas() for _ in range(3)]
        self.canvas = canvas
        self.disque_ids = [None] * nb_disques
        self.couleurs = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]
        self.lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(nb_disques,0, -1):
            self.tours[0].empiler(i)
        self.dessiner_tours()

    def dessiner_tours(self):
        """
        Dessine les tours et la base du jeu sur le canvas.
        étape 1
        Supprime tous les dessins existants sur le canvas avant de commencer.
        étape 2
        Définit les dimensions des tours et de la base :
        - Les tours ont une largeur et une hauteur fixes.
        - La base a une hauteur fixe.
        étape 3
        Itère pour dessiner trois tours positionnées  sur le canvas :
        - Chaque tour est représentée par un rectangle noir.
        - Les positions des tours sont calculées en fonction de leurs index

        Dessine la base des tours comme un rectangle noir s'étendant horizontalement à travers le canvas.
        etape 4
        Appelle la méthode pour dessiner les disques sur le canvas après avoir créé les tours et la base.

        /
        """
        self.canvas.delete("all")
        largeur_tour = 20 ; hauteur_tour = 300 # ça c'est pour les tours
        hauteur_base = 20  # et ça la base
        for i in range(3): # creation des tours
            x = 150 + i * 200
            self.canvas.create_rectangle(x - largeur_tour // 2, 300 - hauteur_tour, x + largeur_tour // 2, 300,
                                         fill="black")
        self.canvas.create_rectangle(50, 300, 650, 300 + hauteur_base, fill="black")
        self.dessiner_disques()

    def dessiner_disques(self):
        """
        Dessine les disques sur les tours.
        /
        """
        for i in range(3): # ici on dessine les disques sur les tours 
            courant = self.tours[i].tete 
            disques = [] 
            while courant: 
                disques.append(courant.donnee) # on ajoute les disques dans la liste disques 
                courant = courant.suivant # on passe au suivant
            y = 300 - 20 # on commence a 300 et on descend de 20 a chaque fois 
            for donnee in reversed(disques): # on dessine les disques en commencant par le plus grand avec reversed 
                largeur_disque = 20 + donnee * 20 
                x = 150 + i * 200
                couleur = self.couleurs[(donnee - 1) % len(self.couleurs)]
                lettre = self.lettres[(donnee - 1) % len(self.lettres)]
                self.disque_ids[donnee - 1] = self.canvas.create_rectangle(x - largeur_disque // 2, y - 20, x + largeur_disque // 2, y, fill=couleur)
                self.canvas.create_text(x, y - 10, text=lettre, fill="white")
                y -= 20

    def deplacer_disque(self, de_tour, a_tour):
        """
        Déplace un disque d'une tour à une autre.
        /
        """
        disque = self.tours[de_tour].depiler() # on depile le disque de la tour de depart
        if disque is not None: 
            self.tours[a_tour].empiler(disque)
            self.dessiner_tours()

    def resoudre(self, n, de_tour, a_tour, tour_aux):
        """
        Résout le problème de la Tour de Hanoi pour n disques.
        /
        """
        if n == 1:
            self.deplacer_disque(de_tour, a_tour)
            self.mettre_a_jour_gui()
            return
        # sinon on fait la meme chose mais en deplacant "n-1 disques"  de la tour de depart a la tour aux 
        self.resoudre(n-1, de_tour, tour_aux, a_tour)
        self.deplacer_disque(de_tour, a_tour)
        self.mettre_a_jour_gui()
        self.resoudre(n-1, tour_aux, a_tour, de_tour)

    def mettre_a_jour_gui(self):
        """
        Met à jour l'interface graphique.
        
        /
        """
        self.canvas.update()
        self.canvas.after(500)

def main():
    """
    fonction principale du programme c'est celle la qui va tout lancer la demande et qui va ordonné la resolution du jeu 
    on crée la fenetre " fen 
    on demande les disque seulement des int() ( et il y a une assertion dans la partie moteur si c'est negatif ou == 0 car sinon tout est convers par le askinteger  ) et on donne le nombre d'operation attendu 
    
     
     """
    fen = tk.Tk() 
    fen.title("les 3 tours de Hanoi")
    canvas = tk.Canvas(fen, width=700, height=400)
    canvas.pack()
    #photo_hanoi = tk.PhotoImage(file="Hanoi.png")
    #fen.iconphoto(False, photo_hanoi) # pour l'instant j'y arrive pas 

    nb_disques = simpledialog.askinteger("Input pour la résolution :", "combien de disque tu veux :")
    if nb_disques is None: #si y'a pas de disque ya pas de suite donc c'est ciao 
        return

    nb_operations = 2**nb_disques - 1 # Le probleme de ce jeu ce resoud avec cette suite de math et on la calucl pour l'afficher 
    messagebox.showinfo("Information", f" ça va faire : {nb_operations} operations pour finir avec ce nombre de disques.") # et la on l'affiche 

    hanoi = TourDeHanoi(nb_disques, canvas)
    hanoi.resoudre(nb_disques, 0, 2, 1)
    fen.mainloop()

if __name__ == "__main__":
    test_pile()
    main()
