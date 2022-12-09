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

def est_une_intersection(clicCoord:tuple) :
    x,y = clicCoord

    for i in range(len(Intersections)) :
        for j in range(len(Intersections[i])) :
            coord = Intersections[i][j]
            distance = (coord[0]-x)**2 + (coord[1]-y)**2
            if distance < 15**2 :
                return [coord, (i,j)]

    return 0

fltk.cree_fenetre(WEIGHT, HEIGHT)


fltk.rectangle(300, 100, 1200, 850, epaisseur=3, remplissage="#FFE0A9")
fltk.rectangle(435, 210, 1070, 740, epaisseur=3)
fltk.rectangle(555, 310, 950, 640, epaisseur=3)

fltk.ligne(750, 100, 750, 310, epaisseur=3)
fltk.ligne(750, 640, 750, 850, epaisseur=3)

fltk.ligne(300, 475, 555, 475, epaisseur=3)
fltk.ligne(950, 475, 1200, 475, epaisseur=3)


jetonsJ1 = list()
jetonsJ2 = list()

for _ in range(9) :
    jeton = Jeton(15, (1381, 467), "b", "blue")
    jetonsJ1.append(jeton)

    jeton = Jeton(15, (100, 475), "b", "green")
    jetonsJ2.append(jeton)

grille = plateau.Plateau(1)

j1 = joueur.Joueur(grille, "b")
j2 = joueur.Joueur(grille, "g")

who = True

while True :

    coordClic = fltk.attend_clic_gauche()


    intersec = est_une_intersection(coordClic)


    if intersec != 0 :

        if who :
            jeton = jetonsJ1.pop()
            jeton.deplace(intersec[0])

            j1.joue(intersec[1])

        else :
            
            jeton = jetonsJ2.pop()
            jeton.deplace(intersec[0])

            j2.joue(intersec[1])


        who = not who

    win = grille.Moulin()

    if win[0] != "Null" :
        print(win)



    fltk.mise_a_jour()


