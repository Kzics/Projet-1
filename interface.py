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
    fltk.ligne(1200, 100, 950, 300, epaisseur=3, couleur=color)


# while True:
#     ev = donne_ev()
#     tev = type_ev(ev)
    
#     if tev == "ClicGauche":
#         print("Clic gauche au point", (abscisse(ev), ordonnee(ev)))
    
#     elif tev == 'Quitte':  # on sort de la boucle
#         break

#     mise_a_jour()

# ferme_fenetre()
