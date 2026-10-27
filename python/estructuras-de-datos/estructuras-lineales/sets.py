# Creación
unicos = {1, 2, 3, 2, 1}
print(unicos)  # Output: {1, 2, 3} (elimina duplicados)

# Inserción y búsqueda
unicos.add(4)  # O(1)
if 3 in unicos:  # O(1) promedio
  print("El 3 está en el conjunto")