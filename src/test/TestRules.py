import math

tablero=[' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  #Nuestro tablero inicalmente serán nueva callisas vacias
casillasVacias=[]
TABLERO_FILAS=3
TABLERO_COLUMNAS=3


def colocarFicha(ficha, fila, columna):
    """
    >>> colocarFicha('X', 1, 2)
    La casilla esta ocupada
    [1, 'X']

    >>> colocarFicha('X', 2, 1)
    [3, 'X']

    """
    while True:
        # fila=numero("Fila entre [1 y 3]: ", 1,3)-1 #Restamos uno ya que nuestro rango real está entre 0 y 2
        fila = fila - 1
        # columna=numero("Columna entre [1 y 3]: ",1,3)-1
        columna = columna - 1
        #Como mi tablero es de 3x3
        casilla=fila*TABLERO_COLUMNAS+columna
        if(tablero[casilla]!=' '):
            #Esa casilla ya está cubierta
            print("La casilla esta ocupada")
            return [casilla, ficha]
        else:
            tablero[casilla] = ficha
            return [casilla, ficha]



def numeroHermanos(casilla, ficha, v, h, tablero):
    """
    # Tablero
    ## X   O   O
    ## O  [ ]  X
    ## X  [ ]  X

    # Columnas
        ## Atras
    >>> numeroHermanos(4, 'X', 0, -1, ['X','O','O','O',' ','X','X',' ','X'])
    1

        ## Adelante
    >>> numeroHermanos(4, 'X', 0, 1, ['X','O','O','O',' ','X','X',' ','X'])
    1

    # Filas
        ## Atras
    >>> numeroHermanos(7, 'X', -1, 0, ['X','O','O','O',' ','X','X',' ','X'])
    0

        ## Adelante
    >>> numeroHermanos(7, 'X', 1, 0, ['X','O','O','O',' ','X','X',' ','X'])
    0

    # Diagonal ( / )
        ## Atras
    >>> numeroHermanos(4, 'X', -1,-1, ['X','O','O','O',' ','X','X',' ','X'])
    0

        ## Adelante
    >>> numeroHermanos(4, 'X', -1, 1, ['X','O','O','O',' ','X','X',' ','X'])
    0

    # Diagonal (`\`)
        ## Atras
    >>> numeroHermanos(4, 'X', -1, -1, ['X','O','O','O',' ','X','X',' ','X'])
    0

        ## Adelante
    >>> numeroHermanos(4, 'X', 1, 1, ['X','O','O','O',' ','X','X',' ','X'])
    0


    """
    f = math.floor(casilla/TABLERO_COLUMNAS) #Obtengo la fila
    c = casilla % TABLERO_COLUMNAS #columna
    fila_nueva = f + v
    if(fila_nueva < 0 or fila_nueva >= TABLERO_FILAS):
        return 0
    columna_nueva= c + h
    if(columna_nueva < 0 or columna_nueva >= TABLERO_COLUMNAS):
        return 0
    #No estamos en el limite así que
    #calculamos la nueva posición y vemos si hay la misma ficha
    pos=(fila_nueva*TABLERO_COLUMNAS + columna_nueva)
    if(tablero[pos] != ficha):
        return 0
    else:
        return 1 + numeroHermanos(pos, ficha, v, h, tablero)



import doctest

doctest.testmod()