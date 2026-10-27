# Guía de Estructuras de Datos

Las estructuras de datos son formas especializadas de organizar, gestionar y almacenar datos en la memoria de un computador de manera eficiente, permitiendo realizar operaciones de búsqueda, inserción y eliminación con el menor costo posible.

---

## 1. Estructuras Lineales
Los elementos se encuentran secuencialmente, uno tras otro. Cada elemento (excepto el primero y el último) tiene un único predecesor y un único sucesor.

### A. Arrays (Arreglos) / Listas
* **Qué son:** Una colección de elementos almacenados en **posiciones de memoria contiguas**.
* **Ventajas:** Acceso directo e inmediato a cualquier elemento mediante su índice.
* **Desventajas:** Su tamaño es estático (en lenguajes como Java o C++) o requiere redimensionamiento dinámico costoso (como en Python). Insertar o eliminar elementos en el medio requiere desplazar los demás.
* **Complejidades en Python (Listas):**
  * Acceso por índice: $O(1)$
  * Búsqueda por valor: $O(N)$
  * Inserción/Eliminación al final (`append`/`pop`): $O(1)$ amortizado
  * Inserción/Eliminación al inicio o medio (`insert`/`pop(0)`): $O(N)$

### B. Hash Tables (Tablas Hash / Diccionarios)
* **Qué son:** Estructuras que almacenan datos en formato **Clave-Valor (Key-Value)** utilizando una función hash para calcular la posición en memoria donde se guardará el valor.
* **Ventajas:** Búsquedas, inserciones y eliminaciones ultra rápidas en tiempo constante promedio.
* **Complejidades:**
  * Búsqueda / Inserción / Eliminación: $O(1)$ (en el peor caso por colisiones graves: $O(N)$).

### C. Linked Lists (Listas Enlazadas)
* **Qué son:** Secuencia de nodos donde cada nodo contiene un valor y un **puntero (referencia)** al siguiente nodo (y opcionalmente al anterior en listas doblemente enlazadas). No requieren memoria contigua.
* **Ventajas:** Inserciones y eliminaciones muy eficientes $O(1)$ si ya tienes la referencia al nodo, ya que solo cambias punteros sin mover bloques de memoria.
* **Desventajas:** No hay acceso aleatorio; para buscar un elemento hay que recorrer la lista secuencialmente desde la cabeza ($O(N)$).

### D. Stacks (Pilas) y Queues (Colas)
* **Stacks (Pilas):** Siguen el principio **LIFO** (*Last In, First Out* — El último en entrar es el primero en salir). Piensa en una pila de platos. Operaciones principales: `push` (añadir) y `pop` (sacar) en $O(1)$.
* **Queues (Colas):** Siguen el principio **FIFO** (*First In, First Out* — El primero en entrar es el primero en salir). Piensa en una fila de personas en el banco. Operaciones principales: `enqueue` (entrar) y `dequeue` (salir) en $O(1)$ si se usan estructuras adecuadas (como `collections.deque` en Python).

---

## 2. Estructuras No Lineales
Los elementos no están organizados de forma secuencial, sino jerárquica o en red, donde un elemento puede conectarse a múltiples elementos.

### A. Trees (Árboles)
* **Qué son:** Estructuras jerárquicas compuestas por un **Nodo Raíz (Root)** y ramas de subnodos hijos. 
* **Binary Trees (Árboles Binarios):** Cada nodo tiene a lo sumo dos hijos (izquierdo y derecho).
* **Binary Search Trees (BST - Árboles de Búsqueda Binaria):** Un árbol binario especial donde el hijo izquierdo es menor que el nodo padre, y el hijo derecho es mayor. Esto permite búsquedas eficientes en $O(\log N)$ si el árbol está balanceado.

### B. Heaps (Montículos / Priority Queues)
* **Qué son:** Árboles binarios completos que satisfacen la propiedad de orden de heap: 
  * *Max-Heap:* El padre es siempre mayor o igual que sus hijos (el mayor está en la raíz).
  * *Min-Heap:* El padre es siempre menor o igual que sus hijos (el menor está en la raíz).
* **Uso principal:** Implementar colas de prioridad donde necesitas extraer el elemento mínimo o máximo constantemente en $O(\log N)$.

### C. Graphs (Grafos)
* **Qué son:** Conjunto de **Vértices (Nodos)** conectados por **Aristas (Edges)**. Sirven para modelar redes complejas (redes sociales, mapas de navegación, rutas de internet).
* **Tipos:** Dirigidos (con sentido de flujo) o No dirigidos; Ponderados (con costos en las aristas) o No ponderados.
* **Representación:** 
  * Matriz de Adyacencia ($O(V^2)$ espacio).
  * Lista de Adyacencia ($O(V + E)$ espacio, la más utilizada).

---

## Resumen de Cuándo Usar Qué

| Problema / Necesidad | Estructura Ideal |
| :--- | :--- |
| Buscar elementos rápidamente por clave o ID | **Hash Table / Diccionario** |
| Mantener un historial de "deshacer" (Undo) o procesamiento secuencial inverso | **Stack (Pila)** |
| Procesar tareas en orden de llegada (Atención al cliente, BFS) | **Queue (Cola)** |
| Búsquedas rápidas en datos ordenados o rangos | **Binary Search Tree (BST)** |
| Obtener siempre el elemento más pequeño o más grande eficientemente | **Min/Max Heap** |
| Modelar relaciones de red, conexiones o rutas | **Grafo** |