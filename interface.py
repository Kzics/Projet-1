import fltk

from config import WEIGHT, HEIGHT


class coins :
    def __init__(self, rayon:int, coord:tuple, joueur:str) -> None:
        self.couleur = "black"
        self.rayon = rayon
        self.x, self.y = coord
        self.joueur = joueur


    

fltk.cree_fenetre(WEIGHT, HEIGHT)


fltk.rectangle(300, 100, 1200, 850, epaisseur=3, remplissage="#FFE0A9")
fltk.rectangle(435, 210, 1070, 740, epaisseur=3)
fltk.rectangle(555, 310, 950, 640, epaisseur=3)


fltk.ligne(300, 100, 555, 310, epaisseur=3)
fltk.ligne(1200, 100, 950, 310, epaisseur=3)

fltk.ligne(300, 850, 555, 640, epaisseur=3)
fltk.ligne(950, 640, 1200, 850, epaisseur=3)

fltk.attend_ev()

fltk.ferme_fenetre()