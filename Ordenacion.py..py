# Matriz bidimensional de ejemplo (3x3)
matriz = [
    [11, 25, 31],
    [44, 15, 6],
    [7, 58, 39]
]

# Función para ordenar una fila (por ejemplo la fila 2)
def ordenar_fila(matriz, fila_index):
    # Ordenar fila en orden ascendente
    matriz[fila_index].sort()

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila 2
ordenar_fila(matriz, 2)

# Mostrar la matriz después de ordenar
print("\nMatriz después de ordenar la fila 2:")
for fila in matriz:
    print(fila)