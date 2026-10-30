# Guía Completa de Pilas (Stacks) y Colas (Queues)

Las **Pilas** y **Colas** son estructuras de datos lineales fundamentales que imponen restricciones específicas sobre cómo se pueden insertar y extraer los elementos. A diferencia de los arrays o listas genéricas, no puedes acceder a cualquier elemento de forma arbitraria; solo puedes interactuar con los extremos de la estructura.

---

## 1. Stacks (Pilas — LIFO)

Una **Pila** sigue el principio **LIFO** (*Last In, First Out* — El último en entrar es el primero en salir). Piensa en una pila de platos en una cafetería: solo puedes poner un plato nuevo arriba de todo, y solo puedes retirar el plato que está hasta arriba.

### Métodos y Complejidad Temporal (Pilas)

| Método | Descripción | Complejidad Temporal |
| :--- | :--- | :--- |
| `push(item)` | Agrega un elemento a la parte superior de la pila. | $O(1)$ |
| `pop()` | Elimina y retorna el elemento de la parte superior. | $O(1)$ |
| `peek()` / `top()` | Consulta el valor superior sin eliminarlo. | $O(1)$ |
| `is_empty()` | Verifica si la pila no contiene elementos. | $O(1)$ |
| `size()` | Retorna el número total de elementos en la pila. | $O(1)$ |

### Detalle Explicativo de Pilas
- **`push(item)`:** Coloca el elemento en la cima de la pila. Si se implementa usando un array dinámico o una lista enlazada por el frente, su costo es constante $O(1)$.
- **`pop()`:** Remueve el elemento que está arriba de todo y lo devuelve. Es crucial para algoritmos de retroceso (*backtracking*), evaluación de expresiones matemáticas y el manejo de la pila de llamadas (*call stack* en recursión).
- **`peek()`:** Permite "espiar" el valor actual que se encuentra en la cima sin alterar la estructura.

---

## 2. Queues (Colas — FIFO)

Una **Cola** sigue el principio **FIFO** (*First In, First Out* — El primero en entrar es el primero en salir). Piensa en una fila de personas esperando en la taquilla del cine: la primera persona que llega es la primera en ser atendida y salir.

### Métodos y Complejidad Temporal (Colas)

| Método | Descripción | Complejidad Temporal |
| :--- | :--- | :--- |
| `enqueue(item)` / `push()` | Agrega un elemento al final (detrás) de la cola. | $O(1)$ |
| `dequeue()` / `pop()` | Elimina y retorna el elemento del inicio (frente) de la cola. | $O(1)$ *(usando estructuras optimizadas)* |
| `front()` / `peek()` | Consulta el valor del primer elemento sin eliminarlo. | $O(1)$ |
| `is_empty()` | Verifica si la cola no contiene elementos. | $O(1)$ |
| `size()` | Retorna el número total de elementos en la cola. | $O(1)$ |

### Detalle Explicativo de Colas
- **`enqueue(item)`:** Añade un nuevo elemento en la parte posterior de la cola.
- **`dequeue()`:** Remueve el elemento que está al frente. *Advertencia en Python:* Si usas una lista normal y haces `pop(0)`, desplazas todos los elementos restantes, lo que cuesta $O(N)$. Por ello, para implementar colas eficientes siempre se debe usar `collections.deque`, que permite extracciones al frente en $O(1)$.
- **Aplicaciones principales:** Se utilizan en sistemas de procesamiento de tareas asíncronas, impresoras en red, y en algoritmos de grafos como **BFS (Breadth-First Search)**.

---

## ¿Cómo se implementan en Python?

* **Pila (Stack):** Se puede usar directamente una lista normal de Python utilizando `append()` para hacer `push` y `pop()` para extraer el último elemento.
* **Cola (Queue):** Se debe importar `deque` desde el módulo `collections`, usando `append()` para entrar y `popleft()` para salir eficientemente.