# Escritura mi Archivo de Texto
# Escribimos en el archivo my_notes.txt
with open("my_notes.txt", "w") as archivo:
    archivo.write("En mi archivo voy a empezar a escribir mi primera nota.\n")
    archivo.write("Ahora estoy conociendo mas de python escrbiendo mi segunda nota.\n")
    archivo.write("Terminar mi tercera nota cerrando el archivo correctamente.\n")

# Lectura de mi Archivo de Texto
# Abrimos el archivo y vamos a leer línea por línea
with open("my_notes.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())