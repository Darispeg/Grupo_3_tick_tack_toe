tablero=[]  #Nuestro tablero inicalmente serán nueva callisas vacias
casillasVacias=[]
TABLERO_FILAS=3
TABLERO_COLUMNAS=3
#Validando casillas de la Jugada 
def numero(valor, inferior, superior):
    """

    # Para valores que no son numeros
    >>> numero("F", 0, 2)
    Solo se adminten números entre 0 y 2
    False

    # Para numeros correctos
    >>> numero("1", 0, 2)
    True
    
    #Para numeros mayores del rango
    >>> numero("5", 0, 2)
    El valor indicado es incorrecto, introduzca un número entre 0 y 2
    False

    """
    while True:
        while(not valor.isnumeric()):
            print("Solo se adminten números entre {0} y {1}".format(inferior,superior))
            return False
        coor=int(valor)
        if(coor>=inferior and coor<=superior):
            return True
        else:
            print("El valor indicado es incorrecto, introduzca un número entre {0} y {1}".format(inferior,superior))
            return False


def inicializar():
    """

    >>> inicializar()
    [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [0, 1, 2, 3, 4, 5, 6, 7, 8]]

    """
    #inicializamos el tablero
    tablero.clear()
    casillasVacias.clear()
    for i in range(TABLERO_FILAS*TABLERO_COLUMNAS):
        tablero.append(' ')
        casillasVacias.append(i)
    return [tablero,casillasVacias]



import doctest

doctest.testmod()