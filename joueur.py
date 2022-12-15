from pprint import pprint
import fltk

class Joueur :

    def __init__(self, plateau, numero:int) -> None :
        self.numero = numero
        self.plateau = plateau

        self.Jeton = dict()

        self.estMaster = False

    def joue(self, coord:tuple):
        self.plateau.joue(coord, self.numero)

    def ajoute_jeton(self, indice:tuple, jeton) :
        self.Jeton[indice] = jeton
    
    def donne_jeton(self, indice:tuple) :
        return self.Jeton.pop(indice)

class Jeton :
    def __init__(self, rayon:int, coord:tuple, couleur:str) -> None:
        self.couleur = couleur
        self.rayon = rayon
        self.x, self.y = coord

        self.fltkobj = fltk.cercle(self.x, self.y, self.rayon, remplissage=self.couleur)
    
    def rafraichir(self) :
        fltk.efface(self.fltkobj)
        self.fltkobj = fltk.cercle(self.x, self.y, self.rayon, remplissage=self.couleur)

    def deplace(self, coord:tuple) :
        self.x, self.y = coord
        self.rafraichir()
    
    def efface(self) :
        fltk.efface(self.fltkobj)