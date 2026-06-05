def eliminar_libro(biblioteca, titulo):
   for l in biblioteca.libros:
      if l.titulo.lower() == titulo.lower():
        biblioteca.libros.remove(l)
        print("Libro eliminado")
        return
   print("No encontrado")

def eliminar_usuario(biblioteca, nombre):
    for u in biblioteca.usuarios:
        if u.nombre.lower() == nombre.lower():
            biblioteca.usuarios.remove(u)
            print("Usuario eliminado")
            return
    print("No encontrado")
