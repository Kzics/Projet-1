from pprint import pprint
import fltk

class Joueur :

    def __init__(self, plateau, numero:int, nombreDeJeton:int, couleur:str) -> None :
        self.numero = numero
        self.plateau = plateau

        self.Jeton = dict()
        self.nbJeton = nombreDeJeton

        self.couleur = couleur

        self.estMaster = False

    def joue(self, coord:tuple):
        self.plateau.joue(coord, self.numero)

    def ajoute_jeton(self, indice:tuple, jeton) :
        self.Jeton[indice] = jeton
        self.nbJeton += 1
    
    def donne_jeton(self, indice:tuple) :
        self.nbJeton -= 1
        return self.Jeton.pop(indice)

class Jeton :
    def __init__(self, rayon:int, coord:tuple, couleur:str, numero:int) -> None:
        self.couleur = couleur
        self.rayon = rayon
        self.x, self.y = coord
        self.numero = numero

        self.fltkobj = fltk.cercle(self.x, self.y, self.rayon, remplissage=self.couleur, couleur=self.couleur)
        self.fltknumero = fltk.texte(self.x-5, self.y-10, self.numero, couleur="black", taille=15)
    
    def rafraichir(self) :
        fltk.efface(self.fltkobj)
        fltk.efface(self.fltknumero)
        self.fltkobj = fltk.cercle(self.x, self.y, self.rayon, remplissage=self.couleur, couleur=self.couleur)
        

    def deplace(self, coord:tuple) :
        self.x, self.y = coord
        self.rafraichir()
    
    def efface(self) :
        fltk.efface(self.fltkobj)
        fltk.efface(self.fltknumero)