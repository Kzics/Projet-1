import fltk

def plateau_1(color:str) :

    fltk.rectangle(300, 100, 1200, 850, epaisseur=3, couleur=color)
    fltk.rectangle(435, 210, 1070, 740, epaisseur=3, couleur=color)
    fltk.rectangle(555, 310, 950, 640, epaisseur=3, couleur=color)

    fltk.ligne(750, 100, 750, 310, epaisseur=3, couleur=color)
    fltk.ligne(750, 640, 750, 850, epaisseur=3, couleur=color)

    fltk.ligne(300, 475, 555, 475, epaisseur=3, couleur=color)
    fltk.ligne(950, 475, 1200, 475, epaisseur=3, couleur=color)


def plateau_2(color:str) :

    fltk.rectangle(300, 99, 1200, 850, epaisseur=3, couleur=color)
    fltk.rectangle(450, 250, 1050, 700, epaisseur=3, couleur=color)
    
    fltk.ligne(300, ((850-100)//2)+100, 450, ((850-100)//2)+100, epaisseur=3, couleur=color)
    fltk.ligne(1200, ((700-250)//2)+250, 1050, ((700-250)//2)+250, epaisseur=3, couleur=color)
    fltk.ligne(((1200-300)//2)+300, 100, ((1200-300)//2)+300, 250, epaisseur=3, couleur=color)
    fltk.ligne(((1200-300)//2)+300, 850, ((1200-300)//2)+300, 700, epaisseur=3, couleur=color)


def plateau_3(color:str) :
    fltk.rectangle(300, 100, 1200, 850, epaisseur=3, couleur=color)

    fltk.ligne(300, 100, 1200, 850, epaisseur=3, couleur=color)
    fltk.ligne(1200, 100, 300, 850, epaisseur=3, couleur=color)
    fltk.ligne(((1200-300)//2)+300, 100, ((1200-300)//2)+300, 850, epaisseur=3, couleur=color)
    fltk.ligne(300, ((850-100)//2)+100, 1200, ((850-100)//2)+100, epaisseur=3, couleur=color)


def plateau_4(color:str) :

    fltk.rectangle(300, 100, 1200, 850, epaisseur=3, couleur=color)
    fltk.rectangle(435, 210, 1070, 740, epaisseur=3, couleur=color)
    fltk.rectangle(555, 310, 950, 640, epaisseur=3, couleur=color)

    fltk.ligne(((1200-300)//2)+300, 100, ((1200-300)//2)+300, 310, epaisseur=3, couleur=color)
    fltk.ligne(((1200-300)//2)+300, 640, ((1200-300)//2)+300, 850, epaisseur=3, couleur=color)

    fltk.ligne(300, ((850-100)//2)+100, 555, ((850-100)//2)+100, epaisseur=3, couleur=color)
    fltk.ligne(950, ((850-100)//2)+100, 1200, ((850-100)//2)+100, epaisseur=3, couleur=color)

    fltk.ligne(300, 100, 555, 310, epaisseur=3, couleur=color)
    fltk.ligne(1200, 100, 950, 310, epaisseur=3, couleur=color)
    fltk.ligne(300, 850, 555, 640, epaisseur=3, couleur=color)
    fltk.ligne(1200, 850, 950, 640, epaisseur=3, couleur=color)

class Intro :

    def __new__(cls, color) :
        if color == "#086398" :
            rgb = (8, 99, 152)
        else :
            rgb = (12,12,12)

        #fltk.cree_fenetre(1500, 950)

        fltk.rectangle(0, 0, 1500, 950, remplissage=color)

        Intro.PlateauAnimation()
        Intro.Animation(rgb)
        fltk.texte(20, 920, "APPUYER POUR CONTINUER", couleur="white")

        fltk.attend_ev()
        fltk.efface_tout()

        
    @classmethod
    def PlateauAnimation(cls) :
        fltk.cercle(400, 250, 10, couleur="white", epaisseur=3, remplissage="white")
        fltk.cercle(1100, 250, 10, couleur="white", epaisseur=3, remplissage="white")

        fltk.cercle(400, 800, 10, couleur="white", epaisseur=3, remplissage="white")
        fltk.cercle(1100, 800, 10, couleur="white", epaisseur=3, remplissage="white")

        count = 1
        j = 1

        while count <= 680:
            c1l1 = fltk.ligne(408,250, 408+count, 250, couleur="white", epaisseur=3)
            c1l2 = fltk.ligne(1092, 800, 1092-count, 800, couleur="white", epaisseur=3)

            fltk.mise_a_jour()

            fltk.efface(c1l1)
            fltk.efface(c1l2)

            count += 3


        count = 1

        fltk.ligne(408,250, 1092, 250, couleur="white", epaisseur=3)
        fltk.ligne(1092, 800, 408, 800, couleur="white", epaisseur=3)

        fltk.mise_a_jour()

        while count <= 535 :
            c1l3 = fltk.ligne(400,258, 400, 258+count, couleur="white", epaisseur=3)
            c1l4 = fltk.ligne(1100, 792, 1100, 792-count, couleur="white", epaisseur=3)

            fltk.mise_a_jour()

            fltk.efface(c1l3)
            fltk.efface(c1l4)

            count += 2


        fltk.ligne(400,258, 400, 792, couleur="white", epaisseur=3)
        fltk.ligne(1100, 792, 1100, 258, couleur="white", epaisseur=3)

        fltk.mise_a_jour()


    @classmethod
    def VerifieDepasemment(cls, valeur):
        if valeur < 0:
            return 0
        elif valeur > 255:
            return 255
        return valeur

    @classmethod
    def rgb2hex(cls, rgb):
        return "#%02x%02x%02x" % tuple(rgb)
    
    @classmethod
    def Animation(cls, rgb:tuple) :
        count = 1
        r,g,b = rgb

        while count < 256 :

            fltk.efface("a1")
            fltk.efface("a2")
            fltk.efface("a3")
            fltk.efface("a4")
            fltk.efface("a5")
            fltk.efface("a6")
            fltk.efface("a7")
            fltk.efface("a8")
            fltk.efface("a9")
            fltk.efface("title")

            newR = cls.VerifieDepasemment(r+count)
            newG = cls.VerifieDepasemment(g+count)
            newB = cls.VerifieDepasemment(b+count)
    
            color = cls.rgb2hex((newR, newG, newB))

            fltk.texte(490, 80, "Jeu Du Moulin", taille=60, tag="titre", couleur=color)


            fltk.ligne(407, 257, 1097, 796, couleur=color, epaisseur=3, tag="a1")
            fltk.ligne(407, 796, 1097, 257, couleur=color, epaisseur=3, tag="a2")


            fltk.ligne(400, 525, 1100, 525, couleur=color, epaisseur=3, tag="a3")
            fltk.ligne(750, 250, 750, 800, couleur=color, epaisseur=3, tag="a4")

            fltk.cercle(750,525, 15, couleur=color, remplissage="white", tag="a5")

            fltk.cercle(400, 525, 10, couleur=color, remplissage=color, tag="a6")
            fltk.cercle(1100, 525, 10, couleur=color, remplissage=color, tag="a7")

            fltk.cercle(750, 250, 10, couleur=color, remplissage=color, tag="a8")
            fltk.cercle(750, 800, 10, couleur=color, remplissage=color, tag="a9")


            fltk.mise_a_jour()
            count += 2
