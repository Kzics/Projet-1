from fltk import *

WEIGHT = 1500
HEIGHT = 950

def grille():
    while True:
        try:
            x = int(input("1, 2, 3 ou 4: "))
            if x < 1:
                print("Erreur, valeur trop faible réessayer")
            elif x > 4:
                print("Erreur, valeur trop grande réessayer")
            else:
                break
        except ValueError:
            print("Ce n'est pas une valeur, réessayer")
    return x

plateau = grille()
plateau

cree_fenetre(WEIGHT, HEIGHT)

if plateau == 1:
    rectangle(300, 100, 1200, 850, epaisseur=3, remplissage="#FFE0A9")
    rectangle(435, 210, 1070, 740, epaisseur=3)
    rectangle(555, 310, 950, 640, epaisseur=3)

    ligne(750, 100, 750, 310, epaisseur=3)
    ligne(750, 640, 750, 850, epaisseur=3)

    ligne(300, 475, 555, 475, epaisseur=3)
    ligne(950, 475, 1200, 475, epaisseur=3)
elif plateau == 2:
    rectangle(300, 100, 1200, 850, epaisseur=3, remplissage="#FFE0A9")
    rectangle(450, 250, 1050, 700, epaisseur=3)
    
    ligne(300, ((850-100)//2)+100, 450, ((850-100)//2)+100, epaisseur=3)
    ligne(1200, ((700-250)//2)+250, 1050, ((700-250)//2)+250, epaisseur=3)
    ligne(((1200-300)//2)+300, 100, ((1200-300)//2)+300, 250, epaisseur=3)
    ligne(((1200-300)//2)+300, 850, ((1200-300)//2)+300, 700, epaisseur=3)
elif plateau == 3:
    rectangle(300, 100, 1200, 850, epaisseur=3, remplissage="#FFE0A9")
    ligne(300, 100, 1200, 850, epaisseur=3)
    ligne(1200, 100, 300, 850, epaisseur=3)
    ligne(((1200-300)//2)+300, 100, ((1200-300)//2)+300, 850, epaisseur=3)
    ligne(300, ((850-100)//2)+100, 1200, ((850-100)//2)+100, epaisseur=3)
elif plateau == 4:
    rectangle(300, 100, 1200, 850, epaisseur=3, remplissage="#FFE0A9")
    rectangle(435, 210, 1070, 740, epaisseur=3)
    rectangle(555, 310, 950, 640, epaisseur=3)

    ligne(((1200-300)//2)+300, 100, ((1200-300)//2)+300, 310, epaisseur=3)
    ligne(((1200-300)//2)+300, 640, ((1200-300)//2)+300, 850, epaisseur=3)

    ligne(300, ((850-100)//2)+100, 555, ((850-100)//2)+100, epaisseur=3)
    ligne(950, ((850-100)//2)+100, 1200, ((850-100)//2)+100, epaisseur=3)

    ligne(300, 100, 555, 310, epaisseur=3)
    ligne(1200, 100, 950, 300, epaisseur=3)
while True:
    ev = donne_ev()
    tev = type_ev(ev)
    
    if tev == "ClicGauche":
        print("Clic gauche au point", (abscisse(ev), ordonnee(ev)))
    
    elif tev == 'Quitte':  # on sort de la boucle
        break

    mise_a_jour()

ferme_fenetre()