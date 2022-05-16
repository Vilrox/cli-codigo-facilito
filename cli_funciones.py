#Definir funciones del programa:

def imprimir_menu():
    print("\tMenú de opciones:")
    print("\t\t")
    print("\t\t[a] Listar documentos.")
    print("\t\t[b] Leer un documento.")
    print("\t\t[c] Editar un documento.")
    print("\t\t[x] Salir.")
    
def clear(): 
    print("\n" * 2)

def continuar():
    print("Presiona 'enter' para continuar") 

def mostrar_contenido(ruta_archivo):
    if ruta_archivo.is_file and ruta_archivo.exists():
        return ruta_archivo.read_text()