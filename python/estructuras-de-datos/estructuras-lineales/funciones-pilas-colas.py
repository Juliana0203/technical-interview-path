from collections import deque

class Stack:
  """Implementación de una Pila (Stack - LIFO: Last In, First Out)

  utilizando una lista de Python por debajo de manera eficiente.
  """

  def __init__(self):
    self._items = []

  def push(self, item):
    """Agrega un elemento a la cima de la pila O(1)."""
    self._items.append(item)

  def pop(self):
    """Elimina y retorna el elemento de la cima O(1)."""
    if self.is_empty():
      raise IndexError("La pila está vacía")
    return self._items.pop()

  def peek(self):
    """Consulta el elemento superior sin eliminarlo O(1)."""
    if self.is_empty():
      raise IndexError("La pila está vacía")
    return self._items[-1]

  def is_empty(self) -> bool:
    """Retorna True si la pila está vacía O(1)."""
    return len(self._items) == 0

  def size(self) -> int:
    """Retorna el número de elementos en la pila O(1)."""
    return len(self._items)

  def __str__(self):
    return f"Cima -> {list(reversed(self._items))}"


class Queue:
  """Implementación de una Cola (Queue - FIFO: First In, First Out)

  utilizando collections.deque para garantizar operaciones O(1) en ambos extremos.
  """

  def __init__(self):
    # deque permite inserciones y eliminaciones ultra rápidas en O(1) por ambos lados
    self._items = deque()

  def enqueue(self, item):
    """Agrega un elemento al final de la cola O(1)."""
    self._items.append(item)

  def dequeue(self):
    """Elimina y retorna el elemento del frente de la cola O(1)."""
    if self.is_empty():
      raise IndexError("La cola está vacía")
    return self._items.popleft()

  def front(self):
    """Consulta el primer elemento de la cola sin eliminarlo O(1)."""
    if self.is_empty():
      raise IndexError("La cola está vacía")
    return self._items[0]

  def is_empty(self) -> bool:
    """Retorna True si la cola está vacía O(1)."""
    return len(self._items) == 0

  def size(self) -> int:
    """Retorna el número de elementos en la cola O(1)."""
    return len(self._items)

  def __str__(self):
    return f"Frente -> {list(self._items)} <- Final"


# --- Pruebas locales de funcionamiento ---
if __name__ == "__main__":
  print("--- PRUEBAS DE PILA (STACK) ---")
  pila = Stack()
  pila.push(10)
  pila.push(20)
  pila.push(30)
  print(pila)  # Cima -> [30, 20, 10]
  print(f"Elemento superior (peek): {pila.peek()}")  # 30
  print(f"Elemento extraído (pop): {pila.pop()}")  # 30
  print(f"Tamaño actual: {pila.size()}")  # 2

  print("\n--- PRUEBAS DE COLA (QUEUE) ---")
  cola = Queue()
  cola.enqueue("Ana")
  cola.enqueue("Carlos")
  cola.enqueue("Lucía")
  print(cola)  # Frente -> ['Ana', 'Carlos', 'Lucía'] <- Final
  print(f"Siguiente en ser atendido (front): {cola.front()}")  # Ana
  print(f"Atendido (dequeue): {cola.dequeue()}")  # Ana
  print(cola)  # Frente -> ['Carlos', 'Lucía'] <- Final