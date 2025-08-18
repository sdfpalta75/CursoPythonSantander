with open("ArchivoEjercicio07-06.txt", "w") as archivo:
    archivo.write("Hola\n")
    archivo.write("de nuevo, ")
    archivo.write("mundo!")

with open("ArchivoEjercicio07-06.txt", "r") as archivo:
    contenido = archivo.read()
    print(f"El contenido del archivo se almacena en una variable tipo {type(contenido)} y es:\n\n{contenido}")
