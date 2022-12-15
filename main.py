import fltk

import plateau
import joueur

from config import WEIGHT, HEIGHT
from config import IntersectionsPlateau1 as Intersections


def est_une_intersection(clicCoord:tuple) -> list:
    x,y = clicCoord

    for i in range(len(Intersections)) :
        for j in range(len(Intersections[i])) :
            coord = Intersections[i][j]
            distance = (coord[0]-x)**2 + (coord[1]-y)**2
            if distance < 15**2 :
                return [coord, (i,j)]

    return [0]*2


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
        fltk.cercle(coord[0], coord[1],10, remplissage="black")


jetonsJ1 = list()
jetonsJ2 = list()

for _ in range(3) :
    jeton = joueur.Jeton(15, (1381, 467), "blue")
    jetonsJ1.append(jeton)

    jeton = joueur.Jeton(15, (100, 475), "green")
    jetonsJ2.append(jeton)

grille = plateau.Plateau(1)

j1 = joueur.Joueur(grille, 1)
j2 = joueur.Joueur(grille, 2)

who = True
phase = 1
estMoulin = False

while True :

    if phase == 1 and not estMoulin:

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

    if phase == 2 and not estMoulin:
        coordClic1= fltk.attend_clic_gauche()
        coordClic2 = fltk.attend_clic_gauche()

        intersec1 = est_une_intersection(coordClic1)
        indice1 = intersec1[1]

        intersec2 = est_une_intersection(coordClic2)
        indice2 = intersec2[1]
        
        estAdjacent = grille.est_un_voisin(indice1, indice2)

        if intersec1[0] != 0 and intersec2[0] != 0 and estAdjacent:

            if who :
                if grille.est_ce_joueur(indice1, j1.numero) and grille.EstJouable(indice2):
                    jeton = j1.donne_jeton(indice1)
                    grille.enleve(indice1)
                    j1.joue(indice2)
                    jeton.deplace(intersec2[0])
                    j1.ajoute_jeton(indice2, jeton)
                    who = not who

            else :
                if grille.est_ce_joueur(indice1, j2.numero) and grille.EstJouable(indice2):
                    jeton = j2.donne_jeton(indice1)
                    grille.enleve(indice1)
                    j2.joue(indice2)
                    jeton.deplace(intersec2[0])
                    j2.ajoute_jeton(indice2, jeton)
                    who = not who


    win = grille.Moulin()

    if win[0] != "Null" :
        _joueur = win[0]
        grille.dejavu(win[1], _joueur)
        estMoulin = True

    if estMoulin :
        coordClic = fltk.attend_clic_gauche()
        intersec = est_une_intersection(coordClic)

        if intersec[0] != 0 :
            indice = intersec[1]

            if _joueur == 1 :
                if grille.est_ce_joueur(indice, 2) :
                    j2.donne_jeton(indice).efface()
                    grille.enleve(indice)
                    estMoulin = False
            
            if _joueur == 2 :
                 if grille.est_ce_joueur(indice, 1) :
                    j1.donne_jeton(indice).efface()
                    grille.enleve(indice)
                    estMoulin = False
            
            grille.affiche()
            
    fltk.mise_a_jour()