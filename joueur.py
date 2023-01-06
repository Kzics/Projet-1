import fltk


class Jeton :

    """
    Attributs
    ---------
    couelur : couleur du cercle.
    rayon : rayon du cerlce.
    coord (tuple) contient x, y pixel pour placer la cercle?
    numero : numero de class

    Methodes
    --------
    rafrachir() :
        Efface le cercle, et repose à nouveau.
    
    effacenum() :
        Permet effacer la numero se trouve sur la cercle (jeton)
    
    deplace(coord) :
        Permet de déplacer à nouveau coordonner.
    
    efface() :
        Permet de effacer la cercle (jeton)
    """

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

    def effacenum(self) :
        fltk.efface(self.fltknumero)

    def deplace(self, coord:tuple) :
        self.x, self.y = coord
        self.rafraichir()
    
    def efface(self) :
        fltk.efface(self.fltkobj)
        fltk.efface(self.fltknumero)


class Joueur :

    """
    Attributs
    ---------
    plateau : object plateau.plateau_X.
    numero : numero de joueur, (joueur1 = 1 et joueur2 = 2).
    nombredEJeton: nombre de jetons que joueur possede.
    couleur : couleur de joueur (joueur1 = vert, joueur2 = jaune).
    saut : indique si joueur peut sauter.
    Jeton : dico qui contient les objects jetons avec l'indice correspond, {indice : jeton}.


    Methodes
    --------
    joue(coord) :
        permet de jouer la cout du joueur dans indice correspond.

    ajoute_jeton(indice, jeton) :
        permet d'ajouter l'object jeton dans la dico Jeton avec l'indice correpond.
    
    donne_jetons(indice) :
        permet de retourner l'object jeton avec l'indice correspond.
    
    enleve_jeton(indice) :
        enlever l'object jetons du joueur avec l'indice correspond.
    
    estbloqué() :
        permet de verifier, si la joueur est bloqué (ne plus déplacer leur pions)
    """


    def __init__(self, plateau, numero:int, nombreDeJeton:int, couleur:str) -> None :
        self.numero = numero
        self.plateau = plateau

        self.Jeton = dict()
        self.nbJeton = nombreDeJeton

        self.couleur = couleur

        self.saut = False

    def joue(self, coord:tuple) :
        self.plateau.joue(coord, self.numero)

    def ajoute_jeton(self, indice:tuple, jeton) :
        self.Jeton[indice] = jeton
    
    def donne_jeton(self, indice:tuple) -> Jeton:
        return self.Jeton.pop(indice)

    def enleve_jeton(self, indice:tuple) -> Jeton:
        self.nbJeton -= 1
        return self.Jeton.pop(indice)

    def estbloqué(self) -> bool :
        
        mesPostions:list = self.Jeton.keys()

        for indice in mesPostions :
            voisins:list = self.plateau.Liens[indice]

            for coord in voisins :
                if self.plateau.EstJouable(coord) :
                    return False

        return True and not self.saut


