''' Proyecto base para el juego de Othello/Reversi
:author: Rodrigo Colin
'''

from Agente import *
from Tablero import *
import os

cantidadJugadores = 1 #TODO: esto se deberia setear cuando se elige en la pantalla

dificultad = int(os.environ['DIFICULTAD'])%3
color = int(os.environ['COLOR'])%2

tablero = Tablero()
agente = Agente(2) #TODO: debería recibir el nivel de dificultad

def settings():
    ''' Metodo para establecer tamano de ventana al incluir variables '''
    size(tablero.dimension * tablero.tamCasilla, tablero.dimension * tablero.tamCasilla)

def setup():
    ''' Inicializaciones '''
    println("Proyecto base para el juego de mesa Othello")

def draw():
    ''' Ciclo de dibujado '''
    tablero.display()
    jugar()

def jugar():
  if cantidadJugadores == 0:
    ceroJugadores()

  elif cantidadJugadores == 1:
    unJugador()

  elif cantidadJugadores == 2:
    dosJugadores()

#TODO: probar este cuando tengamos heuristica que funcione
def ceroJugadores():
  coord = agente.jugar(tablero)
  jugadaTerminada = tablero.setFicha(coord[0], coord[1])
  if jugadaTerminada:
    tablero.cambiarTurno()

#TODO: probar este cuando tengamos heuristica que funcione
def unJugador():
  if tablero.turno: #Juega el jugador de ficha color negro
    if mousePressed:
      println("\nClic en la casilla " + "[" + str(mouseX/tablero.tamCasilla) + ", " + str(mouseY/tablero.tamCasilla) + "]")
      jugadaTerminada = tablero.setFicha(mouseX/tablero.tamCasilla, mouseY/tablero.tamCasilla)
      if jugadaTerminada:
        tablero.cambiarTurno()
  else: #Juega el jugador de ficha color blanco
    posX, posY = agente.jugar(tablero)
    jugadaTerminada = tablero.setFicha(posX, posY)
    if jugadaTerminada:
      tablero.cambiarTurno()

#TODO: ver que pasa cuando no hay jugadas disponibles
def dosJugadores():
  if tablero.turno: #Juega el jugador de ficha color negro
    if mousePressed:
      println("\nClic en la casilla " + "[" + str(mouseX/tablero.tamCasilla) + ", " + str(mouseY/tablero.tamCasilla) + "]")
      jugadaTerminada = tablero.setFicha(mouseX/tablero.tamCasilla, mouseY/tablero.tamCasilla)
      if jugadaTerminada:
        tablero.cambiarTurno()
  else: #Juega el jugador de ficha color blanco
    if mousePressed:
      println("\nClic en la casilla " + "[" + str(mouseX/tablero.tamCasilla) + ", " + str(mouseY/tablero.tamCasilla) + "]")
      jugadaTerminada = tablero.setFicha(mouseX/tablero.tamCasilla, mouseY/tablero.tamCasilla)
      if jugadaTerminada:
        tablero.cambiarTurno()
