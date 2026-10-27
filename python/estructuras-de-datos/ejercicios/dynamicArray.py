
# Vector Automáticamente Redimensionable en Python

class DynamicArray:

  def __init__(self, initial_capacity: int = 4):
    self.capacity = initial_capacity
    self.size = 0
    # Creamos un array estático simulado con valores None de tamaño fijo inicial
    self.data = [None] * self.capacity

  def __len__(self) -> int:
    """Permite usar la función len(vector)"""
    return self.size

  def is_empty(self) -> bool:
    return self.size == 0

  def get(self, index: int):
    """Obtener un elemento por su índice en O(1)"""
    self._validate_index(index)
    return self.data[index]

  def set(self, index: int, element):
    """Modificar un elemento en un índice existente en O(1)"""
    self._validate_index(index)
    self.data[index] = element

  def append(self, element):
    """Agregar un elemento al final.

    Si se llena, duplica la capacidad (O(1) amortizado).
    """
    if self.size == self.capacity:
      self._resize()

    self.data[self.size] = element
    self.size += 1

  def _resize(self):
    """Método privado para duplicar la capacidad del array subyacente."""
    self.capacity *= 2
    new_data = [None] * self.capacity

    # Copiar los elementos antiguos al nuevo array
    for i in range(self.size):
      new_data[i] = self.data[i]

    self.data = new_data
    print(f"[LOG] Vector redimensionado. Nueva capacidad: {self.capacity}")

  def remove(self, index: int):
    """Eliminar un elemento por índice y desplazar los demás a la izquierda O(N)."""
    self._validate_index(index)
    removed_element = self.data[index]

    # Desplazar elementos
    for i in range(index, self.size - 1):
      self.data[i] = self.data[i + 1]

    # Limpiar la última posición para liberar memoria
    self.data[self.size - 1] = None
    self.size -= 1
    return removed_element

  def _validate_index(self, index: int):
    if index < 0 or index >= self.size:
      raise IndexError(f"Índice fuera de rango: {index}, Tamaño: {self.size}")


# --- Bloque de pruebas local ---
if __name__ == "__main__":
  vector = DynamicArray(initial_capacity=3)

  vector.append("Python")
  vector.append("TypeScript")
  vector.append("Fastify")  # Aquí se llena la capacidad (3)
  vector.append("Prisma")  # ¡Aquí se dispara el primer resize (capacidad 6)!

  print(f"\nElemento en índice 2: {vector.get(2)}")  # Fastify
  print(f"Tamaño total del vector: {len(vector)}")  # 4

  vector.remove(1)  # Elimina "TypeScript" y desplaza los demás
  print(f"Nuevo elemento en índice 1: {vector.get(1)}")  # Fastify
  print(f"Tamaño después de eliminar: {len(vector)}")  # 3