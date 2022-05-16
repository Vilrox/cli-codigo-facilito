#Definir funciones del programa:

#Función que pinta el menú de opciones:
def imprimir_menu():
    print("\t¿Qué tarea deseas realizar?")
    print("\tMenú de opciones:")
    print("\t\t")
    print("\t\t[a] Listar documentos.")
    print("\t\t[b] Leer un documento.")
    print("\t\t[c] Editar un documento.")
    print("\t\t[x] Salir.")

#Función para limpiar consola:   
def clear(): 
    print("\n" * 2)

#Función para continuar con el programa:
def continuar():
    print("Presiona 'enter' para continuar") 

#Función para mostrar el contenido de un archivo:
def mostrar_contenido(ruta_archivo):
    if ruta_archivo.is_file and ruta_archivo.exists():
        return ruta_archivo.read_text()