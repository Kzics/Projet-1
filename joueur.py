class Joueur :

    def __init__(self, plateau, couleur:str) -> None :
        self.couleur = couleur
        self.plateau = plateau

        self.Jeton = list()

        self.estMaster = False

    def joue(self, coord:tuple) :
        i,j = coord
        self.plateau.joue(i, j, self.couleur)

    def ajoute_jeton(self, jeton) :
        self.Jeton.appen(jeton)