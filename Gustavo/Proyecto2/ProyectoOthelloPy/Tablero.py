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
        movValido = self.validarMovimiento(posX, posY, turno)
        if movValido:

            #self.mundo[posX][posY] = 1 if turno else 2
            color = self.getColorJugador(turno)
            self.jugarFicha(posX, posY, color)
            self.cambioColor(posX, posY, color)

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

    def validarMovimiento(self, posX, posY, turno):
        esAdyacente = self.esAdyacenteAOponente(posX, posY, turno)
        encierraOponente = self.encierraOponente(posX, posY, turno)
        return esAdyacente and encierraOponente

    def esAdyacenteAOponente(self, posX, posY, turno):
        colorOponente = self.getColorOponente(turno)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.mundo[posX + i][posY + j] == colorOponente:
                    return True

        return False

    def encierraOponente(self, posX, posY, turno):
        color = self.getColorJugador(turno)

        horizontal = self.encierraOponenteHorizontal(posX, posY, color)
        vertical = self.encierraOponenteVertical(posX, posY, color)
        diagonal = self.encierraOponenteDiagonal(posX, posY, color)

        return horizontal or vertical or diagonal

    def encierraOponenteHorizontal(self, posX, posY, color):
        encierraHaciaDerecha = self.encierraOponenteHorizontalRango(posY, color, range(posX, self.dimension))
        encierraHaciaIzquierda = self.encierraOponenteHorizontalRango(posY, color, range(posX, 1, -1))

        return encierraHaciaDerecha or encierraHaciaIzquierda

    def encierraOponenteHorizontalRango(self, posY, color, rango):
        for i in rango: #TODO: ver si esta bien el rango
            if self.mundo[i][posY] == color:
                return True

        return False

    def encierraOponenteVertical(self, posX, posY, color):
        encierraHaciaArriba = self.encierraOponenteVerticalRango(posX, color, range(posY, self.dimension))
        encierraHaciaAbajo = self.encierraOponenteVerticalRango(posX, color, range(posY, 1, -1))

        return encierraHaciaArriba or encierraHaciaAbajo

    def encierraOponenteVerticalRango(self, posX, color, rango):
        for j in rango: #TODO: ver si esta bien el rango
            if self.mundo[posX][j] == color:
                return True

        return False

    def encierraOponenteDiagonal(self, posX, posY, color):
        encierraAscendente = self.encierraOponenteDiagonalRango(color, range(posX, self.dimension), range(posY, self.dimension))
        encierraDescendente = self.encierraOponenteDiagonalRango(color, range(posX, 1, -1), range(posY, 1, -1))

        return encierraAscendente or encierraDescendente

    def encierraOponenteDiagonalRango(self, color, rangoX, rangoY):
        for i, j in zip(rangoX, rangoY): #TODO: ver si esta bien el rango
            if self.mundo[i][j] == color:
                return True

        return False

    def getColorOponente(self, turno):
        return 2 if turno else 1


    def getColorJugador(self, turno):
        return 1 if turno else 2

    def jugarFicha(self, posX, posY, color):
        self.mundo[posX][posY] = color

    #def cambioColor(self, posX, posY, color):
