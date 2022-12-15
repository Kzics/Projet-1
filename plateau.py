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


    def EstJouable(self, coord:tuple) -> bool :
        i,j = coord
        if self.plateau[i][j] == 0 :
            return True

        return False

    def est_ce_joueur(self, coord:tuple, joueur:str) -> bool :
        i,j = coord
        if abs(self.plateau[i][j]) == joueur :
            return True
        return False
    
    def joue(self, coord:tuple, joueur:str) -> None :
        i,j = coord
        self.plateau[i][j] = joueur
        return True


    def enleve(self, coord:tuple) -> None :
        try :
            i,j = coord
            self.plateau[i][j] = 0
        except :
            pass

    def est_un_voisin(self, indice1:tuple, indice2:tuple) -> bool :
        if self.typePlateau == 1 :
            try :
                return indice2 in config.LiensPlateau1[indice1]
            except :
                return False

    def compare(self, a:int, b:int, c:int) -> int:
        if (a == b == c ) and (a > 0 or b > 0 or c > 0) :
            return abs(a)
        else:
            return 0

    def _MoulinLigne_(self) -> list:

        for ligne in range(len(self.plateau)) :

            if len(self.plateau[ligne]) == 3 :
                joueur = self.compare(self.plateau[ligne][0], self.plateau[ligne][1], self.plateau[ligne][2])
                if joueur :
                    return [joueur,[ (ligne, 0), (ligne, 1), (ligne, 2)]]
            
            else :
                if len(self.plateau[ligne]) == 6 :
                    joueur = self.compare(self.plateau[ligne][0], self.plateau[ligne][1], self.plateau[ligne][2])
                    if joueur:
                        return [joueur, [ (ligne, 0), (ligne, 1), (ligne, 2)]]
                    
                    joueur = self.compare(self.plateau[ligne][3], self.plateau[ligne][4], self.plateau[ligne][5])
                    if joueur:
                        return [joueur, [(ligne, 3), (ligne, 4), (ligne, 5)]]

        return ["Null"]
        
    
    def _MoulinColonne_(self) -> list:
        if self.typePlateau == 3 :
            for j in range(3) :
                joueur = self.compare(self.plateau[0][j], self.plateau[1][j], self.plateau[2][j])
                if joueur:
                    return [joueur, [(0,j), (1,j), (2,j)]]

        elif self.typePlateau == 2 :
            
            joueur = self.compare(self.plateau[0][0], self.plateau[2][0], self.plateau[4][0])
            if joueur :
                return [joueur, [(0,0), (2,0), (4,0)]]
            
            joueur = self.compare(self.plateau[1][0], self.plateau[2][1], self.plateau[3][0])
            if joueur:
                return [joueur, [(1,0), (2,1), (3,0)]]
            
            joueur = self.compare(self.plateau[1][2], self.plateau[2][2], self.plateau[3][2])
            if joueur:
                return [joueur, [(1,2), (2,2), (3,2)]]
            
            joueur = self.compare(self.plateau[0][2], self.plateau[2][3], self.plateau[4][2])
            if joueur:
                return [joueur, [(0,2), (2,3), (4,2)]]

        else :
            for coords in config.CoordMoulinColnnePlateau1 :
                tmp = list()
                for coord in coords :
                    tmp.append( self.plateau[coord[0]][coord[1]] )
                
                joueur = self.compare(tmp[0], tmp[1], tmp[2])
                if joueur:
                    return [joueur, coords]

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

    def dejavu(self, indices:list, joueur:int) :
        for i in indices :
            self.joue(i, joueur*-1)

    def affiche(self) :
        pprint(self.plateau)
        print("\n")
