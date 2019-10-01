class Tablero:
    ''' Definicion de un tablero para el juego de Othello '''
    def __init__(self, dimension=8, tamCasilla=60):
        ''' Constructor base de un tablero
        :param dimension: Cantidad de casillas en horizontal y vertical del tablero
        :type dimension: int
        :param tamCasilla: El tamano en pixeles de cada casilla cuadrada del tablero
        :type tamCasilla: int
        '''
        self.dimension = dimension
        self.tamCasilla = tamCasilla
        self.turno = True # Representa de quien es el turno bajo la siguiente convencion: true = jugador 1, false = jugador 2
        self.numeroDeTurno = 0 # Contador de la cantidad de turnos en el tablero
        self.mundo = [[0 for i in range(self.dimension)] for j in range(self.dimension)] # Representacion logica del tablero. Cada numero representa: 0 = vacio, 1 = ficha jugador1, 2 = ficha jugador 2
        # Configuracion inicial (colocar 4 fichas al centro del tablero):
        self.mundo[(self.dimension/2)-1][self.dimension/2] = 1
        self.mundo[self.dimension/2][(self.dimension/2)-1] = 1
        self.mundo[(self.dimension/2)-1][(self.dimension/2)-1] = 2
        self.mundo[self.dimension/2][self.dimension/2] = 2

    def display(self):
        ''' Dibuja en pantalla el tablero, es decir, dibuja las casillas y las fichas de los jugadores '''

        background(204)
        if (mouseX < 33):
            rect(0, 0, 33, 100) # Left
            fill(0,255,0)
        elif (mouseX < 66):
            rect(33, 0, 33, 100) # Middle
            fill(250,150,50)
        else:
            rect(66, 0, 33, 100) #Right
            fill(255,0,0)


        fondo = color(63, 221, 24) # El color del fondo del tablero
        linea = color(0) # El color de linea del tablero
        grosor = 2 # Ancho de linea (en pixeles)
        jugador1 = color(0) # Color de ficha para el primer jugador
        jugador2 = color(255) # Color de ficha para el segundo jugador

        # Doble iteracion para recorrer cada casilla del tablero
        for i in range(self.dimension):
            for j in range(self.dimension):
                # Dibujar cada casilla del tablero:
                fill(fondo)
                stroke(linea)
                strokeWeight(grosor)
                rect(i*self.tamCasilla, j*self.tamCasilla, self.tamCasilla, self.tamCasilla)
                # Dibujar las fichas de los jugadores:
                if not self.mundo[i][j] == 0 and (self.mundo[i][j] == 1 or self.mundo[i][j] == 2): # en caso de que la casilla no este vacia
                    fill(jugador1 if self.mundo[i][j] == 1 else jugador2) # establecer el color de la ficha
                    noStroke() # quitar contorno de linea
                    ellipse(i*self.tamCasilla+(self.tamCasilla/2), j*self.tamCasilla+(self.tamCasilla/2), self.tamCasilla*3/5, self.tamCasilla*3/5)

        posibles = self.tiradasPosibles()
        for i,j in posibles:
            # fill(jugador1 if self.mundo[i][j] == 1 else jugador2) # establecer el color de la ficha
            fill(0,0,255)
            noStroke() # quitar contorno de linea
            ellipse(i*self.tamCasilla+(self.tamCasilla/2), j*self.tamCasilla+(self.tamCasilla/2), self.tamCasilla*3/8, self.tamCasilla*3/8)


    def setFicha(self, posX, posY, turno=None):
        ''' Coloca o establece una ficha en una casilla especifica del tablero.
        Nota: El eje vertical esta invertido y el contador empieza en cero.
        :param posX: Coordenada horizontal de la casilla para establecer la ficha
        :type posX: int
        :param posY: Coordenada vertical de la casilla para establecer la ficha
        :type posY: int
        :param turno: Representa el turno o color de ficha a establecer
        :type turno: bool
        '''

        movimientoRealizado = False

        turno = self.turno if turno is None else turno # permite definir un parametro default que es instancia de la clase (self.turno)
        movValido = not self.estaOcupado(posX, posY) and self.encierraOponente(posX, posY)
        if movValido:

            color = self.getColorJugador(turno)
            self.jugarFicha(posX, posY, color)
            self.cambiarColor(posX, posY, color)
            movimientoRealizado = True

        return movimientoRealizado

    def cambiarTurno(self):
        ''' Representa el cambio de turno. Normalmente representa la ultima accion del turno '''
        self.turno = not self.turno
        self.numeroDeTurno += 1

    def estaOcupado(self, posX, posY):
        ''' Verifica si en la posicion de una casilla dada existe una ficha (sin importar su color)
        :param posX: Coordenada horizontal de la casilla a verificar
        :type posX: int
        :param posY: Coordenada vertical de la casilla a verificar
        :type posY: int
        :returns: True si hay una ficha de cualquier color en la casilla, false en otro caso
        :rtype: bool
        '''
        return self.mundo[posX][posY] != 0

    def cantidadFichas(self):
        ''' Cuenta la cantidad de fichas en el tablero
        :returns: La cantidad de fichas de ambos jugadores en el tablero como vector donde x = jugador 1, y = jugador 2
        :rtype: PVector
        '''
        contador = PVector()
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.mundo[i][j] == 1:
                    contador.x = contador.x + 1
                if self.mundo[i][j] == 2:
                    contador.y = contador.y + 1
        return contador

