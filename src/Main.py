from tkinter import *


class Interface(Frame):
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=1000, height=1000, **kwargs)
        fenetre.geometry("800x400") #You want the size of the app to be 500x500
        fenetre.resizable(0, 0) #Don't allow resizing in the x or y direction
        self.pack(fill=BOTH)
        self.nb_clic = 0

        # Création de nos widgets
        self.message = Label(self,
                             text="Bienvenue sur le jeu des bâtonnets !\n Choisissez une option : ",padx=12)
        self.message.pack()

        self.GameswithIAstandard = Button(self, text="Jouer contre l'IA", command=self.quit)
        self.GameswithIAstandard.pack(padx =3, pady =5)
        self.GameswithIA = Button(self, text="Jouer contre l'IA avec un nombre de baton de votre choix", command=self.quit)
        self.GameswithIA.pack(padx=3, pady=5)
        self.GameswithOtherpersonstandard = Button(self, text="Jouer à deux", command=self.quit)
        self.GameswithOtherpersonstandard.pack(padx =3, pady =5)
        self.GameswithOtherperson = Button(self, text="Jouer à deux avec un nombre de baton de votre choix", command=self.quit)
        self.GameswithOtherperson.pack(padx =3, pady =5)


        self.bouton_cliquer = Button(self, text="Règles du jeu",
                                     command=self.regles, padx=3, pady=5)
        self.bouton_cliquer.pack()


    def regles(self):
        self.message[
            "text"] = "Un nombre de bâtonnets en bois sont alignés les uns à côté des autres au centre de la table. \n A tour de rôle chacun des 2 concurrents va devoir en retirer 1, 2 ou 3 à l'endroit de leur choix, \n le but étant de laisser le dernier bâtonnet à son adversaire."

    def getnbBaton(self,nbBat):
        Bat = list(map(lambda x: x * nbBat, "|"))
        self.message["text"] = Bat

fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
