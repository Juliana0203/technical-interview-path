# Creación
edades = {"Ana": 25, "Carlos": 30}

# Inserción / Actualización
edades["Lucia"] = 22  # O(1) promedio

# Búsqueda segura
if "Ana" in edades:  # O(1) promedio
  print(edades["Ana"])

# Eliminar
del edades["Carlos"]