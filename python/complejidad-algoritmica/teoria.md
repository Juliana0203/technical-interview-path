# Teoría y Guía de Notación Big O

Un **algoritmo** es un conjunto de instrucciones bien definidas para resolver un problema en específico. Debido a que hay varias maneras de resolver un problema, debe haber una manera de evaluar estas soluciones o algoritmos en términos de rendimiento y eficiencia. 


La **Notación Big O** es una métrica en lenguaje matemático que se utiliza en ciencias de la computación para describir cómo crece el tiempo de ejecución (complejidad temporal) o el consumo de memoria (complejidad espacial) de un algoritmo a medida que el tamaño de los datos de entrada ($n$) aumenta.

En palabras simples, la notación Big O no porporciona una medición exacta del tiempo de ejecución, sino que dice el número de operaciones que hará un algoritmo. Este establece un tiempo de ejecución en el peor de los casos. 

En términos matemáticos, describe el límite de una función cuando los argumentos de entrada tienden al infinito o a un valor en particular.

---

## ¿Por qué es importante?
* **Independencia del hardware:** Permite estimar y analizar la eficiencia de un código en diferentes conjuntos de entradas, sin importar si se ejecuta en una supercomputadora o en un teléfono móvil antiguo.
* **Escalabilidad:** Muestra cómo se comportará tu software cuando los datos crezcan exponencialmente (de 10 elementos a 10,000,000).
---

## Gráfico de complejidad
El gráfico Big O es una notación asintótica que se usa para expresar la complejidad d eun algoritmo o su rendimiento en función del tamaño de entrada. Esto ayuda a los programadores a identificar y compreder completamente el peor de los casos y el tiempo de ejecución o la memoria requeria de un algoritmo.

En el pdf **big-o-cheatsheet** se encuentra la gráfica ilustrada.


## Las Órdenes de Complejidad Comunes (De mejor a peor)

### 1. $O(1)$ — Tiempo Constante
* **Qué significa:** El tiempo de ejecución no cambia sin importar el tamaño de los datos de entrada. Estas funciones son muy escalables y se puede determinar que el tiempo de ejecución siempre serña parecido en cualquier ejecución.
* **Ejemplo en Python:** Acceder a un elemento de un diccionario por su clave o leer el primer elemento de una lista por su índice.
```python
def obtener_primer_elemento(lista):
  """Siempre hace una sola operación de acceso por índice,

  sin importar si la lista tiene 5 o 5 millones de elementos.
  """
  if not lista:
    return None
  return lista[0]  # O(1) temporal, O(1) espacial
```

### 2. $O(Log  n)$ — Tiempo Logarítmico
* **Qué significa:** El tiempo de ejecución depende del logaritmo del tamaño de la entrada de datos. Por ejemplo, los algoritmos que dividen los datos de entrada en mitades siguen esta notación.
* **Ejemplo en Python:** La búsqueda binaria, en la que dividimos la lista inicial por la mitad recursivamente hasta encontrar el valor que buscamos es un ejemplo de tiempo logarítmico.
```python
def busqueda_binaria(lista_ordenada, objetivo):
  """Busca un elemento dividiendo el espacio de búsqueda a la mitad

  en cada iteración. Su complejidad es O(log N).
  """
  izquierda = 0
  derecha = len(lista_ordenada) - 1

  while izquierda <= derecha:
    medio = (izquierda + derecha) // 2

    if lista_ordenada[medio] == objetivo:
      return medio  # ¡Encontrado!
    elif lista_ordenada[medio] < objetivo:
      izquierda = medio + 1  # Descartamos la mitad izquierda
    else:
      derecha = medio - 1  # Descartamos la mitad derecha

  return -1  # No encontrado
```

### 3. $O(n)$ — Tiempo Lineal
* **Qué significa:** El tiempo para ejecutar estas funciones depende directamente del tamaño de los datos de entrada ($n$). Cuantos más elementos se añadan al procesamiento, el tiempo de ejecución se incrementará proporcionalmente. 
* **Ejemplo en Python:** Las funciones que usan bucles para recorrer los elementos siguen la notación de tiempo lineal.
```python
def encontrar_maximo(lista):
  """Recorre toda la lista una sola vez.

  Si duplicas los elementos, el tiempo de ejecución se duplica.
  """
  if not lista:
    return None

  max_val = lista[0]
  for numero in lista:  # Se ejecuta N veces
    if numero > max_val:
      max_val = numero
  return max_val
```

### 4. $O(n^2)$ — Tiempo Cuadrático
* **Qué significa:** El crecimiento de las funciones con tiempo cuadrático es exponencial, generalmente se observa en las funciones con bucles anidados. Se debe controlar correctamente la cantidad de elementos de entrada que tienen estos algoritmos, ya que el tiempo de ejecución puede descontrolarse rápidamente al tener un crecimiento tan elevado.
* **Ejemplo en Python:** Involucra bucles anidados donde cada elemento se procesa en función de todos los demás.
```python
def buscar_duplicados_fuerza_bruta(lista):
  """Compara cada elemento con todos los demás usando bucles anidados.

  Si N es 1,000, hará alrededor de 1,000,000 de operaciones.
  """
  pares = []
  n = len(lista)
  for i in range(n):  # N veces
    for j in range(i + 1, n):  # N veces en promedio
      if lista[i] == lista[j]:
        pares.append((lista[i], lista[j]))
  return pares
```


### 5. $O(2^n)$ — Tiempo Exponencial
* **Qué significa:** Expresa las funciones cuyo tiempo de ejecución se dobla con cada elemento que añadimos al dataset de entrada
* **Ejemplo en Python:** Las funciones que implementan cálculos recursivos con fuerza bruta siguen esta notación, debemos evitar su uso o limitarlo a conjuntos de entrada pequeños para que el tiempo de ejecución sea razonable.
```python
def fibonacci_recursivo_ingenuo(n):
  """Calcula el n-ésimo número de Fibonacci de forma recursiva pura.

  Cada llamada genera dos ramas adicionales, creando un árbol de llamadas de O(2^N).
  """
  if n <= 1:
    return n
  return fibonacci_recursivo_ingenuo(n - 1) + fibonacci_recursivo_ingenuo(n - 2)
```

