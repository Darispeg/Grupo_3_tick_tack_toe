#Cambios realizados por Dennis
#09/10/2020
import random

class Nodo:
    def __init__(self, accion, hijos=None):
        self.accion = accion
        self.hijos = None
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)
    
    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos is not None:
            for h in self.hijos:
                h.padre = self

    def get_hijos(self):
        return self.hijos
    
    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_ACCION(self,accion):
        self.accion = accion

    def ACCIONES(self):
        acciones = []
        for accion in self.get_hijos:
            acciones.append(accion)
        return acciones

    def set_utilidad(self, coste):
        self.coste = coste
    
    def UTILIDAD(self):
        return self.coste

    def funcion_Prueba_Git(self):
        return None

    def Prueba_Git(self):
        return None


