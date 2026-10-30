# Guía Completa de Métodos y Funciones de una Lista Enlazada (Linked List)

Una **Lista Enlazada** es una estructura de datos lineal compuesta por una cadena de **Nodos**. A diferencia de los vectores dinámicos (que usan memoria contigua), cada nodo contiene un valor de datos y un puntero que referencia al siguiente nodo. Esto permite inserciones y eliminaciones muy eficientes sin necesidad de desplazar bloques enteros de memoria.

---

## Resumen de Métodos y Complejidad Temporal

| Método | Descripción | Complejidad Temporal |
| :--- | :--- | :--- |
| `size()` | Retorna el número de elementos en la lista. | $O(N)$ |
| `empty()` | Retorna `True` si la lista está vacía. | $O(1)$ |
| `value_at(index)` | Retorna el valor del elemento en el índice dado (empezando en 0). | $O(N)$ |
| `push_front(value)` | Agrega un elemento al inicio de la lista. | $O(1)$ |
| `pop_front()` | Elimina el primer elemento y retorna su valor. | $O(1)$ |
| `push_back(value)` | Agrega un elemento al final de la lista. | $O(N)$ |
| `pop_back()` | Elimina el último elemento y retorna su valor. | $O(N)$ |
| `front()` | Obtiene el valor del primer elemento sin eliminarlo. | $O(1)$ |
| `back()` | Obtiene el valor del último elemento sin eliminarlo. | $O(N)$ |
| `insert(index, value)` | Inserta un valor en un índice específico, actualizando enlaces. | $O(N)$ |
| `erase(index)` | Elimina el nodo ubicado en el índice dado. | $O(N)$ |
| `value_n_from_end(n)` | Retorna el valor del nodo situado a `n` posiciones desde el final. | $O(N)$ |
| `reverse()` | Invierte los punteros de toda la lista en el lugar. | $O(N)$ |
| `remove_value(value)` | Elimina el primer nodo que coincida con el valor especificado. | $O(N)$ |

---

## Detalle Explicativo de Cada Función

### 1. `size()` – Número de elementos
- **Qué hace:** Recorre la lista desde la cabeza (`head`) hasta el final, contando cuántos nodos existen.
- **Funcionamiento interno:** Inicia un contador en 0 y un puntero temporal en `head`. Mientras el puntero no sea nulo (`None`), avanza al siguiente nodo e incrementa el contador.
- **Costo:** $O(N)$.

### 2. `empty()` – Verificación de vacío
- **Qué hace:** Evalúa si la lista no contiene elementos.
- **Funcionamiento interno:** Retorna `True` si la cabeza de la lista es nula (`self.head is None`), o `False` en caso contrario.
- **Costo:** $O(1)$.

### 3. `value_at(index)` – Obtener valor por índice
- **Qué hace:** Busca y devuelve el valor almacenado en el nodo ubicado en el índice numérico especificado (empezando desde `0`).
- **Control de errores:** Avanza paso a paso desde el `head` exactamente `index` veces. Si el índice supera el tamaño de la lista, lanza un error de límites (`IndexError`).
- **Costo:** $O(N)$, ya que las listas enlazadas no permiten acceso aleatorio directo.

### 4. `push_front(value)` – Inserción al inicio
- **Qué hace:** Crea un nuevo nodo con el valor dado y lo coloca como el nuevo inicio de la lista.
- **Funcionamiento interno:** 
  1. Se instancia un nuevo nodo.
  2. Se hace que el puntero `next` del nuevo nodo apunte al actual `head`.
  3. Se actualiza el `head` para que ahora sea este nuevo nodo.
- **Costo:** $O(1)$, ya que toma un número fijo de pasos sin importar el tamaño de la lista.

