import time
from threading import Thread
from random import choice, randint

import fltk
import briquepattern
import bonus_malus

WEIGHT = 1920
HEIGHT = 1080

groundWeight = (340, 1579)
groundHeight = (150,870)

fltk.cree_fenetre(WEIGHT, HEIGHT)
fltk.rectangle(groundWeight[0], groundHeight[0], groundWeight[1], groundHeight[1])

listeBonus = ["vie", "randbreak", "largeur"]
listeMalus = ["invisible", "teleport", "inverse", "small"]

patterns = ["normale", "losange", "dessin1", "dessin2","dessin3", "dessin4"]

colors = ["red", "blue", "green", "yellow", "magenta", "grey", "orange", "black"]

class Raquette :

    def __init__(self, x:int, y:int)-> None :

        """
        la classe Raquette contient les methodes et les attributs de la raquette.

        args :
            x (int) : postion x de la raquette.
            y (int) : postion y de la raquette.
        """

        self.x = x
        self.y = y

        self.vitesse = 20

        self.largeur = 100
        self.longeur = 10

        self.left = "Left"
        self.right = "Right"

        self.raquette:int = fltk.rectangle(self.x, self.y, self.x+self.largeur, self.y + self.longeur, remplissage =  "#ffd64b")

    def deplaceGauche(self) -> None:

        """
        cette methode permet de deplacer la raquette à gauche.
        """
        coord:int = self.x - self.vitesse

        if not (coord  < groundWeight[0]) :
            self.x = coord
        else :
            pass

    def deplaceDroite(self) -> None:

        """
        cette methode permet de deplacer la raquette à droite.
        """
        coord:int = self.x + self.vitesse

        if not (coord + (self.largeur - self.vitesse) > groundWeight[1]) :
            self.x = coord


    def rafraichir(self) -> None:

        """
        cette methode efface la raquette actuelle puis affiche une nouvelle raquette.
        elle est appelée à chaque mouvement de raquette.
        """
        fltk.efface(self.raquette)
        self.raquette:int = fltk.rectangle(self.x, self.y, self.x+self.largeur, self.y + self.longeur, remplissage =  "#ffd64b")


    def collision(self, balle) -> None:
        
        """
        cette methode calcule la collision entre la balle et la raquette.
        si il y a une collision, la balle fait un rebond.

        args :
            balle : object (instance) balle
        """

        raquetteX, raquetteY = self.x, self.y
        balleX, balleY = balle.x, balle.y

        if balleY >= raquetteY :
            if balleX > raquetteX and balleX < raquetteX + self.largeur :

                if balleX > raquetteX + 20 and balleX < (raquetteX + self.largeur - 20) :
                    balle.rebond(y = True)
                else :
                    balle.rebond(True, True)



class Briques:
    def __init__(self, x:int, y:int, color:str, creer:bool) -> None:

        """
        args :
            x (int) : position x de la brique
            y (int) : position y de la brique
            color (str) : couleur de la brique
            creer (bool) : variable bool qui determine la creation de vrai brique ou une brique fatôme.
        """

        self.x = x
        self.y = y

        self.largeur:int = 100
        self.longeur:int = 30

        if creer :
            self.color = color
            randNum = randint(1, 10)

            self.bonus = None
            self.malus = None


            if randNum == 5 :
                self.bonus = choice(listeBonus)

            elif randNum == 8 :
                self.malus  = choice(listeMalus)
            
            self.brique = fltk.rectangle(self.x, self.y, self.x+self.largeur, self.y+self.longeur, remplissage=self.color)
    
    def centreCoord(self) -> tuple :

        """
        cette methode renvoie la coord centre de la brique (retangle).
        """

        x = (self.x + (self.x + self.largeur))/2
        y = (self.y + (self.y + self.longeur))/2
        return int(x), int(y)

    def coord(self) -> list :

        """
        cette methode renvoie les coordonnees des coins de la brique.
        """

        return [(self.x, self.y), (self.x+self.largeur, self.y+self.longeur)]
    
    def casse(self) -> None :

        """
        cette methode permet de faire disparaitre la brique.
        """

        fltk.efface(self.brique)
        self.state = "casser"

    def appartient(self, valeur:int, intervalle:tuple) -> bool:

        """
        cette methode permet de savoir si une valeure est dans un intervalle.
        """

        if valeur > intervalle[0] and valeur < intervalle[1] :
            return True

        return False            
        


    def collision(self, x:int, y:int) -> bool:

        """
        cette methode permet de savoir s'il y a eu une collision entre la balle et le haut/bas de la brique.

        args :
            x (int) : coord x de la balle
            y (int) : coord y de la balle
        """

        if self.appartient(x, (self.x + 1, (self.x + self.largeur) - 1)) :
            if self.appartient(y, (self.y - 1, (self.y + self.longeur)+1 )) :
                return True
        
        return False
    
    def collision_coté(self, x, y) -> bool:

        """
        cette methode permet de savoir s'il y a eu une collision entre la balle et le coté de la brique.
        
        args :
            x (int) : coord x de la balle
            y (int) : coord y de la balle
        """
        if self.appartient(x, (self.x-10, self.x)) or self.appartient(x,((self.x + self.largeur), (self.x + self.largeur) + 10)) :
            if self.appartient(y, (self.y -1, (self.y + self.longeur) + 1)) :
                return True
                
        return False
        
