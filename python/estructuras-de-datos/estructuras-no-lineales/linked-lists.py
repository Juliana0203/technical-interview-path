class Nodo:

  def __init__(self, valor):
    self.valor = valor
    self.siguiente = None


# Construcción manual: 10 -> 20 -> 30
cabeza = Nodo(10)
cabeza.siguiente = Nodo(20)
cabeza.siguiente.siguiente = Nodo(30)

# Recorrido de la lista enlazada
actual = cabeza
while actual:
  print(actual.valor, end=" -> ")
  actual = actual.siguiente
# Output: 10 -> 20 -> 30 ->