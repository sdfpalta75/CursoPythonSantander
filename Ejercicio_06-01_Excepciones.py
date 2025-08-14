try: # Dentro de este bloque va el código que puede generar una excepción
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError: # excepción ante división por 0
    print("Error. Intenta dividir en 0")
except ValueError: #excepción ante tipo de dato inesperado
    print("Error. Valor inesperado")

# se pueden manejar distintas excepciones
# se puede poner una excepción general con except: (sin indicar un tipo de error)