class Balle :

    def __init__(self, x:int, y:int) -> None:

        """
        class contient les methodes et les attributs de balle
        """

        self.x = x
        self.y = y

        self.rayon = 5

        self.vitesseX = 3
        self.vitesseY = 3

        self.couleur = "grey"

        self.balle:int = fltk.cercle(self.x, self.y, self.rayon, remplissage=self.couleur, couleur=self.couleur)

    def rafraichir(self) -> None:

        """ 
        cette methode effectue le rafraichissement de la balle
        """
        fltk.efface(self.balle)
        self.balle = fltk.cercle(self.x, self.y, self.rayon, remplissage=self.couleur, couleur=self.couleur)

    def rebond(self, x = False, y = False) -> None :

        """
        cette methode permet de faire rebondir la balle

        args :
            x (bool) : cette argument fait reference à la coord x de la balle. si vrai alor x = x*-1.
            y (bool) : coord y est de la balle.
        """

        if x :
            self.vitesseX *= -1
        
        if y :
            self.vitesseY *= -1

    def checkCollisionMur(self) -> None:
        
        """
        cette methode permet de verifier la collision avec un mur puis de faire rebondir la balle.
        """

        if self.x - self.rayon <= groundWeight[0] or self.x + self.rayon >= groundWeight[1] :
            self.rebond(x = True)

        if self.y + self.rayon <= groundHeight[0]:
            self.rebond(y = True)


    def deplacement(self) -> None:

        """
        cette methode effectue le prochain deplacement de la balle.
        """
        self.x += self.vitesseX * -1
        self.y += self.vitesseY * -1
        self.rafraichir()
        
    def coord(self):

        """
         cette methode renvoie les coordonnees du centre de la balle.
         """
        return self.x, self.y


def poseBriques(pattern:list) :

    """
    cette fonction permet de poser les briques en fonction du pattern donné

    args :
        pattern (list) : pattern de la brique (briquepattern.py)
    """

    x,y = groundWeight[0] + 20 , groundHeight[0] + 15
    couleur = choice(colors)

    for j in pattern :

        for i in j :

            if i :
                b = Briques(x, y, couleur, True)
                briqueListe.append(b)
            else :
                b = Briques(x, y, "black", False)

            nx, ny = b.coord()[1]
            x = nx + 20

        x = groundWeight[0] + 22
        y += 40


def perdu(y:int) -> bool:

    """
    cette fonction permet de savoir si la balle a touché le sol.

    args :
        y (int) : coord y de la balle.
    """

    if y >= groundHeight[1] :
        return True
    return False


