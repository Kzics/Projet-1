from pprint import pprint

import config

class Plateau :

    """
    Methodes
    --------
    creeer_plateau(Type) :
        Creer un liste de liste qui renvoie à plateau correspond.
    
    est_un_voisin(indice1, indice2) :
        Renvoie True si indice2 est un voisin d'indice1.
    
    EstJouable(indice) :
        Renvoie True si l'indice corrspond est une place disponible (0) pour déplacer le pion.
    
    est_ce_joueur(indice, joueur) :
        Renvoie True si joueur est présent dans cette indice.
    
    joue(indice, joueur) :
        Remplace la valeur de plateau dans cette indice par joueur.
    
    enleve(indice) :
        Enleve la joueur dans cette indice.
    
    compare(a, b, c) :
        Verifier si a == b == c.
    """

    def __init__(self, typePlateau) -> None :
        self.plateau = self.creer_plateau(typePlateau)

    
    def creer_plateau(self, Type:int) -> list:
        grille = list()

        if Type == 1 :
            for i in range(7) :
                if i != 3 :
                    grille.append([0]*3)
                else :
                    grille.append([0]*6)
        
        elif Type == 2 :
            for i in range(5) :
                if i != 2 :
                    grille.append([0]*3)
                else :
                    grille.append([0]*4)
        
        else :
            grille = [[0]*3 for _ in range(3)]
            
        return grille

    def est_un_voisin(self, indice1:tuple, indice2:tuple) -> bool :
        try :
            return indice2 in self.Liens[indice1]
        except :
            return False


    def EstJouable(self, indice:tuple) -> bool :
        i,j = indice
        if self.plateau[i][j] == 0 :
            return True

        return False

    def est_ce_joueur(self, indice:tuple, joueur:int) -> bool :
        i,j = indice
        if self.plateau[i][j] == joueur :
            return True
        return False
    
    def joue(self, indice:tuple, joueur:str) -> None :
        i,j = indice
        self.plateau[i][j] = joueur
        return True


    def enleve(self, indice:tuple) -> None :
        try :
            i,j = indice
            self.plateau[i][j] = 0
        except :
            pass

    def compare(self, a:int, b:int, c:int) -> int:
        if a == b == c :
            return a
        else :
            return 0


    def affiche(self) :
        pprint(self.plateau)
        print("\n")



class Plateau_1(Plateau) :

    
    #     (0,0)--------------(0,1)-------------(0,2)
    #      |                    |                |
    #      |     (1,0)-------(1,1)-------(1,2)   |
    #      |       |           |           |     |
    #      |       |  (2,0)--(2,1)--(2,2)  |     |
    #      |       |    |             |    |     |
    #      |       |    |             |    |     |
    #    (3,0)--(3,1)--(3,2)       (3,3)--(3,4)--(3,5)
    #      |       |    |             |    |     |
    #      |       |    |             |    |     |
    #      |       |  (4,0)--(4,1)--(4,2)  |     |
    #      |       |           |           |     |
    #      |      (5,0)------(5,1)-------(5,2)   |
    #      |                   |                 |
    #     (6,0)--------------(6,1)-------------(6,2)
    

    def __init__(self) -> None :
        super().__init__(1)
        self.Type = 1
        self.nombreJeton = 9
        self.Liens = config.LiensPlateau1


    def _moulin_ligne_(self, indice:tuple) -> list:

        """
        Arguments :
            indice (tuple) : derniere positions (indice) clicker par joueur.
        
        Renvoie (list) :
            si moulin formé horizontale, renvoie coord de l'écran (x,y) et un liste qui contient les indices formé,
            sinon renvoie liste ["Null"].
        """

        i, j = indice
        ligne = self.plateau[i]

        if i == 3 and j > 2 :
            joueur = self.compare(ligne[3], ligne[4], ligne[5])
            if joueur : return [joueur, ((i,3), (i,4), (i,5))]
        
        else :
            joueur = self.compare(ligne[0], ligne[1], ligne[2])
            if joueur : return [joueur, ((i,0), (i,1), (i,2))]
        
        return ["Null"]


    def _moulin_colonne_(self, indice:tuple) -> list :

        """
        Arguments :
            indice (tuple) : derniere positions (indice) clicker par joueur.
        
        Renvoie (list) :
            si moulin formé verticale, renvoie coord de l'écran (x,y) et un liste qui contient les indices formé,
            sinon renvoie liste ["Null"].
        """

        i, j = indice
        z = None

        #Verifier la moulin dans les lignes veriticales j = 1, sauf dans l'indice (3,1).
        if j == 1 and i != 3:

            if i <= 2 :
                z = (0,1,2) # les indices i de la ligne verticale bas.
            else :
                z = (4,5,6) # les indices i de la ligne verticale haut.

            joueur = self.compare(self.plateau[z[0]][j], self.plateau[z[1]][j], self.plateau[z[2]][j])
            if joueur : 
                return [joueur, ((z[0],1), (z[1],1), (z[2],1))]
            else : 
                return ["Null"]
            
        # Verifier la moulin dans les lignes veritcales de 1er carré (indice [0,0]).
        if i%3 == 0 and (j == 0 or (j in [2,5] and j+1 != i)) :

            if j == 0 : # ligne de gauche
                z = (0,)*3

            elif j in [2,5] : #ligne de droite
                z = (2,5,2)

            else :
                pass
            
            joueur = self.compare(self.plateau[0][z[0]], self.plateau[3][z[1]], self.plateau[6][z[2]])
            if joueur :
                return [joueur, ( (0,z[0]), (3, z[1]), (6, z[2]) )]
            else :
                return ["Null"]
        

        # Verifier la moulin dans les lignes veritcales de 2eme carré (indice [1,0]).
        if i%2 == 1 and (j in [0,1] or (j in [2,4] and j+1 != i)):

            if j in [0,1] :
                z = (0,1,0)

            elif j in [2,4] :
                z = (2,4,2)
            

            else :
                pass
            
            joueur = self.compare(self.plateau[1][z[0]], self.plateau[3][z[1]], self.plateau[5][z[2]])
            if joueur :
                return [joueur, ( (1,z[0]), (3, z[1]), (5, z[2]) )]
            else :
                return ["Null"]

        # Verifier la moulin dans les lignes veritcales de 3eme carré (indice [2,0])
        if i in [2,3,4] :

            if j == 0 or (j == 2 and i == 3) : #ligne gauche
                z = (0,2,0)

            elif j in [2,3]: #line droite
                z = (2,3,2)
            
            else :
                pass
            
            joueur = self.compare(self.plateau[2][z[0]], self.plateau[3][z[1]], self.plateau[4][z[2]])
            if joueur :
                return [joueur, ((2, z[0]), (3, z[1]), (4, z[2]))]
            else :
                return ["Null"]
            

    def moulin(self, indice:tuple) -> list:

        """
        Regroupe moulin_ligne et moulin_colonne.
        Argument :
            indice (tuple) : derniere positions (indice) clicker par joueur.
        """

        ligne = self._moulin_ligne_(indice)
        if ligne[0] != "Null" :
            return ligne
        
        colonne = self._moulin_colonne_(indice)
        if colonne[0] != "Null" :
            return colonne
        
        return ["Null"]


