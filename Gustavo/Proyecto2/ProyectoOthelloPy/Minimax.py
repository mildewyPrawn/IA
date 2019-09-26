#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Arbol
import Tablero

def minimax(node, depth, maximizingPlayer):
    if depth == 0 or node.value.esTableroFinal():
        return heuristica(node.value)
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
