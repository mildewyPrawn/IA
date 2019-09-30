#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Arbol
import Tablero

''' Algoritmo para calcular el minimax '''
def minmax(node, depth, maximizingPlayer):
    valor =  []
    j=0
    decision=-1
    node.generaHijos();
    #if maximizingPlayer:

    for nodo in node.children:
        valor.append(minimax1(nodo, depth-1, False))
        i=float("-inf")
        for v in valor:
            if v>i:
                decision=j
                i=v
            j = j + 1
    #else: minimizingPlayer
        #for nodo in node.children:
           # valor.append(minimax(nodo, sub(depth, 1), True)))
#        i=float("inf")
  #      for v in valor:
   #         if v<i:
    #            decision=j
     #           i=v
      #      j++
            #el Return hay que modificar.
    return node.children[decision],node.children[decision].difTablero(nodo.tablero)

def minimax1(node, depth, maximizingPlayer):
    if depth == 0 or node.tablero.esTableroFinal():
        return heuristica(node.value)
    node.generaHijos();
    if maximizingPlayer:
        valor = float("-inf")
        for nodo in node.children:
            valor = max(valor, minimax1(nodo, sub(depth, 1), False))
        return valor
    else: #minimizingPlayer
        valor = float("inf")
        for nodo in node.children:
            valor = min(valor, minimax(nodo, sub(depth, 1), True))
        return valor

''' Heuristica utilizada para definir la siguiente jugada '''
def heuristica(tablero, negras):
    tab = [[0 for i in range(tablero.dimension)] for j in range(tablero.dimension)]
    for i in range(tablero.dimension):
           for j in range(tablero.dimension):
               if i ==0 or i==tablero.dimension-1 or  j ==0 or j==tablero.dimension-1 :
                   if i ==0 and j ==0:
                       tab[i][j]=20
                   elif  i ==0 and j ==tablero.dimension-1:
                       tab[i][j]=20
                   elif i ==tablero.dimension-1 and j ==tablero.dimension-1:
                       tab[i][j]=20
                   elif i ==tablero.dimension-1 and j ==0:
                       tab[i][j]=20
                   elif i == 1 or j==1 or i ==tablero.dimension-2 or j ==tablero.dimension-2:
                       tab[i][j]=2
                   else:
                       tab[i][j]=10
               elif i ==1 or i==tablero.dimension-2 or  j ==1 or j==tablero.dimension-2:
                   if i ==1 and j==tablero.dimension-2:
                       tab[i][j]=-20
                   elif i ==tablero.dimension-2 and j==tablero.dimension-2:
                       tab[i][j]=-20
                   elif i ==1 and j==1:
                       tab[i][j]=-20
                   elif i ==tablero.dimension-2 and j == 1:
                       tab[i][j]=-20
                   else:
                       tab[i][j]=1
               elif i==2 or j==2 or i==tablero.dimension-3 or j==tablero.dimension-3:
                   if i==2 and j==2 :
                       tab[i][j]=10
                   elif i==2 and j==tablero.dimension-3:
                       tab[i][j]=10
                   elif i==tablero.dimension and j == tablero.dimension:
                       tab[i][j]=10
                   elif i==tablero.dimension and j == 2:
                       tab[i][j]=10
                   else:
                       tab[i][j]=4
               else:
                   tab[i][j]=3
    h=0
    for i in range(tablero.dimension):
            for j in range(tablero.dimension):
                if negras:
                    if tablero[i][j]== 1:
                        h+=tab[i][j]
                    elif tablero[i][j]== 2:
                        h-=tab[i][j]
                else:
                    if tablero[i][j]== 1:
                        h-=tab[i][j]
                    elif tablero[i][j]== 2:
                        h+=tab[i][j]
    return h