class Plateau_2(Plateau) :
    
    # (0,0)--------(0,1)--------(0,2)
    #   |             |            |
    #   |             |            |
    #   |   (1,0)---(1,1)---(1,2)  |
    #   |     |               |    |
    #   |     |               |    |
    # (2,0)--(2,1)         (2,2)--(2,3)
    #   |     |               |    |
    #   |     |               |    |
    #   |    (3,0)---(3,1)---(3,2) |
    #   |		      |            |
    #   |		 	  |            |  
    #  (4,0)---------(4,1)--------(4,2)


    def __init__(self) -> None :
        super().__init__(2)
        self.Type = 2
        self.nombreJeton = 6
        self.Liens = config.LiensPlateau2

    def _moulin_ligne_(self, indice:tuple) -> list :
        i, j = indice

        if i == 2 :
            return ["Null"]

        ligne = self.plateau[i]
        joueur = self.compare(ligne[0], ligne[1], ligne[2])

        if joueur :
            return [joueur, ((i,0), (i,1), (i,2))]
        else :
            return ["Null"]

    def _moulin_colonne_(self, indice:tuple) -> list:
        i, j = indice

        if j == 1 and i != 2 :
            return ['Null']

        # verifie moulin les lignes verticals de 1er carré (indice [0,0] ).
        if i%2 == 0 :

            if j==0 : # ligne gauche
                joueur = self.compare(self.plateau[0][0], self.plateau[2][0], self.plateau[4][0])
                if joueur : return [joueur, ((0,0), (2,0), (4,0))]

            elif (i != j and j in [2,3]) : # ligne droite
                joueur = self.compare(self.plateau[0][2], self.plateau[2][3], self.plateau[4][2])
                if joueur : return [joueur, ((0,2), (2,3), (4,2))]

            else:
                pass
        
        # verifie moulin les lignes verticals de 2eme carré (indice [1,0] ).

        if j == 2 :
            z = (2,)*3   # indices j de la ligne droite
        else :
            z = (0,1,0)  # indices j de la ligne gauche

        joueur = self.compare(self.plateau[1][z[0]], self.plateau[2][z[1]], self.plateau[3][z[2]])
        if joueur :
            return [joueur, (1, (z[0]), (2, z[1]), (3, z[2]))]
        
        return ["Null"]


    def moulin(self, indice:tuple) -> list:
        ligne = self._moulin_ligne_(indice)
        if ligne[0] != "Null" :
            return ligne
        
        colonne = self._moulin_colonne_(indice)
        if colonne[0] != "Null" :
            return colonne
        
        return ["Null"]


