from collections import deque

# --- Pila (Stack - LIFO) ---
pila = []
pila.append(1)  # Push
pila.append(2)
ultimo = pila.pop()  # Pop -> saca el 2 (O(1))

# --- Cola (Queue - FIFO) ---
cola = deque([10, 20, 30])
cola.append(40)  # Enqueue al final (O(1))
primero = cola.popleft()  # Dequeue al inicio (O(1)) -> saca el 10