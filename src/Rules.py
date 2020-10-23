import random
import math
import Board
import estrategia1
import estrategia2
NIVEL_DESPISTE=-1
#Colaca una ficha en el tablero

def numeroHermanos(casilla, ficha, v, h,tablero):
    f=math.floor(casilla/Board.TABLERO_COLUMNAS) #Obtengo la fila
    c=casilla % Board.TABLERO_COLUMNAS #columna
    fila_nueva=f+v
    if(fila_nueva<0 or fila_nueva>=Board.TABLERO_FILAS):
        return 0
    columna_nueva=c+h
    if(columna_nueva<0 or columna_nueva>=Board.TABLERO_COLUMNAS):
        return 0
    #No estamos en el limite así que
    #calculamos la nueva posición y vemos si hay la misma ficha
    pos=(fila_nueva*Board.TABLERO_COLUMNAS+columna_nueva)
    if(tablero[pos]!=ficha):
        return 0
    else:
        return 1+numeroHermanos(pos,ficha,v,h,tablero)

# comprobamos que la ficha colocada en la casilla indica tiene dos fichas similares en casillas contiguas
def hemosGanado(casilla, ficha, tablero):
    hermanos=numeroHermanos(casilla,ficha,-1,-1,tablero)+numeroHermanos(casilla,ficha,1,1,tablero)
    if(hermanos==2):
        return True
    hermanos=numeroHermanos(casilla,ficha,1,-1,tablero)+numeroHermanos(casilla,ficha,-1,1,tablero)
    if(hermanos==2):
        return True
    hermanos=numeroHermanos(casilla,ficha,-1,0,tablero)+numeroHermanos(casilla,ficha,1,0,tablero)
    if(hermanos==2):
        return True
    hermanos=numeroHermanos(casilla,ficha,0,-1,tablero)+numeroHermanos(casilla,ficha,0,1,tablero)
    if(hermanos==2):
        return True

def colocarFicha(ficha):
    print("Dame la posición de una ficha")
    while True:
        fila=Board.numero("Fila entre [1 y 3]: ", 1,3)-1 #Restamos uno ya que nuestro rango real está entre 0 y 2
        columna=Board.numero("Columna entre [1 y 3]: ",1,3)-1
        #Como mi tablero es de 3x3
        casilla=fila*Board.TABLERO_COLUMNAS+columna
        if(Board.tablero[casilla]!=' '):
            #Esa casilla ya está cubierta
            print("La casilla está ocupada")
        else:
            Board.tablero[casilla]=ficha
            return casilla



#Inteligencia de la Maquina

def colocarFichaMaquina(ficha, fichaContrincante, tablero):
    random.shuffle(Board.casillasVacias)
    despiste=random.randint(0,100)
    
    
    for casilla in Board.casillasVacias:
        if(hemosGanado(casilla,ficha, tablero)):
            if(despiste>NIVEL_DESPISTE):
                Board.tablero[casilla]=ficha
                return casilla
            else:
                print("No nos hemos fijado en que podíamos ganar")
    despiste=random.randint(0,100)
    for casilla in Board.casillasVacias:
        if(hemosGanado(casilla,fichaContrincante, tablero)):
            if(despiste>NIVEL_DESPISTE):
                Board.tablero[casilla]=ficha
                return casilla
            else:
                print("No nos hemos dado cuenta de que nos podían ganar")
    # Algoritmos de Decision
    if ficha =="X":
        mejorOpcion=estrategia2.laOpcion(tablero, Board.casillasVacias, ficha, False)
    else:
        mejorOpcion=estrategia1.laOpcion(tablero, Board.casillasVacias, ficha, False)
    #  ---------------------
    if(mejorOpcion!=-1):
        casilla=mejorOpcion
    else:
        if(len(Board.casillasVacias)>0):
            print("No hay mejor opción así que escojemos la primera de todas")
            casilla=Board.casillasVacias[0]
        else:
            return -1
    Board.tablero[casilla]=ficha
    return casilla