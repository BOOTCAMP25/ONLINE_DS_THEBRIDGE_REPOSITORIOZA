import os
import time
import pprint

from funcioneshlf import *
from variableshlf import *

# Juego principal
'''Llamadas a las funciones para su ejecucion'''
tablero_jugador = crear_tablero(tamaño)
tablero_computadora = crear_tablero(tamaño)
tablero_visible = crear_tablero(tamaño)
colocar_barcos(tablero_computadora, tamaño_barco)

print("¡Bienvenido a Hundir la Flota!")
time.sleep(2)
pprint.pprint(tablero_jugador)
while True:
    fila = int(input("Introduce la fila (0-9): "))
    columna = int(input("Introduce la columna (0-9): "))
    if atacar(tablero_computadora,tablero_visible, fila, columna):
        print("¡Tocado!")
    else:
        print("¡Agua!")
    time.sleep(1)
    os.system("cls")
    pprint.pprint(tablero_visible)
        
    if all(celda != 'B' for fila in tablero_computadora for celda in fila):
        print("¡Has hundido todos los barcos!")
        break
