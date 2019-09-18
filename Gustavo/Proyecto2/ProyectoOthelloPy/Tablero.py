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
        turno = self.turno if turno is None else turno # permite definir un parametro default que es instancia de la clase (self.turno)
        movValido = self.encierraOponente(posX, posY)
        if movValido:

            color = self.getColorJugador(turno)
            self.jugarFicha(posX, posY, color)

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

#TODO: este comportamiento podria ir en clase aparte ################################################################

    #TODO: deberian ser un enumerado en lugar de string
    def encierraOponente(self, posX, posY):
        color = self.getColorJugador(self.turno)

        return self.encierraOponenteEnDireccion(color, posX, posY, "horizontalDerecha") or self.encierraOponenteEnDireccion(color, posX, posY, "horizontalIzquierda") or self.encierraOponenteEnDireccion(color, posX, posY, "verticalArriba") or self.encierraOponenteEnDireccion(color, posX, posY, "verticalAbajo") or self.encierraOponenteEnDireccion(color, posX, posY, "diagonalDerAscendente") or self.encierraOponenteEnDireccion(color, posX, posY, "diagonalDerDescendente") or self.encierraOponenteEnDireccion(color, posX, posY, "diagonalIzqAscendente") or self.encierraOponenteEnDireccion(color, posX, posY, "diagonalIzqDescendente")

    def posicionValida(self, x, y):
        return 0 <= x < self.dimension and 0 <= y < self.dimension

    def encierraOponenteEnDireccion(self, color, posX, posY, direccion):
        encierraOponente = False

        if direccion == "horizontalDerecha" and self.posicionValida(posX + 1, posY):
            encierraOponente = self.esAdyacenteA(posX, posY, 1, 0) and self.encierraOponenteHorizontalRango(posY, color, range(posX + 1, self.dimension))
        elif direccion == "horizontalIzquierda" and self.posicionValida(posX - 1, posY):
            encierraOponente = self.esAdyacenteA(posX, posY, -1, 0) and self.encierraOponenteHorizontalRango(posY, color, range(posX - 1, -1, -1))
        elif direccion == "verticalArriba" and self.posicionValida(posX, posY - 1):
            encierraOponente = self.esAdyacenteA(posX, posY, 0, -1) and self.encierraOponenteVerticalRango(posX, color, range(posY - 1, -1, -1))
        elif direccion == "verticalAbajo" and self.posicionValida(posX, posY + 1):
            encierraOponente = self.esAdyacenteA(posX, posY, 0, 1) and self.encierraOponenteVerticalRango(posX, color, range(posY + 1, self.dimension))
        elif direccion == "diagonalDerAscendente" and self.posicionValida(posX + 1, posY - 1):
            encierraOponente = self.esAdyacenteA(posX, posY, 1, -1) and self.encierraOponenteDiagonalRango(color, range(posX + 1, self.dimension), range(posY - 1, -1, -1))
        elif direccion == "diagonalDerDescendente" and self.posicionValida(posX + 1, posY + 1):
            encierraOponente = self.esAdyacenteA(posX, posY, 1, 1) and self.encierraOponenteDiagonalRango(color, range(posX + 1, self.dimension), range(posY + 1, self.dimension))
        elif direccion == "diagonalIzqAscendente" and self.posicionValida(posX - 1, posY - 1):
            encierraOponente = self.esAdyacenteA(posX, posY, -1, -1) and self.encierraOponenteDiagonalRango(color, range(posX - 1, -1, -1), range(posY - 1, -1, -1))
        elif direccion == "diagonalIzqDescendente" and self.posicionValida(posX - 1, posY + 1):
            encierraOponente = self.esAdyacenteA(posX, posY, -1, 1) and self.encierraOponenteDiagonalRango(color, range(posX - 1, -1, -1), range(posY + 1, self.dimension))

        return encierraOponente

    def esAdyacenteA(self, posX, posY, dirX, dirY):
        colorOponente = self.getColorOponente(self.turno)

        return self.mundo[posX + dirX][posY + dirY] == colorOponente

    def encierraOponenteHorizontalRango(self, posY, color, rango):
        for i in rango: #TODO: ver si esta bien el rango
            if self.mundo[i][posY] == 0:
                return False
            elif self.mundo[i][posY] == color:
                return True

        return False

    def encierraOponenteVerticalRango(self, posX, color, rango):
        for j in rango: #TODO: ver si esta bien el rango
            if self.mundo[posX][j] == 0:
                return False
            elif self.mundo[posX][j] == color:
                return True

        return False

    def encierraOponenteDiagonalRango(self, color, rangoX, rangoY):
        for i, j in zip(rangoX, rangoY): #TODO: ver si esta bien el rangoX
            if self.mundo[i][j] == 0:
                return False
            elif self.mundo[i][j] == color:
                return True

        return False

    def getColorOponente(self, turno):
        return 2 if turno else 1

    def getColorJugador(self, turno):
        return 1 if turno else 2

    def jugarFicha(self, posX, posY, color):
        self.mundo[posX][posY] = color

    #def cambioColor(self, posX, posY, color):
