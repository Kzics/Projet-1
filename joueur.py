from pprint import pprint

class Joueur :

    def __init__(self, plateau, couleur:str) -> None :
        self.couleur = couleur
        self.plateau = plateau

        self.Jeton = dict()

        self.estMaster = False

    def joue(self, coord:tuple):
        i,j = coord
        self.plateau.joue(i, j, self.couleur)

    def ajoute_jeton(self, indice:tuple, jeton) :
        self.Jeton[indice] = jeton

    def donne(self) :
        pprint(self.Jeton)

    def donne_jeton(self, indice:tuple) :
        return self.Jeton.pop(indice)