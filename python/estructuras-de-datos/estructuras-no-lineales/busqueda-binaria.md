# Guía Definitiva de Búsqueda Binaria (Binary Search)

La **Búsqueda Binaria** es uno de los algoritmos más eficientes y elegantes en ciencias de la computación. Permite encontrar la posición de un valor objetivo dentro de un **arreglo previamente ordenado**.

---

## ¿Cómo funciona?

A diferencia de una búsqueda lineal (que revisa elemento por elemento en tiempo $O(N)$), la búsqueda binaria aplica el principio de **"Divide y Vencerás"**:
1. Se establecen dos punteros: `izquierda` (al principio del array) y `derecha` (al final).
2. Se calcula el elemento del **medio**: `medio = (izquierda + derecha) // 2`.
3. Se compara el valor del medio con el `objetivo`:
   * Si coinciden, ¡lo encontramos! Retornamos su índice.
   * Si el objetivo es **menor** que el elemento del medio, descartamos toda la mitad derecha moviendo `derecha = medio - 1`.
   * Si el objetivo es **mayor**, descartamos toda la mitad izquierda moviendo `izquierda = medio + 1`.
4. El proceso se repite dividiendo el espacio de búsqueda a la mitad en cada paso hasta encontrar el elemento o cruzar los punteros.

---

## Complejidad Temporal y Espacial

* **Complejidad Temporal:** $O(\log N)$ — Como el espacio de búsqueda se reduce a la mitad en cada iteración, incluso para un array de 1,000,000 de elementos, solo tomará a lo sumo unas 20 operaciones encontrar el resultado.
* **Complejidad Espacial:** $O(1)$ — Solo requiere un par de variables para los punteros (si se implementa de forma iterativa).

---

## Requisito Indispensable
Para que la búsqueda binaria funcione correctamente, **el arreglo de entrada DEBE estar ordenado**. Si no está ordenado, el resultado será incorrecto.