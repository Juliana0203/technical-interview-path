import heapq

# Crear una lista y transformarla en heap
numeros = [5, 3, 8, 1, 2]
heapq.heapify(numeros)  # O(N)

# Insertar un elemento manteniendo la propiedad de heap
heapq.heappush(numeros, 0)  # O(log N)

# Extraer siempre el menor elemento
menor = heapq.heappop(numeros)  # O(log N) -> Extrae el 0
print(menor)