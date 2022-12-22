import fltk

import joueur
import interface
import config

from plateau import creerPlateau


def est_une_intersection(clicCoord:tuple) -> list:
    x,y = clicCoord

    for i in range(len(Intersections_)) :
        for j in range(len(Intersections_[i])) :
            coord = Intersections_[i][j]
            distance = (coord[0]-x)**2 + (coord[1]-y)**2
            if distance < 17**2 :
                return [coord, (i,j)]

    return [0]*2


def Phase1() :
    global who, phase

    coordClic = fltk.attend_clic_gauche()
    intersection = est_une_intersection(coordClic)
    coordFenetre, indiceGrille = intersection

    if coordFenetre != 0 and grille.EstJouable(indiceGrille):

        if who :
            jeton = jetonsJ1.pop()

            j1.joue(indiceGrille)
            jeton.deplace(coordFenetre)
            j1.ajoute_jeton(indiceGrille, jeton)

        else :
            
            jeton = jetonsJ2.pop()

            j2.joue(indiceGrille)
            jeton.deplace(coordFenetre)
            j2.ajoute_jeton(indiceGrille, jeton)

        who = not who

        if len(jetonsJ2) == 0 : 
            phase = 2
        
        return indiceGrille

    return 0

def Phase2() :
    global who

    coordClic1 = fltk.attend_clic_gauche()
    intersection = est_une_intersection(coordClic1)
    coordFenetre, indiceGrille = intersection

    coordClic2 = fltk.attend_clic_gauche()
    intersection2 = est_une_intersection(coordClic2)
    indice2 = intersection2[1]

    if who :
        if j1.estMaster : 
            estUnVoisin = True
        else :
            estUnVoisin = grille.est_un_voisin(indiceGrille, indice2)

    else :
        if j2.estMaster : 
            estUnVoisin = True
        else :
            estUnVoisin = grille.est_un_voisin(indiceGrille, indice2)
    

    if coordFenetre != 0 and intersection2[0] != 0 and estUnVoisin:

        if who :
            if grille.est_ce_joueur(indiceGrille, j1.numero) and grille.EstJouable(indice2):
                grille.enleve(indiceGrille)

                jeton = j1.donne_jeton(indiceGrille)
                jeton.deplace(intersection2[0])

                j1.joue(indice2)
                j1.ajoute_jeton(indice2, jeton)

                who = not who

        else :
            if grille.est_ce_joueur(indiceGrille, j2.numero) and grille.EstJouable(indice2):
                grille.enleve(indiceGrille)

                jeton = j2.donne_jeton(indiceGrille)
                jeton.deplace(intersection2[0])

                j2.joue(indice2)
                j2.ajoute_jeton(indice2, jeton)

                who = not who
    
        return indice2
    
    return 0

def Phase3() :
    pass

def enleve_jeton_adversaire(joueur) :
    global estMoulin

    coordClic = fltk.attend_clic_gauche()
    intersection = est_une_intersection(coordClic)

    if intersection[0] != 0 :
        indice = intersection[1]

        if joueur == 1 :
            if grille.est_ce_joueur(indice, j2.numero) :
                j2.donne_jeton(indice).efface()
                grille.enleve(indice)
                estMoulin = False
        
        if joueur == 2 :
                if grille.est_ce_joueur(indice, j1.numero) :
                    j1.donne_jeton(indice).efface()
                    grille.enleve(indice)
                    estMoulin = False

def afficheMoulin(qui:int) :
    if qui == 1 :
        color = j1.couleur
    else :
        color = j2.couleur

    fltk.texte(610, 20, f"Moulin pour Joueur : {qui}", couleur=color, tag="afficheMoulin")


fltk.cree_fenetre(config.WEIGHT, config.HEIGHT)
fltk.rectangle(0, 0, config.WEIGHT, config.HEIGHT, remplissage="#086398")
color = "#faf9f7"

typePlateau:int = 1

if typePlateau == 2 :

    Intersections_ = config.IntersectionsPlateau2
    interface.plateau_2(color)

elif typePlateau == 3 :
    Intersections_ = config.IntersectionsPlateau3
    interface.plateau_3(color)

elif typePlateau == 4:
    Intersections_ = config.IntersectionsPlateau4
    interface.plateau_4(color)

else :
    Intersections_ = config.IntersectionsPlateau1
    interface.plateau_1(color)


#creation des cercles dans les intersections
for i in Intersections_:
    for coord in i :
        fltk.cercle(coord[0], coord[1],10, remplissage=color, couleur="white")
        fltk.cercle(coord[0], coord[1],7, remplissage="#086398", couleur="#086398")

grille = creerPlateau(typePlateau)

jetonsJ1 = list()
jetonsJ2 = list()

nombreDeJeton = grille.nombreJeton

j1 = joueur.Joueur(grille, 1, nombreDeJeton, "#4dfa41")
j2 = joueur.Joueur(grille, 2, nombreDeJeton, "#ffd414")

numeroJeton = 1

for _ in range(nombreDeJeton) :
    jeton = joueur.Jeton(17, (1381, 467), j1.couleur, numeroJeton)
    jetonsJ1.append(jeton)

    jeton = joueur.Jeton(17, (100, 475), j2.couleur, numeroJeton)
    jetonsJ2.append(jeton)
    
    numeroJeton += 1


who = True
phase = 1
estMoulin = False


while True :

    if who :
        fltk.texte(10, 10, "Tour : Joueur 1", taille=20, tag="tour", couleur=j1.couleur)
    else :
        fltk.texte(10, 10, "Tour : Joueur 2", taille=20, tag="tour", couleur=j2.couleur)

    if phase == 1 and not estMoulin:
        dernierClicIndice = Phase1()

    elif phase == 2 and not estMoulin:
        dernierClicIndice = Phase2()

    if dernierClicIndice != 0 and not estMoulin:
        moulin = grille.moulin(dernierClicIndice)

    else :
        moulin = ["Null"]


    if moulin[0] != "Null" :
        print(moulin)
        _joueur = moulin[0]
        estMoulin = True
        afficheMoulin(_joueur)

    if estMoulin :
        enleve_jeton_adversaire(_joueur)
        fltk.efface("afficheMoulin")

    if typePlateau != 3 :
        if j1.nbJeton == 3 :
            j1.estMaster = True

        if j2.nbJeton == 3 :
            j2.estMaster = True

    if j1.nbJeton <= 2 :
        print("Joueur 2 gagné")
        break

    if j2.nbJeton <= 2 :
        print("Joueur 1 gagné") 
        break

    fltk.mise_a_jour()
    fltk.efface("tour")