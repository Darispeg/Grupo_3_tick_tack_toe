class Nodo:
    # Constructos de la Clase
    def __init__(self, item, hijos=None, padre=None):
        self.item = item
        self.padre = None
        self.hijos = []

    def getItem(self):
        return self.item

    def setItem(self, item):
        self.item = item

    def getHijos(self):
        return self.hijos

    def setHijos(self, hijo):
        self.hijos = hijo

    def getPadre(self):
        return self.padre

    def setPadre(self, padre):
        self.padre = padre

    def esHoja(self):
        return len(self.hijos) == 0

    def addHijos(self, h):
        self.hijos.append(h)

    # Para Imprimir en la Consola
    # def __str__(self):
    #     return "Nodo{item=" + str(self.item) + ", hijos=" + str(self.hijos) + ", padre=" + str(self.padre) + '}'

    def __str__(self):
        return str(self.item)


