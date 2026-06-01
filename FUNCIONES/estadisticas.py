def estadisticas(biblioteca):
  total = len(biblioteca.libros)
  prestados = len([l for l in biblioteca.libros if l.estado == "prestado"])
  disponibles = total - prestados

print("\n Estadisticas")
print("Total de Libros:", total)
print("Prestados:", prestados)
print("Disponibles:", disponibles)
