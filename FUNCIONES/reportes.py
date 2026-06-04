def libros_disponibles(biblioteca):
  print("\n LIBROS DISPONIBLES")
  for l in biblioteca.libros:
    if l.estado == "disponible":
      l.mostrar()

def libros_prestados(biblioteca):
  print("\n LIBROS PRESTADOS")
  for l in biblioteca.libros:
    if l.estado == "prestado":
      l.mostrar()

def usuarios_registrados(biblioteca):
  print("\n USUARIOS")
  for u in biblioteca.usuarios:
    print(u.nombre, "-", u.id_usuario)
