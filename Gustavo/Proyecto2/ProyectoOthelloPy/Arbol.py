import Tablero
class Node(object):
    def __init__(self, name, tablero): #TODO: ver si hay que pasar profundidad
        self.name = name
        self.tablero = tablero
        self.children = []
    #def add_child(self, obj):
#        self.children.append(obj)
    def generaHijos(self):
        tablerosHijos  = value.tiradasPosibles()
        for i,j in tablerosHijos:
	    #ver si la sintaxis esta bien
            self.children.append(n= Nodo(tablero.setFicha(i,j)))
