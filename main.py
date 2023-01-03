import sys

import fltk
import joueur
import interface
import config
import parsing

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


def Phase1(coordClic) :
    global who, phase

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

def PhaseFinale(coordClic1) :
    global who

    intersection:list = est_une_intersection(coordClic1)
    coordFenetre, indiceGrille = intersection

    coordClic2 = fltk.attend_clic_gauche()
    intersection2:list = est_une_intersection(coordClic2)
    indice2:tuple = intersection2[1]

    #verification pour phase 3
    if who :
        if j1.saut: 
            estUnVoisin = True
        else :
            estUnVoisin:bool = grille.est_un_voisin(indiceGrille, indice2)

    else :
        if j2.saut: 
            estUnVoisin = True
        else :
            estUnVoisin:bool = grille.est_un_voisin(indiceGrille, indice2)
    

    if coordFenetre != 0 and intersection2[0] != 0 and estUnVoisin:

        if who :

            if grille.est_ce_joueur(indiceGrille, j1.numero) and grille.EstJouable(indice2):
                grille.enleve(indiceGrille)

                jeton = j1.donne_jeton(indiceGrille)
                jeton.deplace(intersection2[0])

                j1.joue(indice2)
                j1.ajoute_jeton(indice2, jeton)

                who = not who

                return indice2

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


def enleve_jeton_adversaire(joueur:int) -> None :
    global estMoulin

    coordClic = fltk.attend_clic_gauche()
    intersection:list = est_une_intersection(coordClic)

    if intersection[0] != 0 :
        indice:tuple = intersection[1]

        if joueur == j1.numero :
            if grille.est_ce_joueur(indice, j2.numero) :
                j2.enleve_jeton(indice).efface()
                grille.enleve(indice)
                estMoulin = False
        
        if joueur == j2.numero :
                if grille.est_ce_joueur(indice, j1.numero) :
                    j1.enleve_jeton(indice).efface()
                    grille.enleve(indice)
                    estMoulin = False


def verifie_fin_du_partie() -> int :
    joueurGagné = 0

    if j1.nbJeton <= 2 or  (phase == 2 and j1.estbloqué()):
        joueurGagné = 2

    if j2.nbJeton <= 2 or (phase == 2 and j2.estbloqué()):
        joueurGagné = 1
    
    if joueurGagné :
        fltk.texte(580, 20, f"Fin du Partie Joueur {joueurGagné} Gagné", couleur=color, tag="afficheMoulin")

    return joueurGagné


def afficheMoulin(qui:int) -> None:
    if qui == 1 :
        color = j1.couleur
    else :
        color = j2.couleur

    fltk.texte(610, 20, f"Moulin pour Joueur : {qui}", couleur=color, tag="afficheMoulin")

fltk.cree_fenetre(config.WEIGHT, config.HEIGHT)

userconfig = parsing.parse(sys.argv)
isImported = userconfig["imported"]

partie = userconfig["partie"] if isImported else 0

remcolor =  partie.color if isImported else userconfig["color"]
typePlateau:int = partie.TypePlateau if isImported else userconfig["TypePlateau"]

interface.Intro(remcolor)

fltk.rectangle(0, 0, config.WEIGHT, config.HEIGHT, remplissage=remcolor)
color = "#faf9f7"


if typePlateau == 2 :
    Intersections_ = config.IntersectionsPlateau2
    interface.plateau_2(color)

elif typePlateau == 3 :
    Intersections_ = config.IntersectionsPlateau3
    interface.plateau_3(color)

elif typePlateau == 4:
    Intersections_ = config.IntersectionsPlateau1
    interface.plateau_4(color)

else :
    Intersections_ = config.IntersectionsPlateau1
    interface.plateau_1(color)


#creation des cercles dans les intersections
for i in Intersections_:
    for coord in i :
        fltk.cercle(coord[0], coord[1],10, remplissage=color, couleur="white")


grille = partie.grille if isImported else creerPlateau(typePlateau)

jetonsJ1 = partie.jetonJ1() if isImported else list()
jetonsJ2 = partie.jetonJ2() if isImported else list()

nombreDeJeton:int = grille.nombreJeton

j1 = partie.joueur1() if isImported else joueur.Joueur(grille, 1, nombreDeJeton, "#4dfa41")
j2 = partie.joueur2() if isImported else joueur.Joueur(grille, 2, nombreDeJeton, "#ffd414")

if not isImported : 
    numeroJeton = 1
    for _ in range(nombreDeJeton) :
        jeton = joueur.Jeton(17, (1381, 467), j1.couleur, numeroJeton)
        jetonsJ1.append(jeton)

        jeton = joueur.Jeton(17, (100, 475), j2.couleur, numeroJeton)
        jetonsJ2.append(jeton)
        
        numeroJeton += 1


who = partie.qui if isImported else True
phase = partie.phase if isImported else 1
estMoulin = False


while True:

    fltk.mise_a_jour()

    if not estMoulin :
        if who :
            fltk.texte(10, 10, "Tour : Joueur 1", taille=20, tag="tour", couleur=j1.couleur)
        else :
            fltk.texte(10, 10, "Tour : Joueur 2", taille=20, tag="tour", couleur=j2.couleur)

    evenement = fltk.attend_ev()
    typeEvenement = fltk.type_ev(evenement)

    if typeEvenement == "Quitte" :
        fltk.ferme_fenetre()
        break

    elif typeEvenement == "ClicGauche" :
        coorClic = (fltk.abscisse(evenement), fltk.ordonnee(evenement))

    elif fltk.touche(evenement) == "s" :
        parsing.Sauvegarder(plateau=grille, joueur1=j1, joueur2=j2, phase=phase, 
                    who = who, jetonJ1=jetonsJ1, jetonJ2=jetonsJ2, userConfig=userconfig)

    else :
        fltk.efface("tour")
        continue


    if phase == 1 and not estMoulin:
        dernierClicIndice = Phase1(coorClic)
    elif phase == 2 and not estMoulin:
        dernierClicIndice = PhaseFinale(coorClic)


    if dernierClicIndice != 0 and not estMoulin:
        moulin:list = grille.moulin(dernierClicIndice)
    else :
        moulin = ["Null"]


    if moulin[0] != "Null" :
        _joueur:int = moulin[0]
        estMoulin = True

    if estMoulin :
        afficheMoulin(_joueur)
        enleve_jeton_adversaire(_joueur)

    if not estMoulin :    
        fltk.efface("afficheMoulin")

    if typePlateau not in (2,3) and j1.nbJeton == 3 :
        j1.saut = True
        print('Joueur 1 saut activé') 
    if typePlateau not in (2,3) and j2.nbJeton == 3 :
        j2.saut = True
        print('Joueur 2 saut activé') 

    if verifie_fin_du_partie() :
        break
    
    fltk.efface("tour")
    fltk.mise_a_jour()

    debug = True

try :
    fltk.attend_ev()
except :
    pass