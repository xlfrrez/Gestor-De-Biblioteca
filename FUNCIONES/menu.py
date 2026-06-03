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
        Usuario(input("Nombre: "), input("Autor: "), input("Genero: "), input("Año: "))
      )

    
    case "3":
      t = input("Libro: ")
      u = input("Usuario: ")
      
      usuario = next((x for x in biblioteca.usuarios if x.nombre == u), None)
      libro = next((x for x in biblioteca.libros if x.titulo == t), None)

      
      if usuario and libro:
        biblioteca.prestar(libro, usuario)

    
    case "4":
      t = input("Libro: ")
      u = input("Usuario: ")

      
      usuario = next((x for x in biblioteca.usuarios if x.nombre == u), None)
      libro = next((x for x in biblioteca.libros if x.titulo == t), None)

      
      if usuario and libro:
        biblioteca.devolver(libro, usuario)

    
    case "5":
      texto = input("Buscar: ")
      for l in biblioteca.buscar(texto):
        l.mostrar()

    
    case "6":
      libros_disponibles(biblioteca)

    
    case "7":
      estadisticas(biblioteca)

    
    case "8":
      nombre = input("Usuario: ")
      usuario = next((x for x in biblioteca.usuarios if x.nombre == nombre), None)
      if usuario:
        ver_historial(usuario)

    
    case "9":
      eliminar_libro(biblioteca, input("Tutulo: "))

    
    case "10":
      eliminar_usuario(biblioteca, input("Nombre: "))

    
    case "11":
      break