def malusExecute(Type) :

    """
    cette fonction permet d'executer les malus
    args :
        Type (str) : type de malus (invisible, small ...)
    """

    if Type == "invisible" :
            thread = Thread(target=malus.invisible, args=(balle,))
            thread.start()

    elif Type == "teleport" :
        malus.teleport(balle)

    elif Type == "inverse" :
        thread = Thread(target=malus.inverse, args=(raquette,), daemon=True)
        thread.start()

    elif Type == "small" :
        thread = Thread(target=malus.diminue_largeur, args=(raquette,), daemon=True)
        thread.start()
    else :
        pass


def bonusExecute(Type) :

    """
    cette fonction permet d'executer les bonus
    """

    global vie, briqueListe, textVie

    if Type == "vie" :
        vie += 1
        fltk.efface(textVie)
        textVie = fltk.texte(groundWeight[0],30, f"Vie : { '| '*vie}", taille=20)

    if Type == "largeur" :
        thread = Thread(target=bonus.augmentLargeur, args=(raquette,), daemon=True)
        thread.start()

    if Type == "randbreak" :
        if len(briqueListe) > 2 :
            brique1 = choice(briqueListe)
            brique1.casse()
            briqueListe.remove(brique1)

            brique2 = choice(briqueListe)
            brique2.casse()
            briqueListe.remove(brique2)


mainloop = True

raquette = Raquette(900,850)  #creation de la raquette
balle = Balle(900,830)        #creation de la balle

vie = 3
victoire = False
tempDebuter = time.time()

malus = bonus_malus.Malus()
bonus = bonus_malus.Bonus()
                                #initialisation de toutes les données pour le breakout
briqueListe = list()

pattenUtilse:list = getattr(briquepattern, choice(patterns))
poseBriques(pattenUtilse)           #creation du niveau


fltk.texte(groundWeight[0] + 50, 80, "Effects : ", taille=20)

while vie != 0 and not victoire:

    textVie = fltk.texte(groundWeight[0] + 50 ,30, f"Vie : {vie}", taille=20)

    while mainloop :

        Text = fltk.texte(groundWeight[0]+150, 80, malus.malustxt + bonus.bonustxt, taille=20)
            
        evenement = fltk.donne_ev()

        balle.deplacement()
        if perdu(balle.y + balle.rayon) :
            break

        balle.checkCollisionMur()

        if evenement != None :
        
            if fltk.touche(evenement) == raquette.left :
                raquette.deplaceGauche()
            
            if fltk.touche(evenement) == raquette.right :
                raquette.deplaceDroite()
        
        raquette.rafraichir()

        if len(briqueListe) == 0 :
            victoire = True
            break
                
        for brique in briqueListe :
            if brique.collision_coté(balle.coord()[0],balle.coord()[1]):
                brique.casse()
                        
                if brique.malus != None :
                    malusExecute(brique.malus)
                    
                
                if brique.bonus != None :
                    bonusExecute(brique.bonus)

                balle.rebond(True,False)
                
                try :
                    briqueListe.remove(brique)
                except :
                    pass

            elif brique.collision(balle.coord()[0],balle.coord()[1]):
                brique.casse()

                if brique.malus != None :
                    malusExecute(brique.malus)
                    
                
                if brique.bonus != None :
                    bonusExecute(brique.bonus)

                balle.rebond(False,True)
                
                try :
                    briqueListe.remove(brique)
                except :
                    pass
           
        raquette.collision(balle)

        fltk.mise_a_jour()
        fltk.efface(Text)
    
    vie -= 1

    fltk.efface(textVie)
    time.sleep(1)

    balle.y = raquette.y - 10
    balle.rebond(y = True)
    balle.x = raquette.x + (raquette.largeur // 2)


fltk.efface_tout()

tempEcouler = int(time.time() - tempDebuter)
nbDeBriqueReste = len(briqueListe)

if victoire :
    fltk.texte(770, 100, "You Win", couleur="#FFD700", taille = 70)
else :
    fltk.texte(770, 100, "You lose", couleur="red", taille = 70)

fltk.texte(700, 400, f"Temps écouler : {tempEcouler}s")
fltk.texte(700, 450, f"Briques restant : {nbDeBriqueReste}")

fltk.attend_fermeture()