### 5. `pop_front()` – Eliminación al inicio
- **Qué hace:** Remueve el primer nodo de la lista y devuelve su valor.
- **Funcionamiento interno:** 
  1. Si la lista está vacía, lanza una excepción.
  2. Guarda temporalmente el valor del nodo en el `head`.
  3. Mueve el puntero `head` para que apunte al segundo nodo (`head = head.next`).
  4. Retorna el valor guardado.
- **Costo:** $O(1)$.

### 6. `push_back(value)` – Inserción al final
- **Qué hace:** Añade un nuevo nodo al final absoluto de la lista enlazada.
- **Funcionamiento interno:** 
  1. Si la lista está vacía, actúa igual que `push_front`.
  2. Si tiene elementos, recorre la lista completa desde el `head` hasta encontrar el último nodo (aquel cuyo `next` sea `None`).
  3. Cambia el `next` de ese último nodo para que apunte al nuevo nodo creado.
- **Costo:** $O(N)$ debido a la necesidad de recorrer toda la cadena.

### 7. `pop_back()` – Extracción del último elemento
- **Qué hace:** Remueve el último nodo de la lista y retorna su valor.
- **Funcionamiento interno:** 
  1. Si la lista está vacía o tiene un solo elemento, maneja el caso ejecutando `pop_front`.
  2. Se recorre la lista hasta llegar al **penúltimo** nodo.
  3. Se guarda el valor del último nodo, y se hace que el `next` del penúltimo nodo sea `None`.
- **Costo:** $O(N)$.

### 8. `front()` – Obtener el primer valor
- **Qué hace:** Retorna el valor del nodo en el `head` sin modificar ni eliminar nada.
- **Costo:** $O(1)$.

### 9. `back()` – Obtener el último valor
- **Qué hace:** Recorre la lista hasta llegar al último nodo y retorna su valor.
- **Costo:** $O(N)$.

### 10. `insert(index, value)` – Inserción en posición específica
- **Qué hace:** Inserta un valor en un índice arbitrario, reestructurando los enlaces.
- **Funcionamiento interno:** 
  1. Si el índice es `0`, equivale a `push_front`.
  2. Se avanza hasta el nodo ubicado en el índice `index - 1`.
  3. Se crea el nuevo nodo cuyo `next` apuntará al nodo que originalmente ocupaba esa posición, y se actualiza el `next` del nodo anterior para que apunte al nuevo.
- **Costo:** $O(N)$.

### 11. `erase(index)` – Eliminación por índice
- **Qué hace:** Remueve el nodo ubicado exactamente en el índice dado.
- **Funcionamiento interno:** 
  1. Si el índice es `0`, equivale a `pop_front`.
  2. Se navega hasta el nodo en la posición `index - 1`.
  3. Se ajusta el puntero `next` para que "salte" el nodo a eliminar y apunte directamente al siguiente.
- **Costo:** $O(N)$.

### 12. `value_n_from_end(n)` – Búsqueda desde el final
- **Qué hace:** Encuentra y devuelve el valor del nodo situado a `n` posiciones contando desde el final hacia atrás.
- **Funcionamiento interno:** Utiliza la técnica de **dos punteros** (un puntero rápido que se adelanta `n` pasos y un puntero lento que avanza junto con él hasta que el rápido llega al final).
- **Costo:** $O(N)$.

### 13. `reverse()` – Invertir la lista
- **Qué hace:** Invierte la dirección de los punteros de toda la lista de forma que el último nodo pase a ser el primero y viceversa.
- **Funcionamiento interno:** Utiliza variables de seguimiento (`prev`, `current`, `next_node`) en un bucle iterativo para reorientar cada enlace `next` hacia atrás paso a paso.
- **Costo:** $O(N)$.

### 14. `remove_value(value)` – Eliminación por valor
- **Qué hace:** Busca la primera aparición de un nodo que contenga el valor especificado y lo elimina de la lista.
- **Funcionamiento interno:** Se recorre la lista comparando el valor de cada nodo. Si se encuentra, se ajustan los punteros del nodo anterior para saltarlo.
- **Costo:** $O(N)$.