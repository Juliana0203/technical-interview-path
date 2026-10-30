# Guía Definitiva de Tablas Hash (Hash Maps)

Una **Tabla Hash** (conocida como `dict` en Python, `HashMap` en Java o `Dictionary` en C#) es una estructura de datos fundamental que almacena información en formato de **Pares Clave-Valor (Key-Value)**. Es una de las herramientas más potentes en ciencias de la computación debido a su velocidad para recuperar información.

---

## Resumen de Métodos y Complejidad Temporal

| Operación | Descripción | Complejidad Promedio | Complejidad en el Peor Caso |
| :--- | :--- | :--- | :--- |
| `put(key, value)` / `dict[key] = val` | Inserta o actualiza un par clave-valor. | $O(1)$ | $O(N)$ |
| `get(key)` / `dict[key]` | Obtiene el valor asociado a una clave. | $O(1)$ | $O(N)$ |
| `remove(key)` / `del` | Elimina una clave y su valor asociado. | $O(1)$ | $O(N)$ |
| `contains(key)` / `in` | Verifica si una clave existe en la tabla. | $O(1)$ | $O(N)$ |

---

## Detalle Explicativo del Funcionamiento

### 1. ¿Cómo funciona internamente?
A diferencia de un array normal (donde buscas por un índice numérico secuencial), una tabla hash utiliza una **Función Hash (Hash Function)**:
1. Le pasas una **Clave** (por ejemplo, el string `"Ana"`).
2. La función hash procesa matemáticamente esa clave y genera un número entero único (código hash).
3. Este número se utiliza para calcular el índice exacto en un array subyacente de memoria donde se guardará el **Valor**.
4. Como resultado, la computadora va directamente a esa posición sin tener que recorrer toda la estructura, logrando un tiempo constante $O(1)$.

### 2. ¿Qué son las Colisiones y el Peor Caso ($O(N)$)?
* **Colisión:** Como el espacio de posibles claves es infinito pero la memoria del array es finita, puede ocurrir que dos claves distintas generen el mismo índice hash.
* **Solución (Encadenamiento / Chaining):** Las buenas implementaciones guardan una pequeña lista de elementos en esa misma posición si ocurre una colisión.
* **Peor Caso ($O(N)$):** Si la función hash es deficiente o demasiadas claves colisionan en la misma posición, la tabla hash se degrada y se comporta como una lista enlazada, donde buscar un elemento requiere recorrerlos todos.

---
