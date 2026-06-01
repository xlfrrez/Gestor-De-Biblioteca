def ver_historial(usuario):
    print(f"\nHistorial de {usuario.nombre}")
    for h in usuario.historial:
        print("-",h)
        
