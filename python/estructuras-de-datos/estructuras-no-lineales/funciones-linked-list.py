
# Implementación de una lista enlazada simple en Python

class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  def size(self) -> int:
    """Retorna el número de elementos en la lista O(N)."""
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count

  def empty(self) -> bool:
    """Retorna True si la lista está vacía O(1)."""
    return self.head is None

  def value_at(self, index: int):
    """Retorna el valor del ítem en el índice dado O(N)."""
    current = self.head
    current_index = 0
    while current:
      if current_index == index:
        return current.value
      current = current.next
      current_index += 1
    raise IndexError(f"Índice fuera de rango: {index}")

  def push_front(self, value):
    """Agrega un elemento al inicio de la lista O(1)."""
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

  def pop_front(self):
    """Elimina el primer elemento y retorna su valor O(1)."""
    if self.empty():
      raise IndexError("La lista está vacía")
    popped_value = self.head.value
    self.head = self.head.next
    return popped_value

  def push_back(self, value):
    """Agrega un elemento al final de la lista O(N)."""
    new_node = Node(value)
    if self.empty():
      self.head = new_node
      return

    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  def pop_back(self):
    """Elimina el último elemento y retorna su valor O(N)."""
    if self.empty():
      raise IndexError("La lista está vacía")
    if self.head.next is None:
      return self.pop_front()

    current = self.head
    while current.next.next:
      current = current.next

    popped_value = current.next.value
    current.next = None
    return popped_value

  def front(self):
    """Obtiene el valor del primer elemento O(1)."""
    if self.empty():
      raise IndexError("La lista está vacía")
    return self.head.value

  def back(self):
    """Obtiene el valor del último elemento O(N)."""
    if self.empty():
      raise IndexError("La lista está vacía")
    current = self.head
    while current.next:
      current = current.next
    return current.value

  def insert(self, index: int, value):
    """Inserta un valor en el índice dado O(N)."""
    if index < 0:
      raise IndexError("Índice inválido")
    if index == 0:
      self.push_front(value)
      return

    new_node = Node(value)
    current = self.head
    current_index = 0

    while current and current_index < index - 1:
      current = current.next
      current_index += 1

    if not current:
      raise IndexError("Índice fuera de rango")

    new_node.next = current.next
    current.next = new_node

  def erase(self, index: int):
    """Elimina el nodo en el índice dado O(N)."""
    if self.empty():
      raise IndexError("La lista está vacía")
    if index == 0:
      return self.pop_front()

    current = self.head
    current_index = 0

    while current.next and current_index < index - 1:
      current = current.next
      current_index += 1

    if not current.next:
      raise IndexError("Índice fuera de rango")

    removed_value = current.next.value
    current.next = current.next.next
    return removed_value

  def value_n_from_end(self, n: int):
    """Retorna el valor del nodo a n posiciones desde el final O(N)."""
    slow = self.head
    fast = self.head

    for _ in range(n):
      if fast is None:
        raise IndexError("N es mayor que el tamaño de la lista")
      fast = fast.next

    while fast and fast.next:
      slow = slow.next
      fast = fast.next

    if slow is None:
      raise IndexError("Índice fuera de rango")
    return slow.value

  def reverse(self):
    """Invierte los punteros de toda la lista O(N)."""
    prev = None
    current = self.head
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev

  def remove_value(self, value):
    """Elimina el primer ítem en la lista con este valor O(N)."""
    if self.empty():
      return False

    if self.head.value == value:
      self.head = self.head.next
      return True

    current = self.head
    while current.next:
      if current.next.value == value:
        current.next = current.next.next
        return True
      current = current.next
    return False

  def __str__(self):
    """Método auxiliar para imprimir la lista visualmente."""
    valores = []
    current = self.head
    while current:
      valores.append(str(current.value))
      current = current.next
    return " -> ".join(valores) + " -> None"


# --- Pruebas locales ---
if __name__ == "__main__":
  ll = LinkedList()
  ll.push_back(10)
  ll.push_back(20)
  ll.push_front(5)
  print(f"Lista inicial: {ll}")  # 5 -> 10 -> 20 -> None

  ll.insert(1, 7)
  print(f"Tras insertar 7 en índice 1: {ll}")  # 5 -> 7 -> 10 -> 20 -> None

  ll.reverse()
  print(f"Lista invertida: {ll}")  # 20 -> 10 -> 7 -> 5 -> None