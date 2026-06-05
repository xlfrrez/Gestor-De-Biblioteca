class Biblioteca:
  def __init__(self):
    self.libros = []
    self.usuarios = []

  
  def agregar_libro(self, libro):
      self.libros.append(libro)
    
  def registrar_usuario(self, usuario):
      self.usuarios.append(usuario)
    
  def buscar(self, texto):
      resultados = []
      for l in self.libros:
        if texto.lower() in l.titulo.lower() or texto.lower() in l.autor.lower() or texto.lower() in l.genero.lower():
          resultados.append(l)
      return resultados

  
  def prestar(self, libro, usuario):
      if libro.estado == "disponible" and usuario.puede_prestar():
        libro.estado = "prestado"
        usuario.libros_prestados.append(libro)
        usuario.historial.append(f"Prestado:{libro.titulo}")
        print("Libro prestado")
      else:
        print("No se puede prestar")

  
  def devolver(self, libro, usuario):
      if libro in usuario.libros_prestados:
        libro.estado = "disponible"
        usuario.libros_prestados.remove(libro)
        usuario.historial.append(f"Devuelto:{libro.titulo}")
        print("Libro devuelto")
