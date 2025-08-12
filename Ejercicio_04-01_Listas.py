frutas = ["pera", "manzana", "naranja"]

print(f"Lista original: {frutas}")

frutas.append("banana")
print(f".append(\"banana\"): {frutas}")

frutas.insert(1, "uva")
print(f".insert(1,\"uva\"): {frutas}")

frutas.remove("banana")
print(f".remove(\"banana\"): {frutas}")

fruta_eliminada = frutas.pop(2)
print(f"fruta_eliminada = frutas.pop(2): {frutas}") 
print(f"fruta_eliminada: {fruta_eliminada}")

frutas.sort()
print(f".sort(): {frutas}") 

frutas.reverse()
print(f".reverse(): {frutas}")
