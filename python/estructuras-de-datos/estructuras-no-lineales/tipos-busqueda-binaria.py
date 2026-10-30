def binary_search_iterative(nums: list[int], target: int) -> int:
  """Implementación iterativa de la Búsqueda Binaria.

  Complejidad Temporal: O(log N)
  Complejidad Espacial: O(1)
  """
  izquierda = 0
  derecha = len(nums) - 1

  while izquierda <= derecha:
    medio = (izquierda + derecha) // 2

    if nums[medio] == target:
      return medio
    elif nums[medio] < target:
      izquierda = medio + 1
    else:
      derecha = medio - 1

  return -1


def binary_search_recursive(nums: list[int], target: int) -> int:
  """Implementación recursiva de la Búsqueda Binaria (función envolvente).

  Complejidad Temporal: O(log N)
  Complejidad Espacial: O(log N) debido a la pila de llamadas (call stack).
  """

  def _helper(izquierda: int, derecha: int) -> int:
    if izquierda > derecha:
      return -1

    medio = (izquierda + derecha) // 2

    if nums[medio] == target:
      return medio
    elif nums[medio] < target:
      return _helper(medio + 1, derecha)  # Buscar en la mitad derecha
    else:
      return _helper(izquierda, medio - 1)  # Buscar en la mitad izquierda

  return _helper(0, len(nums) - 1)


# --- Pruebas locales ---
if __name__ == "__main__":
  datos = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
  objetivo = 23

  print(
      "Resultado Iterativo -> Índice:"
      f" {binary_search_iterative(datos, objetivo)}"
  )
  print(
      "Resultado Recursivo -> Índice:"
      f" {binary_search_recursive(datos, objetivo)}"
  )