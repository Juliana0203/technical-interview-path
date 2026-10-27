class NodoArbol:

  def __init__(self, valor):
    self.valor = valor
    self.izq = None
    self.der = None


# Construcción de un pequeño árbol binario
raiz = NodoArbol(10)
raiz.izq = NodoArbol(5)
raiz.der = NodoArbol(15)