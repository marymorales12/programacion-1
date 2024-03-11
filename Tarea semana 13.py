#Tarea semana 13
#Funcion para calcular para calcular el promedio de temperatura en un intervalo de tiempo
def calculo_temperatura(datos,ciudad,semana_inicio, semana_final): #definicion de funcion
    num_itms=0 #variable para alamacenar el total de items leidos
for i in range(lend(datos[ciudad])): #elementos en cada posicion
    for i>=semana_inicio and i<=semana_final:
        for j in range(lend(datos[ciudad])):
            for i in range(lend(datos[ciudad])):
                suma_temp=datos[ciudad][1][j]["temp"]
                num_itms=num_itms+1
                print(datos[ciudad][1][j])

promedio=suma_temp/num_itms
return promedio
#datos de temperatura
temperaturas = [
    [   # Ciudad 1 Machala
        [   # Semana 1
            {"day": "Lunes", "temp": 45},#indice 0
            {"day": "Martes", "temp": 30},#indice 1
            {"day": "Miércoles", "temp": 42},
            {"day": "Jueves", "temp": 51},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 51},
            {"day": "Viernes", "temp": 45},
            {"day": "Sábado", "temp": 39},
            {"day": "Domingo", "temp": 43}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 51},
            {"day": "Miércoles", "temp": 45},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 53},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 5}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 55},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 11}
        ]
    ],
    [   # Ciudad 2_Macas
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 54},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 53},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 46},
            {"day": "Miércoles", "temp": 50},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 55},
            {"day": "Sábado", "temp": 57},
            {"day": "Domingo", "temp": 11}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 64},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 66},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 49},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [   # Ciudad 3_Latacunga
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 8},
            {"day": "Sábado", "temp": 5},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 11}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 9},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 3}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 8}
        ]
    ]
]

ciudad=input("Ingrese la cuidad")
promedio=calcular_temperaturas(temperaturas, ciudad 1, semenana inicio 1, semana final 2)
print(promedio)




