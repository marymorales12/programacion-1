#TAREA SEMANA 11
#Programa 2
#Mary Morales

def ordenar_fila(matriz, numero_fila):
    matriz[numero_fila] = sorted(matriz[numero_fila])

# Creamos variable bidimensional 3x3
mi_matriz = [
    [98, 120, 67],
    [65, 55, 104],
    [37, 21, 101]
    ]

#Elejimos la fila a ordenat
numero_fila_a_ordenar = 1

#imprimimos la variable original
print("Matriz original:")
for fila in mi_matriz:
    print(fila)

ordenar_fila(mi_matriz, numero_fila_a_ordenar)

print(f"\nMatriz con la fila {numero_fila_a_ordenar} ordenada:")
for fila in mi_matriz:
    print(fila)

###############################

#Para ordenar automaticamente toda una matriz

#Empezamos creando la  variable dimensional
matriz_b=[
    [5,2,4],
    [7,12,53],
    [14,52,63]
    ]
#imprimimos nuestra variable original
print("Arreglo_bibimensional_3x3_original ",matriz_b)
#haciendo uso del sorf ordenamos los valores de nuestra variable de forma ascendente
matriz_b.sort()
#inprimimos la variable  ordenadad
print("Arreglo_bibimensional_3x3_ordenado ",matriz_b)
