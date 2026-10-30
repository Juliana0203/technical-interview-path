from yaml import Node

def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None


class HashTable:

  def _hash(self, key) -> int:
    """Función hash para convertir cualquier clave en un índice válido."""
    return hash(key) % self.capacity

  def put(self, key, value):
    """Inserta o actualiza un par clave-valor en O(1) promedio."""
    index = self._hash(key)

    if self.buckets[index] is None:
      self.buckets[index] = Node(key, value)
      self.size += 1
      return

    # Si ya hay elementos, recorremos la cadena buscando si la clave ya existe
    current = self.buckets[index]
    while current:
      if current.key == key:
        current.value = value  # Actualizamos el valor existente
        return
      if current.next is None:
        break
      current = current.next

    # Si no existía, agregamos un nuevo nodo al final del bucket
    current.next = Node(key, value)
    self.size += 1

  def get(self, key):
    """Obtiene el valor asociado a una clave en O(1) promedio."""
    index = self._hash(key)
    current = self.buckets[index]

    while current:
      if current.key == key:
        return current.value
      current = current.next

    raise KeyError(f"La clave '{key}' no existe en la tabla hash.")

  def remove(self, key):
    """Elimina un elemento por su clave en O(1) promedio."""
    index = self._hash(key)
    current = self.buckets[index]
    prev = None

    while current:
      if current.key == key:
        if prev is None:
          self.buckets[index] = current.next  # Era el primer nodo
        else:
          prev.next = current.next  # Saltamos el nodo a eliminar
        self.size -= 1
        return current.value
      prev = current
      current = current.next

    raise KeyError(f"La clave '{key}' no existe para eliminar.")


# --- Pruebas de funcionamiento local ---
if __name__ == "__main__":
  tabla = HashTable(capacity=5)
  tabla.put("Ana", 25)
  tabla.put("Carlos", 30)
  tabla.put("Lucia", 22)

  print(f"Edad de Ana: {tabla.get('Ana')}")  # 25
  tabla.put("Ana", 26)  # Actualiza el valor
  print(f"Edad actualizada de Ana: {tabla.get('Ana')}")  # 26

  tabla.remove("Carlos")
  print("Carlos eliminado exitosamente.")