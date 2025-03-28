# 1. Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Laura Sofia",
    "apellido": "Gomez Torres",
    "edad": 25,
    "ciudad": "Bogota",
    "profesion": "Periodista"
}

# 2. Modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Medellin"

# 3. Agregar una nueva clave-valor al diccionario ("hobby")
informacion_personal["hobby"] = "Bailar"

# 4. Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0996547123"

# 5. Eliminar la clave "edad"
del informacion_personal["edad"]

# 6. Imprimir el diccionario final
print(informacion_personal)