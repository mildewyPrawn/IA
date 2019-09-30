import Tablero

''' Definicion de un arbol '''
class Node(object):

    ''' Constructor base de un arbol
    :param name: nombre del nodo #TODO: creo que este no es necesario
    :type nombre: string
    :param tablero: tablero sobre el que se define la siguiente jugada
    :type nombre: Tablero
    '''
    def __init__(self, name, tablero): #TODO: ver si hay que pasar profundidad
        self.name = name
        self.tablero = tablero
        self.children = []
    #def add_child(self, obj):
#        self.children.append(obj)

    ''' Genera los tableros resultado de jugar fichas en posiciones validas '''
    def generaHijos(self):
        tablerosHijos  = self.tablero.tiradasPosibles()
        for i,j in tablerosHijos:
            #TODO: hacer el cambio de tablero afuera
            tablero = self.tablero.tableroConSetFicha(i, j)
            self.children.append(Node("hola", tablero)) #TODO: creo que el nombre hay que sacarlo
