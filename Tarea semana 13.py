#Tarea semana 13
#Funcion para calcular para calcular el promedio de temperatura en un intervalo de tiempo
temperaturas = [
    # Cuenca
    [
        [25, 26, 11, 24, 25, 15, 26],  # Semana 1: Temperaturas diarias
        [26, 15, 14, 15, 13, 26, 25]  # Semana 2: Temperaturas diarias
    ],
    # Ambato
    [
        [28, 12, 23, 20, 11, 15, 24],  # Semana 1: Temperaturas diarias
        [21, 23, 14, 25, 23, 20, 24]  # Semana 2: Temperaturas diarias
    ],
    # Latacunga
    [
        [18, 13, 12, 18, 19, 21, 19],  # Semana 1: Temperaturas diarias
        [18, 17, 28, 29, 10, 29, 18]  # Semana 2: Temperaturas diarias
    ]
]


# definimos la funcion  con parametros
def calcular_promedios_ciudades(temperaturas,
                                nombres_ciudades):  # FUNCION CON PARAMETROS( recibe temperaturas y nombres de ciudades)

    promedios_ciudades = {}

    for indice_ciudad, ciudad in enumerate(temperaturas):  # DECLARAROS UN FOR

        suma_total = 0  # INICIALIZAMOSMLAS VARIBLES
        dias_total = 0  # INICIALIZAMOS LAS VARIABLES

        for semana in ciudad:
            # mediante el fort  contamos los dias de la seman  y las semanas
            suma_semana = sum(semana)
            dias_semana = len(semana)
            #            usamos acumuladores
            suma_total += suma_semana
            dias_total += dias_semana

        promedio_ciudad = suma_total / dias_total if dias_total else 0  # realizamos la operacion de  sumar los promedios totales  divididos para los dias
        promedios_ciudades[nombres_ciudades[
            indice_ciudad]] = promedio_ciudad  # en este arreglo almacenamos la ciudad  y el promedio de temperatura
    # por lo tanto retorna la funcion
    return promedios_ciudades


# las ciudades
nombres_ciudades = ["Cuenca", "Ambato", "Latacunga"]

# Calcular y mostrar los promedios de temperatura
print("******************** reaultados Obtenidos por medio de la funcion*******************")
print("**********************************************")
promedios = calcular_promedios_ciudades(temperaturas, nombres_ciudades)
# Mostrar por consola  cada promedio con una iteracion  donde va el promedio la ciudad
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: Promedio de temperatura {promedio:.2f}°C")



