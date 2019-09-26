#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Arbol
import Tablero
#Metodo auxiliar que 
def minmax(node, depth, maximizingPlayer):
     valor =  []
     j=0
     desicion=-1
     node.generaHijos();
    #if maximizingPlayer:
       
    for nodo in node.children:
        valor.append(minimax1(nodo, sub(depth, 1), False))
        i=float("-inf")
        for v in valor:
            if v>i:
                decision=j
                i=v
            j++
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
    return (node.children[decision],node.children[decision].difTablero(nodo.value)
    
            
        


            
def minimax1(node, depth, maximizingPlayer):
    if depth == 0 or node.value.esTableroFinal():
        return heuristica(node.value)
    node.generaHijos();
    if maximizingPlayer:
        valor = float("-inf")
        for nodo in node.children:
            valor = max(valor, minimax(nodo, sub(depth, 1), False))
        return valor
    else: #minimizingPlayer
        valor = float("inf")
        for nodo in node.children:
            valor = min(valor, minimax(nodo, sub(depth, 1), True))
        return valor

    #TODO: completar
def heuristica(tablero):
    return 1
