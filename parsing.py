from os.path import isfile
from json import dump, load

import joueur
import config

from plateau import creerPlateau


def parse(args) -> dict :
    #main.py [nombre de jeton] [theme]
    
    jeuconfig = dict()

    if len(args) == 1 :
        jeuconfig["TypePlateau"] = 1
        jeuconfig["color"] = "#086398"
        jeuconfig["imported"] = False
        return jeuconfig
    
    if args[1] == "help" :
        helptxt = """
        usage : main.py [nombre de pion] [theme]

        nombre de pion : 3, 6, 9 et 12.
        theme : standard ou dark.

        Par defaut :
            nomnbre de pion : 9
            theme : standard
        
        Sauvergarder la partie :
            appuyer [s] pendant la jeu, puis saisir la nom du fichier.
        """

        print(helptxt)
    
    if isfile(args[1]) :

        if args[1][-4:] == "json":
            jeuconfig["imported"] = True
            jeuconfig["partie"] = chargerPartie(args[1])
            jeuconfig["TypePlateau"] = jeuconfig["partie"].TypePlateau
            jeuconfig["color"] = jeuconfig["partie"].color
            return jeuconfig
        else :
            print("ce n'est pas la bonne fichier")
            exit()

    if args[1] == "3" :
        jeuconfig["TypePlateau"] = 3

    elif args[1] == "6" :
        jeuconfig["TypePlateau"] = 2

    elif args[1] == "9" :
        jeuconfig["TypePlateau"] = 1
    
    elif args[1] == "12" :
        jeuconfig["TypePlateau"] = 4

    else :
        print("La nombre de pions disponible sont 3, 6, 9 et 12")
        exit()
    
    try :
        if args[2] == "dark" :
            jeuconfig["color"] = "#0C0C0C"
        else :
            jeuconfig["color"] = "#086398"

    except :
        jeuconfig["color"] = "#086398"

    jeuconfig["imported"] = False

    return jeuconfig


class Sauvegarder :

    """
    class permet de sauvegrader la partie dans un fichier JSON.

    Attributs
    ---------
    plateau: object plateau
    joueur1 : object joueur.joueur de joueur 1.
    joueur2 : object joueur.joueur de joueur 2.
    phase (int): phase de la partie.
    who (int): indique la tour de qui.
    jetonJ1 : objects joueur.jeton de joueur 1.
    jetonJ2 : objects joueur.jeton de joueur 2.

    Methodes
    --------
    demande_nom_fichier() :
        demander nom de fichier à user par terminale pour sauvegarder la partie.

    plateau(grille) :
        transforme les information de class plateau en dico.
    
    joueur(j1, j2) :
        transforme les information de class joueur (joueur 1 et 2) en dico.
    
    jetonsList(j1, j2) :
        transforme les information de class jeton (joueur 1 et 2) en list.
    """
    
    def __new__(cls, plateau, joueur1, joueur2, phase, who, jetonJ1, jetonJ2, userConfig) :

        fileName = cls.demande_nom_fichier()

        if fileName == "A.json" : return

        informations = dict()

        informations["plateau"] = cls.plateau(plateau)
        informations["joueurs"] = cls.joueur(joueur1, joueur2)
        informations["jetons"] = cls.jetonsList(jetonJ1, jetonJ2)

        informations["phase"] = phase
        informations["qui"] = who

        informations["color"] = userConfig["color"]
        informations["TypePlateau"] = userConfig["TypePlateau"]

        with open(fileName, "w+") as file :
            dump(informations, file, indent=4)

        print(f"partie sauvegardé dans la fichier {fileName}")

    @classmethod
    def demande_nom_fichier(cls) :

        while True :
            fileName = input('Enter "A" pour annuler \nEnter nom du fichier : ')
            if len(fileName) != 0 :
                break
            else :
                print("donner la nom correctement")
        
        return fileName + ".json"

    @classmethod
    def plateau(cls, grille) :
        info = dict()

        info["grille"] = grille.plateau
        info["type"] = grille.Type
        info["nombreJeton"] = grille.nombreJeton

        return info

    @classmethod
    def joueur(cls, j1, j2) :
        info = dict()

        info["joueur1"] = dict()
        info["joueur2"] = dict()

        info["joueur1"]["couleur"] = j1.couleur
        info["joueur1"]["saut"] = j1.saut
        info["joueur1"]["nombreDeJeton"] = j1.nbJeton
        info["joueur1"]["positionJeton"] = list(j1.Jeton.keys())
        info["joueur1"]["numerosJetons"] = cls.donne_numeros_jetons(j1.Jeton)

        info["joueur2"]["couleur"] = j2.couleur
        info["joueur2"]["saut"] = j2.saut
        info["joueur2"]["nombreDeJeton"] = j2.nbJeton
        info["joueur2"]["positionJeton"] = list(j2.Jeton.keys())
        info["joueur2"]["numerosJetons"] = cls.donne_numeros_jetons(j2.Jeton)

        return info

    
    @classmethod
    def donne_numeros_jetons(cls, jetons) :
        LesNumeros = list()

        for indice in jetons.keys() :
            numero = jetons[indice].numero
            LesNumeros.append(numero)
        
        return LesNumeros

    @classmethod
    def jetonsList(cls, j1, j2) :
        info = dict()

        info["jetonJ1"] = list()
        info["jetonJ2"] = list()

        for jeton in j1 : info["jetonJ1"].append(jeton.numero) 
        for jeton in j2 : info["jetonJ2"].append(jeton.numero) 

        return info



