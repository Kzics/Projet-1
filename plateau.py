import config
from pprint import pprint

class Plateau :

    def __init__(self, typePlateau:int = 1) -> None :
        
        self.typePlateau = typePlateau

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


    def EstJoué(self, i, j) -> bool :
            if self.plateau[i][j] == 0 :
                return False
            
            return True

    
    def joue(self, i:int, j:int, joueur:str) -> bool :

        print(not self.EstJoué(i,j))
        if not self.EstJoué(i, j) :
            print("eeee")
            self.plateau[i][j] = joueur
            return True

        else :
            print("zzzz")
            return False


    def enleve(self, i:int, j:int) -> None :
        try :
            self.plateau[i][j] = 0
        except :
            pass


    def _MoulinLigne_(self) -> list:

        for ligne in range(len(self.plateau)) :

            if len(self.plateau[ligne]) == 3 :
                if self.plateau[ligne][0] == self.plateau[ligne][1] == self.plateau[ligne][2] and self.plateau[ligne][0] !=0 :
                        return [self.plateau[ligne][0], (ligne, 0), (ligne, 1), (ligne, 2)]
            
            else :
                if len(self.plateau[ligne]) == 6 :

                    if self.plateau[ligne][0] == self.plateau[ligne][1] == self.plateau[ligne][2] and self.plateau[ligne][0] != 0:
                        return [self.plateau[ligne][0], (ligne, 0), (ligne, 1), (ligne, 2)]

                    if self.plateau[ligne][3] == self.plateau[ligne][4] == self.plateau[ligne][5] and self.plateau[ligne][3] != 0:
                        return [self.plateau[ligne][3], (ligne, 3), (ligne, 4), (ligne, 5)]

        return ["Null"]
        
    
    def _MoulinColonne_(self) -> list:
        if self.typePlateau == 3 :
            for j in range(3) :
                if self.plateau[0][j] == self.plateau[1][j] == self.plateau[2][j] and self.plateau[0][j] != 0:
                    return [self.plateau[0][j], (0,j), (1,j), (2,j)]

        elif self.typePlateau == 2 :

            if self.plateau[0][0] == self.plateau[2][0] == self.plateau[4][0] and self.plateau[0][0] != 0:
                return [self.plateau[0][0], (0,0), (2,0), (4,0)]
            
            if self.plateau[1][0] == self.plateau[2][1] == self.plateau[3][0] and self.plateau[1][0] != 0:
                return [self.plateau[1][0], (1,0), (2,1), (3,0)]
            
            if self.plateau[1][2] == self.plateau[2][2] == self.plateau[3][2] and self.plateau[1][2] != 0:
                return [self.plateau[1][2], (1,2), (2,2), (3,2)]
            
            if self.plateau[0][2] == self.plateau[2][3] == self.plateau[4][2] and self.plateau[0][2] != 0:
                return [self.plateau[0][2], (0,2), (2,3), (4,2)]

        else :
            for coords in config.CoordMoulinColnnePlateau1 :
                tmp = list()
                for coord in coords :
                    tmp.append( self.plateau[coord[0]][coord[1]] )
                
                if tmp[0] == tmp[1] == tmp[2] and tmp[0] != 0:
                    coords.insert(0, tmp[0])
                    return coords

        return ["Null"]

    def Moulin(self) -> list:
        ligne = self._MoulinLigne_()

        if ligne[0] != "Null" : 
            return ligne
        else :
            colonne = self._MoulinColonne_()
            if colonne[0] != "Null" :
                return colonne
        
        return ["Null"]


    def donne_stat(self) :
        pprint(self.plateau)