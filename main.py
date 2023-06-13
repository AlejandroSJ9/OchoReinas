def es_seguro(tablero, fila, columna):
    for i in range(fila):
        if tablero[i] == columna:
            return False
    
    for i in range(fila):
        if abs(tablero[i] - columna) == abs(i - fila):
            return False
    
    return True


def colocar_reina(tablero, fila):
    
    if fila >= 8:
        return True
    
    for columna in range(8):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna
            if colocar_reina(tablero, fila + 1):
                return True
            tablero[fila] = -1
    
    return False


def resolver_ocho_reinas():
    
    tablero = [-1] * 8
    
    if colocar_reina(tablero, 0):
        print("Solución encontrada:")
        for fila in range(8):
            for columna in range(8):
                if tablero[fila] == columna:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
    else:
        print("No se encontró solución.")


resolver_ocho_reinas()
