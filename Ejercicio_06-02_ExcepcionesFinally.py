try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    resultado = "Error. División en cero."
finally: 
    print(resultado)

# el contenido del bloque finally se ejecuta siempre
