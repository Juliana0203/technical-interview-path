# Guía Completa de Métodos y Funciones de un Array

Un vector dinámico es una estructura de datos lineal que gestiona un bloque de memoria contigua y se redimensiona automáticamente cuando supera su capacidad máxima. A continuación, se detallan cada una de las funciones y operaciones fundamentales que componen su arquitectura.

---

## Resumen de Métodos y Complejidad Temporal

| Método | Descripción | Complejidad Temporal |
| :--- | :--- | :--- |
| `size()` | Retorna la cantidad de elementos actuales. | $O(1)$ |
| `capacity()` | Retorna la capacidad total de memoria reservada. | $O(1)$ |
| `is_empty()` | Verifica si el vector no contiene elementos. | $O(1)$ |
| `at(index)` | Obtiene el elemento en un índice específico validando límites. | $O(1)$ |
| `push(item)` | Agrega un elemento al final (redimensiona si está lleno). | $O(1)$ amortizado |
| `insert(index, item)` | Inserta un elemento en un índice desplazando los demás a la derecha. | $O(N)$ |
| `prepend(item)` | Inserta un elemento al inicio (equivalente a `insert(0, item)`). | $O(N)$ |
| `pop()` | Elimina y retorna el último elemento del vector. | $O(1)$ |
| `delete(index)` | Elimina el elemento en un índice y desplaza los elementos a la izquierda. | $O(N)$ |
| `remove(item)` | Busca todas las apariciones de un valor y elimina sus índices. | $O(N)$ |
| `find(item)` | Busca un valor y retorna su primer índice (o `-1` si no existe). | $O(N)$ |
| `resize(nueva_capacidad)` | Duplica o ajusta el array subyacente copiando los elementos (*Privada*). | $O(N)$ |

---

## Detalle Explicativo de Cada Función

### 1. `size()` – Número de elementos
* **Qué hace:** Devuelve el número actual de elementos almacenados activamente en el vector (`self.size`), no la capacidad máxima que tiene reservada.
* **Por qué importa:** Permite conocer los límites reales de datos válidos sin exponer la memoria subyacente vacía.

### 2. `capacity()` – Número de elementos soportados
* **Qué hace:** Retorna el tamaño total del array en memoria (`self.capacity`).
* **Por qué importa:** Indica cuántos elementos puede almacenar el vector antes de que sea necesario disparar una operación de redimensionamiento (`resize`).

### 3. `is_empty()` – Verificación de vacío
* **Qué hace:** Evalúa si el tamaño del vector es igual a 0 (`size() == 0`).
* **Por qué importa:** Es una validación lógica esencial antes de realizar operaciones de lectura (`at`) o eliminación (`pop`) para evitar errores por desbordamiento o índices vacíos.

### 4. `at(index)` – Obtener elemento por índice
* **Qué hace:** Regresa el elemento ubicado en el índice proporcionado. 
* **Control de errores:** **Falla y lanza una excepción** (como `IndexOutOfBoundsException` o `IndexError`) si el índice es menor que 0 o mayor/igual que el tamaño actual (`size`). Garantiza acceso directo en tiempo constante $O(1)$.

### 5. `push(item)` – Inserción al final
* **Qué hace:** Añade un nuevo elemento al final del vector.
* **Funcionamiento interno:** 
  1. Comprueba si `size == capacity`.
  2. Si está lleno, llama automáticamente a `resize()` para duplicar el espacio.
  3. Inserta el elemento en la posición `size` e incrementa el tamaño en 1.

### 6. `insert(index, item)` – Inserción en posición específica
* **Qué hace:** Inserta un elemento en un índice arbitrario.
* **Funcionamiento interno:** 
  1. Valida que el índice sea válido.
  2. Si el vector está lleno, redimensiona la capacidad.
  3. **Desplaza todos los elementos** desde el índice dado una posición hacia la derecha para hacerle espacio al nuevo valor.
  4. Asigna el elemento en el índice e incrementa el tamaño.
* **Costo:** Al implicar desplazamiento, su complejidad es $O(N)$.

### 7. `prepend(item)` – Inserción al inicio
* **Qué hace:** Inserta un elemento directamente en la primera posición (equivalente conceptual a `insert(0, item)`).
* **Funcionamiento interno:** Desplaza todos los elementos existentes una posición hacia la derecha y coloca el nuevo elemento en el índice `0`. Al igual que `insert`, su costo es $O(N)$.

### 8. `pop()` – Extracción del último elemento
* **Qué hace:** Remueve el último elemento del vector, libera su referencia (limpiando posibles fugas de memoria) y **devuelve su valor**.
* **Costo:** $O(1)$, ya que no requiere ningún tipo de desplazamiento.

### 9. `delete(index)` – Eliminación por índice
* **Qué hace:** Elimina el elemento ubicado en un índice específico.
* **Funcionamiento interno:**
  1. Guarda temporalmente el valor a eliminar.
  2. **Desplaza todos los elementos** a la derecha del índice una posición hacia la izquierda para rellenar el espacio vacío.
  3. Limpia la última posición sobrante y decrementa el tamaño en 1.
* **Costo:** $O(N)$ debido al reacomodo de los elementos.

### 10. `remove(item)` – Eliminación por valor
* **Qué hace:** Busca un valor específico dentro del vector y **elimina todas las ocurrencias** que lo contengan (o la primera, dependiendo de la implementación deseada).
* **Funcionamiento interno:** Recorre el vector buscando coincidencias con el ítem y ejecuta un proceso similar a `delete` para cada índice encontrado. Su costo es $O(N)$ por la búsqueda y el reordenamiento.

### 11. `find(item)` – Búsqueda de valor
* **Qué hace:** Recorre el vector secuencialmente en busca del valor proporcionado.
* **Salida:** Regresa el **primer índice** donde encuentra una coincidencia. Si el elemento no existe en el vector, devuelve `-1`.
* **Costo:** $O(N)$ en el peor de los casos (cuando el elemento está al final o no existe).

### 12. `resize(nueva_capacidad)` – Función Privada de Redimensionamiento
* **Qué hace:** Es el motor interno de la flexibilidad del vector. 
* **Funcionamiento interno:**
  1. Crea un nuevo bloque de memoria (un nuevo array auxiliar) con la `nueva_capacidad` (típicamente el doble de la actual).
  2. Copia uno a uno los elementos del array antiguo al nuevo array mediante un bucle.
  3. Reemplaza la referencia del array antiguo por el nuevo array.
* **Costo:** $O(N)$ temporalmente, pero al duplicar la capacidad, su costo se "amortiza" a $O(1)$ por cada inserción individual a largo plazo.