class Plateau_3(Plateau) :

    # (0,0)---(0,1)---(0,2)
    # |  \      |      /  |
    # |     \   |   /     |
    # (1,0)---(1,1)---(1,2)
    # |    /    |  \      |
    # |  /      |     \   |
    # (2,0)---(2,1)---(2,2)


    def __init__(self) -> None :
        super().__init__(3)
        self.Type = 3
        self.nombreJeton = 3
        self.Liens = config.LiensPlateau3

    def _moulin_ligne_(self, indice:tuple) -> list:
        i,j = indice
        ligne = self.plateau[i]
        joueur = self.compare(ligne[j], ligne[(j+1)%3], ligne[(j-1)%3])

        if joueur :
            return [joueur, ((i,j), (i, (j+1)%3), (i, (j-1)%3))]
        return ["Null"]

    def _moulin_colonne_(self, indice:tuple) -> list :
        i,j = indice
        joueur = self.compare(self.plateau[i][j], self.plateau[(i+1)%3][j], self.plateau[(i-1)%3][j])

        if joueur :
            return [joueur, ((i,j), ((i+1)%3, j), ((i-1)%3, j))]

        return ["Null"]
    
    def _moulin_diagonalle_(self, indice:tuple) -> list :
        i,j = indice

        if i == j == 1 :
            a, b, c = self.plateau[0][2], self.plateau[i][j], self.plateau[2][0]
            joueur = self.compare(a,b,c)
            if joueur :
                return [joueur, ((0,2), (i,j), (2,0))]

        if i == j :
            a, b, c = self.plateau[i][j], self.plateau[(i+1)%3][(j+1)%3], self.plateau[(i+2)%3][(j+2)%3]
            joueur = self.compare(a, b, c)
            if joueur :
                return [joueur, ((i,j), ((i+1)%3, (j+1)%3), ((i+2)%3, (j+2)%3))]
                
        elif i+j == 2 :
            a, b, c = self.plateau[i][j], self.plateau[(i+1)%3][(j-1)%3], self.plateau[(i+2)%3][(j-2)%3]
            joueur = self.compare(a, b, c)
            if joueur :
                return [joueur, ((i,j), ((i+1)%3, (j-1)%3), ((i+2)%3, (j-2)%3))]

        return ["Null"]

    def moulin(self, indice:tuple) -> list :
        ligne = self._moulin_ligne_(indice)
        if ligne[0] != "Null" :
            return ligne
        
        colonne = self._moulin_colonne_(indice)
        if colonne[0] != "Null" :
            return colonne
        
        diagonalle = self._moulin_diagonalle_(indice)
        if diagonalle[0] != "Null" :
            return diagonalle
        
        return ["Null"]


class Plateau_4(Plateau_1) :

    #     (0,0)--------------(0,1)-------------(0,2)
    #      |    \               |             /  |
    #      |     (1,0)-------(1,1)-------(1,2)   |
    #      |       |  \        |        /  |     |
    #      |       |  (2,0)--(2,1)--(2,2)  |     |
    #      |       |    |             |    |     |
    #      |       |    |             |    |     |
    #    (3,0)--(3,1)--(3,2)       (3,3)--(3,4)--(3,5)
    #      |       |    |             |    |     |
    #      |       |    |             |    |     |
    #      |       |  (4,0)--(4,1)--(4,2)  |     |
    #      |       |  /        |        \  |     |
    #      |      (5,0)------(5,1)-------(5,2)   |
    #      |    /              |             \   |
    #     (6,0)--------------(6,1)-------------(6,2)

    def __init__(self) -> None:
        super().__init__()
        self.Type = 4
        self.nombreJeton = 12
        self.Liens = config.LiensPlateau4

    def _moulin_diagonalle_(self, indice:tuple) -> list :
        i, j = indice

        if not ( j == 0 or j == 2) :
            return ["Null"]

        if i <= 2 :
            a,b,c = self.plateau[0][j], self.plateau[1][j], self.plateau[2][j]
            joueur = self.compare(a,b,c)
            if joueur :
                return [joueur, ((0,j), (1,j), (2,j))]
        else :
            a,b,c = self.plateau[4][j], self.plateau[5][j], self.plateau[6][j]
            joueur = self.compare(a,b,c)
            if joueur :
                return [joueur, ((4,j), (5,j), (6,j))]

        return ["Null"]

    def moulin(self, indice:tuple) -> list :
        ligne = self._moulin_ligne_(indice)
        if ligne[0] != "Null" :
            return ligne
        
        colonne = self._moulin_colonne_(indice)
        if colonne[0] != "Null" :
            return colonne
        
        diagonalle = self._moulin_diagonalle_(indice)
        if diagonalle[0] != "Null" :
            return diagonalle
        
        return ["Null"]

def creerPlateau(Type:int) :
    if Type == 4 :
        return Plateau_4()
    elif Type == 3 :
        return Plateau_3()
    elif Type == 2 :
        return Plateau_2()
    else :
        return Plateau_1()