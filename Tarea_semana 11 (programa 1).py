#TAREA SEMANA 11
#Programa 1
#Mary Morales
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return True, (i, j)
    return False, None

# Ejemplo de matriz 3x3
mi_matriz = [
    [12, 50, 28],
    [98, 78, 120],
    [5, 115, 93]
     ]
valor_a_buscar = 28
encontrado, posicion = buscar_valor(mi_matriz, valor_a_buscar)

if encontrado:
    print(f"El valor {valor_a_buscar} se encuentra en la posición {posicion}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
valor_a_buscar = 5
encontrado, posicion = buscar_valor(mi_matriz, valor_a_buscar)

if encontrado:
    print(f"El valor {valor_a_buscar} se encuentra en la posición {posicion}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")