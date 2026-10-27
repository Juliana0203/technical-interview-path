# Grafo no dirigido representado como diccionario de listas
grafo = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C"]}

# Consultar los vecinos de un nodo
print(f"Vecinos de A: {grafo['A']}")