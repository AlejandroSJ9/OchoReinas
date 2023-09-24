def es_seguro(tablero, fila, columna):
    for i in range(fila):
        if tablero[i] == columna:
            return False
    
    for i in range(fila):
        if abs(tablero[i] - columna) == abs(i - fila):
            return False
    
    return True

def resolver_ocho_reinas():
    tablero = [-1] * 8
    soluciones = []
    encontrar_todas_soluciones(tablero, 0, soluciones)
    
    if soluciones:
        print("Se encontraron", len(soluciones), "soluciones:")
        for solucion in soluciones:
            for fila in range(8):
                for columna in range(8):
                    if solucion[fila] == columna:
                        print("Q", end=" ")
                    else:
                        print(".", end=" ")
                print()
            print()
    else:
        print("No se encontró ninguna solución.")

def encontrar_todas_soluciones(tablero, fila, soluciones):
    if fila >= 8:
        soluciones.append(tablero[:])  # Almacenar una copia de la solución encontrada
        return
    
    for columna in range(8):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna
            encontrar_todas_soluciones(tablero, fila + 1, soluciones)
            tablero[fila] = -1

resolver_ocho_reinas()
