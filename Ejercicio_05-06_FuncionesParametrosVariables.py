def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(f"La suma de 3 más 15 más 21 es {suma_variable(3, 15, 21)}")
print(f"La suma de 10 más 3 más 11 más 5 es {suma_variable(10, 3, 11, 5)}")
