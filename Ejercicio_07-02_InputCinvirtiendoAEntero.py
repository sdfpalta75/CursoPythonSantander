edad = int(input("Ingresa tu edad: ")) # int() convierte el string de input() a entero

if edad >= 18:
    print("Eres mayor de edad")
elif edad < 0:
    print("Edad incorrecta")
else:
    print("Eres menor de edad")
