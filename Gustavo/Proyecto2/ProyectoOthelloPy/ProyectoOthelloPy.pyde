''' Proyecto base para el juego de Othello/Reversi
:author: Rodrigo Colin
'''
from Tablero import *
tablero = Tablero()

def settings():
    ''' Metodo para establecer tamano de ventana al incluir variables '''
    size(tablero.dimension * tablero.tamCasilla, tablero.dimension * tablero.tamCasilla)

def setup():
    ''' Inicializaciones '''
    println("Proyecto base para el juego de mesa Othello")

def draw():
    ''' Ciclo de dibujado '''
    tablero.display()

def mousePressed():
    ''' Evento para detectar cuando el usuario da clic '''
    println("\nClic en la casilla " + "[" + str(mouseX/tablero.tamCasilla) + ", " + str(mouseY/tablero.tamCasilla) + "]")
    if not tablero.estaOcupado(mouseX/tablero.tamCasilla, mouseY/tablero.tamCasilla):
        jugadaTerminada = tablero.setFicha(mouseX/tablero.tamCasilla, mouseY/tablero.tamCasilla)
        if jugadaTerminada:
          tablero.cambiarTurno()
          print ("voy a imprimirlas jugadas posibles")
          tableroP = tablero.tiradasPosibles() #TODO
          print (tableroP)
          print '[Turno # {!s}] {} (Score {!s} - {!s})'.format(tablero.numeroDeTurno, 'jugo ficha blanca' if tablero.turno else 'jugo ficha negra', int(tablero.cantidadFichas().x), int(tablero.cantidadFichas().y))
