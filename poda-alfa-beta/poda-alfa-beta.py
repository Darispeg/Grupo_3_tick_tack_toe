#Esta es la clase Poda-Alfa-Beta

infinito = 10000

# Recibe Inicial
def Alfa_Beta(problema):#Recibe una Lista
    inicial = problema.ESTADO_INICIAL # Instaciar como la raiz del Nodo
    # problema = Nodo(inicial)
    [accion,valor] = VALOR_MAX(problema,inicial,(-1)*infinito,infinito)

    return accion


def VALOR_MAX(problema,estado,alfa,beta):
    if problema.ES_OBJETIVO(estado):#Es hoja //si no tiene Hijos 
        return problema.UTILIDAD(estado)
    mejor_accion = None
    mayor_valor = (-1)*infinito
    for accion in problema.ACCIONES(estado):#hijos
        resultado = problema.RESULTADO(estado,accion)# Nodo // Lista de posiciones Ocupadas
        utilidad = VALOR_MIN(problema,resultado,alfa,beta)
        if utilidad[1] > mayor_valor:#utilidad[1] porque es una Lista
            mayor_valor = utilidad[1]
            mejor_accion = accion
        if mayor_valor >= beta:
            return [mejor_accion,mayor_valor]
        if mayor_valor > alfa:
            alfa = mayor_valor
    return [mejor_accion, mayor_valor]


def VALOR_MIN(problema,estado,alfa,beta):
    if problema.ES_OBJETIVO(estado): #Es hoja
        return problema.UTILIDAD(estado) # peso o costo
    menor_valor = infinito
    mejor_accion = None
    for accion in problema.ACCIONES(estado): #Hijos
        resultado = problema.RESULTADO(estado,accion) # Nodo
        utilidad = VALOR_MAX(problema,resultado,alfa,beta)
        if utilidad < menor_valor:
            menor_valor = utilidad
            mejor_accion = accion
        if menor_valor <= alfa:
            return [mejor_accion, menor_valor]
        if menor_valor > beta:
            beta = menor_valor
    return [mejor_accion,menor_valor]