#################################################################

    ''' Verifica si una posicion encierra a su oponente en alguna de las direcciones posibles
    :param posX: Coordenada horizontal de la casilla a verificar
    :type posX: int
    :param posY: Coordenada vertical de la casilla a verificar
    :type posY: int
    :returns: True si encierra a oponente en alguna direccion, false en otro caso
    :rtype: bool
    '''
    def encierraOponente(self, posX, posY):
        color = self.getColorJugador(self.turno)

        return self.encierraOponenteEnDireccion(color, posX, posY, "horizontalDerecha") or self.encierraOponenteEnDireccion(color, posX, posY, "horizontalIzquierda") or self.encierraOponenteEnDireccion(color, posX, posY, "verticalArriba") or self.encierraOponenteEnDireccion(color, posX, posY, "verticalAbajo") or self.encierraOponenteEnDireccion(color, posX, posY, "diagonalDerAscendente") or self.encierraOponenteEnDireccion(color, posX, posY, "diagonalDerDescendente") or self.encierraOponenteEnDireccion(color, posX, posY, "diagonalIzqAscendente") or self.encierraOponenteEnDireccion(color, posX, posY, "diagonalIzqDescendente")

    ''' Dado un tablero devuelve las posiciones en las cuales se puede jugar una ficha
    :returns: Una lista de coordenadas en las que se pueden jugar fichas
    :rtype: lista de coordenadas
    '''
    def tiradasPosibles(self):
        color = self.getColorJugador(self.turno)

        tiradas = []

        for posX in range(self.dimension):
            for posY in range(self.dimension):
                if not self.estaOcupado(posX,posY) and self.encierraOponente(posX, posY):
                    tiradas.append((posX, posY))
        return tiradas

    ''' Verifica si una posicion esta en el rango del tablero
    :param posX: Coordenada horizontal de la casilla a verificar
    :type posX: int
    :param posY: Coordenada vertical de la casilla a verificar
    :type posY: int
    :returns: True si esta en rango, false en otro caso
    :rtype: bool
    '''
    def posicionValida(self, x, y):
        return 0 <= x < self.dimension and 0 <= y < self.dimension

    ''' Verifica si se encierra oponente en la direccion determinada
    :param color: color que se quiere encerrar
    :type color: int
    :param posX: Coordenada horizontal de la casilla a verificar
    :type posX: int
    :param posY: Coordenada vertical de la casilla a verificar
    :type posY: int
    :param direccion: direccion en la que se quiere encerrar oponente
    :type direccion: string
    :returns: True si encierra oponente en esa direccion, false en otro caso
    :rtype: bool
    '''
    def encierraOponenteEnDireccion(self, color, posX, posY, direccion):
        encierraOponente = False

        if direccion == "horizontalDerecha" and self.posicionValida(posX + 1, posY):
            encierraOponente = self.encierraHorizontalDerecha(posX, posY, color)
        elif direccion == "horizontalIzquierda" and self.posicionValida(posX - 1, posY):
            encierraOponente = self.encierraHorizontalIzquierda(posX, posY, color)
        elif direccion == "verticalArriba" and self.posicionValida(posX, posY - 1):
            encierraOponente = self.encierraVerticalArriba(posX, posY, color)
        elif direccion == "verticalAbajo" and self.posicionValida(posX, posY + 1):
            encierraOponente = self.encierraVerticalAbajo(posX, posY, color)
        elif direccion == "diagonalDerAscendente" and self.posicionValida(posX + 1, posY - 1):
            encierraOponente = self.encierraDiagonalDerAscendente(posX, posY, color)
        elif direccion == "diagonalDerDescendente" and self.posicionValida(posX + 1, posY + 1):
            encierraOponente = self.encierraDiagonalDerDescendente(posX, posY, color)
        elif direccion == "diagonalIzqAscendente" and self.posicionValida(posX - 1, posY - 1):
            encierraOponente = self.encierraDiagonalIzqAscendente(posX, posY, color)
        elif direccion == "diagonalIzqDescendente" and self.posicionValida(posX - 1, posY + 1):
            encierraOponente = self.encierraDiagonalIzqDescendente(posX, posY, color)

        return encierraOponente

    def encierraHorizontalDerecha(self, posX, posY, color):
        return self.esAdyacenteA(posX, posY, 1, 0) and self.encierraOponenteHorizontalRango(posY, color, range(posX + 1, self.dimension))

    def encierraHorizontalIzquierda(self, posX, posY, color):
        return self.esAdyacenteA(posX, posY, -1, 0) and self.encierraOponenteHorizontalRango(posY, color, range(posX - 1, -1, -1))

    def encierraVerticalArriba(self, posX, posY, color):
        return self.esAdyacenteA(posX, posY, 0, -1) and self.encierraOponenteVerticalRango(posX, color, range(posY - 1, -1, -1))

    def encierraVerticalAbajo(self, posX, posY, color):
        return self.esAdyacenteA(posX, posY, 0, 1) and self.encierraOponenteVerticalRango(posX, color, range(posY + 1, self.dimension))

    def encierraDiagonalDerAscendente(self, posX, posY, color):
        return self.esAdyacenteA(posX, posY, 1, -1) and self.encierraOponenteDiagonalRango(color, range(posX + 1, self.dimension), range(posY - 1, -1, -1))

    def encierraDiagonalDerDescendente(self, posX, posY, color):
        return self.esAdyacenteA(posX, posY, 1, 1) and self.encierraOponenteDiagonalRango(color, range(posX + 1, self.dimension), range(posY + 1, self.dimension))

    def encierraDiagonalIzqAscendente(self, posX, posY, color):
        return self.esAdyacenteA(posX, posY, -1, -1) and self.encierraOponenteDiagonalRango(color, range(posX - 1, -1, -1), range(posY - 1, -1, -1))

    def encierraDiagonalIzqDescendente(self, posX, posY, color):
        return self.esAdyacenteA(posX, posY, -1, 1) and self.encierraOponenteDiagonalRango(color, range(posX - 1, -1, -1), range(posY + 1, self.dimension))

    def encierraOponenteHorizontalRango(self, posY, color, rango):
        for i in rango:
            if self.mundo[i][posY] == 0:
                return False
            elif self.mundo[i][posY] == color:
                return True

        return False

    def encierraOponenteVerticalRango(self, posX, color, rango):
        for j in rango:
            if self.mundo[posX][j] == 0:
                return False
            elif self.mundo[posX][j] == color:
                return True

        return False

    def encierraOponenteDiagonalRango(self, color, rangoX, rangoY):
        for i, j in zip(rangoX, rangoY):
            if self.mundo[i][j] == 0:
                return False
            elif self.mundo[i][j] == color:
                return True

        return False

    ''' Verifica si una posicion es adyacente a oponente en una direccion
    :param posX: Coordenada horizontal de la casilla a verificar
    :type posX: int
    :param posY: Coordenada vertical de la casilla a verificar
    :type posY: int
    :param dirX: Direccion en X. 1 para derecha, -1 para izquierda, 0 en el lugar
    :type dirX: int
    :param dirY: Direccion en Y. 1 para arriba, -1 para abajo, 0 en el lugar
    :type dirY: int
    :returns: True si es adyacente a oponente en esa direccion, false en otro caso
    :rtype: bool
    '''
    def esAdyacenteA(self, posX, posY, dirX, dirY):
        colorOponente = self.getColorOponente(self.turno)

        return self.mundo[posX + dirX][posY + dirY] == colorOponente

    '''Devuelve el color de la casilla'''
    def getColorCasilla(self, posX, posY):
        color = 0

        if self.mundo[posX][posY] == 1:
            color = 1
        elif self.mundo[posX][posY] == 2:
            color = 2

        return color

    ''' Devuelve el color del oponente '''
    def getColorOponente(self, turno):
        return 2 if turno else 1

    ''' Devuelve el color del jugador actual '''
    def getColorJugador(self, turno):
        return 1 if turno else 2

    ''' Coloca una ficha del color determinado en el tablero '''
    def jugarFicha(self, posX, posY, color):
        self.mundo[posX][posY] = color

    ''' Cambia de color linea de fichas '''
    def cambiarColor(self, posX, posY, color):
        if self.posicionValida(posX + 1, posY) and self.encierraHorizontalDerecha(posX, posY, color):
            self.cambiarColorHorizontal(posY, range(posX + 1, self.dimension))
        if self.posicionValida(posX - 1, posY) and self.encierraHorizontalIzquierda(posX, posY, color):
            self.cambiarColorHorizontal(posY, range(posX - 1, -1, -1))
        if self.posicionValida(posX, posY - 1) and self.encierraVerticalArriba(posX, posY, color):
            self.cambiarColorVertical(posX, range(posY - 1, -1, -1))
        if self.posicionValida(posX, posY + 1) and self.encierraVerticalAbajo(posX, posY, color):
            self.cambiarColorVertical(posX, range(posY + 1, self.dimension))
        if self.posicionValida(posX + 1, posY - 1) and self.encierraDiagonalDerAscendente(posX, posY, color):
            self.cambiarColorDiagonal(range(posX + 1, self.dimension), range(posY - 1, -1, -1))
        if self.posicionValida(posX + 1, posY + 1) and self.encierraDiagonalDerDescendente(posX, posY, color):
            self.cambiarColorDiagonal(range(posX + 1, self.dimension), range(posY + 1, self.dimension))
        if self.posicionValida(posX - 1, posY - 1) and self.encierraDiagonalIzqAscendente(posX, posY, color):
            self.cambiarColorDiagonal(range(posX - 1, -1, -1), range(posY - 1, -1, -1))
        if self.posicionValida(posX - 1, posY + 1) and self.encierraDiagonalIzqDescendente(posX, posY, color):
            self.cambiarColorDiagonal(range(posX - 1, -1, -1), range(posY + 1, self.dimension))

    def cambiarColorHorizontal(self, posY, rango):
        color = self.getColorJugador(self.turno)

        for i in rango:
            if self.mundo[i][posY] != 0 and self.mundo[i][posY] != color:
                self.mundo[i][posY] = color
            else:
                break #Termina ya que para cambiar color tiene que estar encerrado

    def cambiarColorVertical(self, posX, rango):
        color = self.getColorJugador(self.turno)

        for j in rango:
            if self.mundo[posX][j] != 0 and self.mundo[posX][j] != color:
                self.mundo[posX][j] = color
            else:
                break

    def cambiarColorDiagonal(self, rangoX, rangoY):
        color = self.getColorJugador(self.turno)

        for i, j in zip(rangoX, rangoY):
            if self.mundo[i][j] != 0 and self.mundo[i][j] != color:
                self.mundo[i][j] = color
            else:
                break

    ''' Determina si es un tablero en el que no se pueden realizar movimientos '''
    def esTableroFinal(self):
        return self.tiradasPosibles() == []

    def tableroConSetFicha(self, posX, posY):
        tablero = self.copyTablero()

        movValido = tablero.setFicha(posX, posY)
        if movValido:
            return tablero
        else:
            return None

    '''Realiza una copia del tablero'''
    def copyTablero(self):
        tablero = Tablero(self.dimension, self.tamCasilla)

        tablero.turno = self.turno # Representa de quien es el turno bajo la siguiente convencion: true = jugador 1, false = jugador 2
        tablero.numeroDeTurno = self.numeroDeTurno

        for i in range(self.dimension):
            for j in range(self.dimension):
                tablero.mundo[i][j] = self.mundo[i][j]

        return tablero

    def difTablero(self, tablero2):
        coord = (-1, -1)
        for posX in range(tablero2.dimension):
            for posY in range(tablero2.dimension):
                if self.mundo[posX][posY] == 0 and self.mundo[posX][posY] != tablero2.mundo[posX][posY]:
                    coord = (posX, posY)
        return coord
