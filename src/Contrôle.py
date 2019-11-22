# import
from random import randint
# import de tkinter mais pas assez de temps
from tkinter import *


# Fonction de retours des regles
def regles():
    print(
        "20 bâtonnets en bois sont alignés les uns à côté des autres au centre de la table. \n"
        "A tour de rôle chacun des 2 concurrents va devoir en retirer 1, 2 ou 3 à l'endroit de leur choix, \n"
        "le but étant de laisser le dernier bâtonnet à son adversaire.")


# Fonction d'accueil de l'application
def accueil():
    print(
        "Bienvenue sur le jeu des bâtonnets !\n Choisissez une option : \n 1. Pour jouer "
        "contre l'IA  \n 2. Pour jouer contre l'IA avec un nombre de baton de votre choix \n "
        "3. Pour jouer à deux \n 4. Pour jouer à deux  avec un nombre de baton de votre choix \n "
        "5. Pour voir les règles du jeu")
    Choix = int(input("Votre choix ? "))
    if (Choix == 5):
        regles()
    elif (Choix == 1):
        NewGamesWithIA(20)
    elif (Choix == 2):
        nbbat = nbBaton()
        NewGamesWithIA(int(nbbat))
    elif (Choix == 3):
        NewGamesWith2Players(20)
    elif (Choix == 4):
        nbbat = nbBaton()
        NewGamesWith2Players(int(nbbat))
    else:
        print("Vous avez fait une mauvaise manipulation de l'application, merci de choisir entre 1 et 5")
        accueil()


# Impression nombre Baton sur plateaux
def getnbBaton(nbBat):
    Bat = list(map(lambda x: x * nbBat, "|"))
    print(Bat)


# Impression nombre Baton sur plateaux
def joueurTurn(nbtour):
    if nbtour % 2 == 0:
        return 1
    else:
        return 2


# Fonction de nouvelle parties à 2 joueurs
def NewGamesWith2Players(NbBaton):
    # Nombre de batonnets
    tour = 0
    countBaton = NbBaton
    while countBaton >= 1:
        getnbBaton(countBaton)
        print("[JOUEUR N°{}] Combien de bâtons prenez vous?".format(joueurTurn(tour)))
        nbbatgetbyplayer = int(input())
        if (nbbatgetbyplayer in range(1, 4)):
            countBaton -= nbbatgetbyplayer
            tour += 1
        else:
            print("Nombre invalide !")
    print("[JOUEUR {}] à perdu !".format(joueurTurn(tour - 1)))
    accueil()


# Fonction de nouvelle parties contre IA
def NewGamesWithIA(NbBaton):
    countBaton = NbBaton
    while countBaton >= 1:
        getnbBaton(countBaton)
        print("[JOUEUR] Combien de bâtons prenez vous?")
        nbbatgetbyplayer = int(input())
        if (nbbatgetbyplayer in range(1, 4)):
            countBaton -= nbbatgetbyplayer
            nbbatbyIA = IAPlay(countBaton)
            countBaton -= nbbatbyIA
        elif nbbatgetbyplayer > countBaton:
            print("Nombre invalide !")
        else:
            print("Nombre invalide !")
    nouvellePartie()


# Fonction Definition jeux de l'IA
def IAPlay(countBaton):
    if (countBaton > 13):
        nbbatbyIA = randint(1, 3)
        print("[IA] prend : {}".format(nbbatbyIA))
    elif (countBaton in range(10, 13)):
        nbbatbyIA = countBaton - 9
        print("[IA] prend : {}".format(nbbatbyIA))
    elif (countBaton in range(6, 9)):
        nbbatbyIA = countBaton - 5
        print("[IA] prend : {}".format(nbbatbyIA))
    elif (countBaton in range(2, 5)):
        nbbatbyIA = countBaton - 1
        print("[IA] prend : {}".format(nbbatbyIA))
    elif (countBaton == 17 or countBaton == 13 or countBaton == 9 or countBaton == 5):
        nbbatbyIA = randint(1, 3)
        print("[IA] prend : {}".format(nbbatbyIA))
    elif (countBaton == 1):
        nbbatbyIA = 1
        print("[IA] prend : {}".format(nbbatbyIA))
        print("[IA] à perdu !")
    elif (countBaton < 1):
        nbbatbyIA = 0
        print("[Joueur] à perdu !")
    return nbbatbyIA


# lancemet de nouvelle partie
def nouvellePartie():
    print("Appuyez sur une touche pour recommencer")
    input()
    accueil()


# retour nombre de baton en graphique
def getnbBaton(nbBat):
    Bat = list(map(lambda x: x * nbBat, "|"))
    print(Bat)
    print(nbBat)


# def nombre baton
def nbBaton():
    print("Combien de bâtons voulez-vous dans la partie ? : ")
    nbbat = input()
    return nbbat


# Main
class Interface(Frame):
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""


fenetre = Tk()

accueil()
