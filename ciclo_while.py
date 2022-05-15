def clear(): 
    print("\n" * 8)

def continuar():
    print("Presiona 'enter' para continuar") 

while True:
    try:
        print("""¿Qué tarea deseas realizar:
        Menú de opciones:
            Presiona a para Listar documentos.
            Presiona b para Leer un documento.
            Presiona c para Editar un documento.
            Presiona x para Salir.""")

        opcion=input()
        if opcion == "a":
            print("Vas a listar documentos con extensión .txt\n")
            clear()
            continuar()
            input()
        elif opcion == "b":
            print("Vas a leer un documento.\n")
            clear()
            continuar()
            input()
        elif opcion == "c":
            print("Vas a editar un documento\n")
            clear()
            continuar()
            input()
        elif opcion == "x": 
            break
    except:
        print("Esta opción no existe")
        clear()
    