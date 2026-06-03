class Usuario:
  def __init__(self, nombre, id_usuario):
    self.nombre = nombre
    self.id_usuario = id_usuario
    self.libros_prestados = []
    self.historial = []
    
  def puede_prestar(self):
    return len(self.libros_prestados) < 3
