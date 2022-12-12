import fltk


class Rectangle:

    def __init__(self,ax,ay,bx,by,epaisseur:int):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by

        self.epaisseur = epaisseur

        rectangle(ax,ay,bx,by,epaisseur)


    def getTopLeftBorder(self):
        return self.by
    def getTopRightBorder(self):
        return self.bx

    def getBotRightBorder(self):
        return self.by

