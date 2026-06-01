from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.biblioteca import Biblioteca

from funciones.reportes import *
from funciones.validaciones import *
from funciones.historial import *
from funciones.estadisticas import *
from funciones.eliminar import *


def menu():
  biblioteca = Biblioteca()

  
  while true:
    print("\n===== BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro")
    print("6. Ver libros disponibles")
    print("7. Ver estadisticas")
    print("8. Ver historial de usuario")
    print("9. Eliminar libro")
    print("10. Eliminar usuario")
    print("11. Salir")
    
    opcion = input("Opcion: ")
    match opcion:
    case "1":
      biblioteca.agregar_libro(
        Libro(input("Titulo: "), input("Genero: "), input("Año: "))
      )
    case "2":
      biblioteca.registrar_usuario(
        
