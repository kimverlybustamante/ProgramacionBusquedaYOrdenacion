def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcular la temperatura promedio de cada ciudad.

    :param datos_temperaturas: Diccionario donde las claves son los nombres de las ciudades
                               y los valores son listas con las temperaturas semanales.
    :return: Diccionario con la temperatura promedio de cada ciudad.
    """
    promedios = {}
    for ciudad, temperaturas in datos_temperaturas.items():
        total_dias = sum(len(semana) for semana in temperaturas)  # Cuenta los días registrados
        suma_total = sum(sum(semana) for semana in temperaturas)  # Suma todas las temperaturas
        promedios[ciudad] = suma_total / total_dias  # Calcula el promedio
    return promedios


# Datos de 3 ciudades, 4 semanas
datos = {
    "Quito": [[15, 14, 16, 17, 18, 18,16], [9, 8, 8, 16, 17, 16, 16], [20, 23, 26, 18, 19, 30, 25], [16, 14, 17, 19, 20, 20, 19]],
    "Nueva loja": [[10, 22, 21, 7, 18, 17, 9], [21, 20, 23, 24, 20, 8, 19], [19, 18, 6, 17, 16, 7, 14], [22, 21, 20, 19, 18, 17, 16]],
    "Cuenca": [[7, 8, 18, 16, 7, 10, 14], [14, 11, 12, 10, 6, 7, 12], [19, 20, 14, 18, 9, 7, 8], [20, 10, 12, 19, 15, 18, 16]]
}

# Llamar la función y mostrar los resultados
resultado = calcular_temperatura_promedio(datos)
print("Temperaturas promedio por ciudad:", resultado)