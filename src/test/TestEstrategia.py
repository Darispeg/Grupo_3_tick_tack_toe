def laOpcion(tablero, casillasVacias, ficha, juegaOponente, nivelMaximo=5, casillas_probar=9, mejor=True):

    """
    # Tablero
    ## X   O   O
    ## O  [ ]  X
    ## X  [ ]  X
    
    >>> laOpcion(['X','O','O','O',' ','X','X',' ','X'], [4,7], 'O', False)
    4


    # Tablero 2
    ## X  [ ]  O
    ## O  [ ] [ ]
    ## [ ][ ]  X
    >>> laOpcion(['X',' ','O','O',' ',' ',' ',' ','X'], [1,4,5,6,7], 'X', False)
    7

    """

    fichaOponente="X" if ficha=="O" else "O"
    # Filas
    for f in range(3):
        mia=0
        oponente=0
        fila=f*3
        posiblesCasillas=[]
        for c in range(3):
            casilla=fila+c
            if(tablero[casilla]==ficha):
                mia+=1
            else:
                if(tablero[casilla]==fichaOponente):
                    oponente+=1
                else:
                    posiblesCasillas.append(casilla)
        #mia=mia/3
        #oponente=oponente/3
        if(oponente>mia and len(posiblesCasillas)>0):
            #El oponente tiene una posibilidad de ganar
            return posiblesCasillas[0]
    return -1

import doctest

doctest.testmod()