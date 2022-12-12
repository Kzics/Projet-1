import fltk

from config import WEIGHT, HEIGHT
from config import IntersectionsPlateau1 as Intersections

import plateau
import joueur


class Jeton :
    def __init__(self, rayon:int, coord:tuple, joueur:str, couleur:str) -> None:
        self.couleur = couleur
        self.rayon = rayon
        self.x, self.y = coord
        self.joueur = joueur

        self.fltkobj = fltk.cercle(self.x, self.y, self.rayon, remplissage=self.couleur)
    
    def rafraichir(self) :
        fltk.efface(self.fltkobj)
        self.fltkobj = fltk.cercle(self.x, self.y, self.rayon, remplissage=self.couleur)

    def deplace(self, coord:tuple) :
        self.x, self.y = coord
        self.rafraichir()

def est_une_intersection(clicCoord:tuple) -> list:
    x,y = clicCoord

    for i in range(len(Intersections)) :
        for j in range(len(Intersections[i])) :
            coord = Intersections[i][j]
            distance = (coord[0]-x)**2 + (coord[1]-y)**2
            if distance < 15**2 :
                return [coord, (i,j)]

    return [0]*2

moulinDic = {}

fltk.cree_fenetre(WEIGHT, HEIGHT)


fltk.rectangle(300, 100, 1200, 850, epaisseur=3, remplissage="#FFE0A9")
fltk.rectangle(435, 210, 1070, 740, epaisseur=3)
fltk.rectangle(555, 310, 950, 640, epaisseur=3)

fltk.ligne(750, 100, 750, 310, epaisseur=3)
fltk.ligne(750, 640, 750, 850, epaisseur=3)

fltk.ligne(300, 475, 555, 475, epaisseur=3)
fltk.ligne(950, 475, 1200, 475, epaisseur=3)

#creation des cercles dans les intersections
for i in Intersections:
    for coord in i :
        fltk.cercle(1200, 100, 10, remplissage="black")


jetonsJ1 = list()
jetonsJ2 = list()

for _ in range(9) :
    jeton = Jeton(15, (1381, 467), "b", "blue")
    jetonsJ1.append(jeton)

    jeton = Jeton(15, (100, 475), "g", "green")
    jetonsJ2.append(jeton)

grille = plateau.Plateau(1)

j1 = joueur.Joueur(grille, "b")
j2 = joueur.Joueur(grille, "g")

who = True
phase = 1


def checkTurn():
    return "g" if not who else "b"

while True :


    if phase == 1 :

        coordClic = fltk.attend_clic_gauche()
        intersec = est_une_intersection(coordClic)
        indice = intersec[1] #indice i,j de grille

        if intersec[0] != 0 and grille.EstJouable(indice):

            if who :
                jeton = jetonsJ1.pop()

                j1.joue(intersec[1])
                jeton.deplace(intersec[0])
                j1.ajoute_jeton(indice, jeton)

            else :
                
                jeton = jetonsJ2.pop()

                j2.joue(intersec[1])
                jeton.deplace(intersec[0])
                j2.ajoute_jeton(indice, jeton)

            who = not who

            if len(jetonsJ2) == 0 : 
                phase = 2

    if phase == 2 :
        coordClic1= fltk.attend_clic_gauche()
        coordClic2 = fltk.attend_clic_gauche()

        intersec1 = est_une_intersection(coordClic1)
        indice1 = intersec1[1]

        intersec2 = est_une_intersection(coordClic2)
        indice2 = intersec2[1]
        
        estAdjacent = grille.est_un_voisin(indice1, indice2)

        if intersec1[0] != 0 and intersec2[0] != 0 and estAdjacent:

            if who :
                if grille.est_ce_joueur(indice1, j1.couleur) and grille.EstJouable(indice2):
                    jeton = j1.donne_jeton(indice1)
                    grille.enleve(indice1)
                    j1.joue(indice2)
                    jeton.deplace(intersec2[0])
                    j1.ajoute_jeton(indice2, jeton)
                    who = not who

            else :
                if grille.est_ce_joueur(indice1, j2.couleur) and grille.EstJouable(indice2):
                    jeton = j2.donne_jeton(indice1)
                    grille.enleve(indice1)
                    j2.joue(indice2)
                    jeton.deplace(intersec2[0])
                    j2.ajoute_jeton(indice2, jeton)
                    who = not who

    win = grille.Moulin()


    if win[0] != "Null" and moulinDic.get(win[0]) == "Null":
       moulinDic[win[0]] = win[1]

    
    if len(jetonsJ2) == 0 :
        pass

    fltk.mise_a_jour()


