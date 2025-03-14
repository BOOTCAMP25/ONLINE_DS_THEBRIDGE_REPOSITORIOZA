import random
import pprint

# Crear el tablero
def crear_tablero(tamaño):
    '''Crea el tablero con el tamaño de celdas asignado'''
    return [['~' for _ in range(tamaño)] for _ in range(tamaño)]

# Imprimir el tablero
def imprimir_tablero(tablero):
    '''Imprime el tablero con funcion join '''
    for fila in tablero:
        print(' '.join(fila))

# Colocar barcos en el tablero
'''Coloca los barcos en el tablero con orientacion horizontal y vertical'''
def colocar_barcos(tablero, tamaño_barco):
    tamaño = len(tablero)
    for _ in range(tamaño_barco):
        barco_colocado = False
        while not barco_colocado:
            orientacion = random.choice(['H', 'V'])
            fila = random.randint(0, tamaño - 1)
            columna = random.randint(0, tamaño - 1)
            if orientacion == 'H' and columna + tamaño_barco <= tamaño:
                if all(tablero[fila][columna + i] == '~' for i in range(tamaño_barco)):
                    for i in range(tamaño_barco):
                        tablero[fila][columna + i] = 'B'
                    barco_colocado = True
            elif orientacion == 'V' and fila + tamaño_barco <= tamaño:
                if all(tablero[fila + i][columna] == '~' for i in range(tamaño_barco)):
                    for i in range(tamaño_barco):
                        tablero[fila + i][columna] = 'B'
                    barco_colocado = True

# Atacar una posición en el tablero
def atacar(tablero,tablero_visible,fila, columna):
    if tablero[fila][columna] == 'B':
        tablero[fila][columna] = 'X'
        tablero_visible [fila][columna] = 'X'
        return True
    elif tablero[fila][columna] == '~':
        tablero[fila][columna] = 'O'
        tablero_visible [fila][columna] = 'O'
        return False

