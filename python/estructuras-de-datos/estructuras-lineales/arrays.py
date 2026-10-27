# Creación e inserción
mi_lista = [10, 20, 30]
mi_lista.append(40)  # O(1) al final
mi_lista.insert(0, 5)  # O(N) al inicio (desplaza los elementos)

# Acceso y modificación
primero = mi_lista[0]  # O(1) -> 5
mi_lista[1] = 99  # Modificar por índice

# Eliminación
ultimo = mi_lista.pop()  # O(1) saca el último
primero = mi_lista.pop(0)  # O(N) saca el primero