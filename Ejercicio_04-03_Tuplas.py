miTupla = (1, 2, 3, 2, 4, 2)
print(f"Tupla original: {miTupla}")

# método count: devuelve la cantidad de veces que un elemento aparece en la tupla
print(f"Método count - Cantidad de veces que aparece el 2: {miTupla.count(2)}")

# método index: devuelve el índice de la primera vez que aparece el elemento
print(f"Método index - El 3 aparece por primera vez en posición: {miTupla.index(3)}")

# len: si bien es una función, no un método de las tuplas, es muy utilizada con éstas
print(f"La tupla tiene {len(miTupla)} elementos")
