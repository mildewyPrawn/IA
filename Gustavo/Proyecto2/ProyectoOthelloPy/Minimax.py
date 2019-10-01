#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Arbol
import Tablero

''' Algoritmo para calcular el minimax '''
def minmax(node, depth, maximizingPlayer):
    valor =  []

    node.children = node.generaHijos()

    for nodo in node.children:
        valor.append(minimax1(nodo, depth-1,not maximizingPlayer))
        max=float("-inf")
    decision=-1
    j = 0
    for v in valor:
        if v > max:
            decision = j
            max = v
        j = j + 1
    return node.tablero.difTablero(node.children[decision].tablero)

def minimax1(node, depth, maximizingPlayer):
    if depth == 0 or node.tablero.esTableroFinal():
        return heuristica(node.tablero, maximizingPlayer)
    node.children = node.generaHijos();
    if maximizingPlayer:
        valor = float("-inf")
        for nodo in node.children:
            valor = max(valor, minimax1(nodo, depth - 1, not maximizingPlayer))
        return valor
    else: #minimizingPlayer
        valor = float("inf")
        for nodo in node.children:
            valor = min(valor, minimax1(nodo, depth - 1, not maximizingPlayer))

        return valor

''' Heuristica utilizada para definir la siguiente jugada '''
def heuristica(tablero, negras):
    tab = [[0 for i in range(tablero.dimension)] for j in range(tablero.dimension)]
    for i in range(tablero.dimension):
           for j in range(tablero.dimension):
               if i ==0 or i==tablero.dimension-1 or  j ==0 or j==tablero.dimension-1 :
                   if i ==0 and j ==0:
                       tab[i][j]=2000
                   elif  i ==0 and j ==tablero.dimension-1:
                       tab[i][j]=2000
                   elif i ==tablero.dimension-1 and j ==tablero.dimension-1:
                       tab[i][j]=2000
                   elif i ==tablero.dimension-1 and j ==0:
                       tab[i][j]=2000
                   elif i == 1 or j==1 or i ==tablero.dimension-2 or j ==tablero.dimension-2:
                       tab[i][j]=200
                   else:
                       tab[i][j]=100
               elif i ==1 or i==tablero.dimension-2 or  j ==1 or j==tablero.dimension-2:
                   if i ==1 and j==tablero.dimension-2:
                       tab[i][j]=-2000
                   elif i ==tablero.dimension-2 and j==tablero.dimension-2:
                       tab[i][j]=-2000
                   elif i ==1 and j==1:
                       tab[i][j]=-2000
                   elif i ==tablero.dimension-2 and j == 1:
                       tab[i][j]=-2000
                   else:
                       tab[i][j]=100
               elif i==2 or j==2 or i==tablero.dimension-3 or j==tablero.dimension-3:
                   if i==2 and j==2 :
                       tab[i][j]=100
                   elif i==2 and j==tablero.dimension-3:
                       tab[i][j]=100
                   elif i==tablero.dimension and j == tablero.dimension:
                       tab[i][j]=100
                   elif i==tablero.dimension and j == 2:
                       tab[i][j]=100
                   else:
                       tab[i][j]=400
               else:
                   tab[i][j]=300
    h=0
    for i in range(tablero.dimension):
            for j in range(tablero.dimension):
                if negras:
                    if tablero.getColorCasilla(i,j) == 1:
                        h+=tab[i][j]
                    elif tablero.getColorCasilla(i,j) == 2:
                        h-=tab[i][j]
                else:
                    if tablero.getColorCasilla(i,j) == 1:
                        h-=tab[i][j]
                    elif tablero.getColorCasilla(i,j) == 2:
                        h+=tab[i][j]
    return h
