conjunto1 = {1, 2, 3}
conjunto2 = set([3, 4, 5])

print(f"Conjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")

union = conjunto1 | conjunto2
print(f"Unión de conjuntos (|): {union}")  # Imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print(f"Intersección de conjuntos (&): {interseccion}")  # Imprime {3}

diferencia = conjunto1 - conjunto2
print(f"Diferencia de conjuntos (conj1-conj2): {diferencia}")  # Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print(f"Diferencia sistémica de los conjuntos (^): {diferencia_simetrica}")  # Imprime {1, 2, 4, 5}

# Métodos de los conjunto
print("\n\nMétodos de los conjuntos\n")

frutas = {"manzana", "banana", "naranja"}
print(f"Conjunto original: {frutas}")

frutas.add("pera") # agrega un elemento al conjunto
print(f"Agregando elemento con .add: {frutas}")  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana") # elimina el elemento, si no existe tira un error
print(f"Eliminando elemento con .remove: {frutas}")  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva") # elimina el elemento. Si no existe, no hace nada
print(f"Eliminando elemento con .discard: {frutas}")  # Imprime {"manzana", "naranja", "pera"}

frutas.clear()
print(f"Borrando el contenido del conjunto con .clear: {frutas}")  # Imprime set()
