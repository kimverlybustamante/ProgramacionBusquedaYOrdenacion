# Crear una matriz 3D
#
# almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Temperatura Quito Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 8},
            {"day": "Miércoles", "temp": 8},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 19}
        ]
    ],
    [   # Temperatura Nueva Loja Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 25}
        ]
    ],
    [   # Temperatura Cuenca Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 7},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 16}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Temperatura Quito Ciudad 1", "Temperatura Nueva Loja Ciudad 2", "Temperatura Cuenca Ciudad 3"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")