class chargerPartie :

    """
    class permet de charger la partie sauvegarder dans fichier JSON.

    """

    def __init__(self, fichier:str) :

        with open(fichier, "r") as file :
            self.data = load(file)

        try :
            self.grille = self.plateau(self.data["plateau"])
            self.phase:int = self.data["phase"]
            self.qui:bool = self.data["qui"]
            self.color:str = self.data["color"]
            self.TypePlateau:int = self.data["TypePlateau"]

        except :
            print("Fichier corrompu")
            exit()


    def plateau(self,infos):
        grille = creerPlateau(infos["type"])
        grille.plateau = infos["grille"]
        grille.Liens = getattr(config, f"LiensPlateau{grille.Type}")
        
        return grille

    def indice2pixel(self, indice, typePlateau) :
        if typePlateau == 1 or typePlateau == 4 :
            return config.IntersectionsPlateau1[indice[0]][indice[1]]
        elif typePlateau == 2 :
            return config.IntersectionsPlateau2[indice[0]][indice[1]]
        elif typePlateau == 3 :
            return config.IntersectionsPlateau3[indice[0]][indice[1]]

    def _joueur1_(self,infos, grille) :
        j1 = joueur.Joueur(grille, 1, infos["nombreDeJeton"], infos["couleur"])
        j1.saut = infos["saut"]
        
        for i in range(len(infos["positionJeton"])) :
            indice = infos["positionJeton"][i]
            coord = self.indice2pixel(indice, grille.Type)
            jeton = joueur.Jeton(17, coord, j1.couleur, infos["numerosJetons"][i])
            jeton.effacenum()
            j1.Jeton[tuple(indice)] = jeton
        
        return j1

    def _joueur2_(self, infos, grille) :
        j2 = joueur.Joueur(grille, 2, infos["nombreDeJeton"], infos["couleur"])
        j2.saut = infos["saut"]
        
        for i in range(len(infos["positionJeton"])) :
            indice = infos["positionJeton"][i]
            coord = self.indice2pixel(indice, grille.Type)
            jeton = joueur.Jeton(17, coord, j2.couleur, infos["numerosJetons"][i])
            jeton.effacenum()
            j2.Jeton[tuple(indice)] = jeton
        
        return j2

    def _jetonsNonPoséJ1_(self, infos, j1couleur) :
        jetonj1 = list()

        for i in infos["jetonJ1"] :
            jetonj1.append( joueur.Jeton(17, (1381, 467), j1couleur, i) )

        return jetonj1

    def _jetonsNonPoséJ2_(self, infos, j2couleur) :
        jetonj2 = list()

        for i in infos["jetonJ2"] :
            jetonj2.append( joueur.Jeton(17, (100, 475), j2couleur, i) )

        return jetonj2

    def joueur1(self) :
        try :
            return self._joueur1_(self.data["joueurs"]["joueur1"], self.grille)
        except :
            print("fichier corrompu")
            exit()

    def joueur2(self) :
        try :
            return self._joueur2_(self.data["joueurs"]["joueur2"], self.grille)
        except :
            print("fichier corrompu")
            exit()

    def jetonJ1(self) :
        try :
            return self._jetonsNonPoséJ1_(self.data["jetons"], self.data["joueurs"]["joueur1"]["couleur"])
        except :
            print("fichier corrompu")
            exit()
    
    def jetonJ2(self) :
        try :
            return self._jetonsNonPoséJ2_(self.data["jetons"], self.data["joueurs"]["joueur2"]["couleur"])
        except :
            print("fichier corrompu")
            exit()
