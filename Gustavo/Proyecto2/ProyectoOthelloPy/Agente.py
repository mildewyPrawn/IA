import Arbol
import Tablero

''' Definicion de un agente para jugar Othello '''
class Agente:

    ''' Constructor base de un agente
    :param competitibidad: Nivel de competitibidad que tiene el agente
    :type competitibidad: int
    '''
    def __init__(self, competitibidad):
        self.competitibidad = competitibidad

    ''' Devuelve coordenada en la cual jugar la ficha '''
    def jugar(self, tablero):
        nodo("hola", tablero) #TODO: creo que no es necesario el nombre, ver en clase arbol
        coord = minmax(nodo, competitibidad, True)
        return coord
    #TODO: aca hay que llamar a minimax
