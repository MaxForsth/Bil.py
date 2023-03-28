#skapade en klass
class bil:

    #construktor
    def __init__ (self, fabrikat, color, lager):
        self.fabrikat = fabrikat
        self.color = color
        self.lager = lager

    def setFabrikat (self, fabrikat):
        self.fabrikat = fabrikat

    def getFabrikat (self):
        return self.fabrikat
    


    def setColor (self, color):
        self.color = color

    def getColor (self):
        return self.color