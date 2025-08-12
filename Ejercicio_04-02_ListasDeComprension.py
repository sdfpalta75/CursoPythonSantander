numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cuadrados = [n**2 for n in numeros]
print(f"Lista original: {numeros}")
print(f"Números al cuadrado: {cuadrados}")

cuadrados_con_filtro = [n**2 for n in numeros if n%2 == 0]
print(f"Números pares al cuadrado (filtrados con if): {cuadrados_con_filtro}")
