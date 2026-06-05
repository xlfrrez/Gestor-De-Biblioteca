class Libro:
    def __init__(self, titulo, autor, genero, año):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año
        self.estado = "disponible"

    def mostrar(self):
         print(f"{self.titulo} | {self.autor} | {self.genero} | {self.año} | {self.estado}")
         
