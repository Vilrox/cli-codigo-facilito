#1. Importar la librería Path de Python
from pathlib import Path 

#Mostrar Bienvenida al usuario.
print("""
Bienvenid@ al CLI de archivos en el Sistema.
Este es el directorio en el cual te encuentras: 
""")
#2. Mostrar la ruta del directorio actual   
print(Path.cwd()) #PENDIENTE: Buscar cómo poner las letras en cursiva

#Guardar nuestra ruta actual en una variable
directorio_actual = Path.cwd() #Conocer en qué directorio estamos ubicados

#3. Crear un objeto de tipo Path, que será capaz de moverse en los diferentes directorios
path = Path(directorio_actual)

#Crear carpeta que contenga los archivos
path_canciones = path / "canciones"
lista_canciones = path_canciones / "lista.txt"

if not path_canciones.exists():
    path_canciones.mkdir()

#Mover los archivos .txt en la carpeta creada




#4. Definir funciones:
def clear(): 
    print("\n" * 3)

def continuar():
    print("Presiona 'enter' para continuar") 

def mostrar_contenido(ruta_archivo):
    if ruta_archivo.is_file and ruta_archivo.exists():
        return ruta_archivo.read_text()

while True:
    try:
        print("""¿Qué tarea deseas realizar:
        Menú de opciones:
            Presiona a para Listar documentos.
            Presiona b para Leer un documento.
            Presiona c para Editar un documento.
            Presiona x para Salir.""")

        opcion = input()
    
        if opcion == "a":
            print("Vas a listar documentos con extensión .txt\n")
            if path_canciones.is_dir():
                for dir in path_canciones.iterdir():

                    if dir.is_file() and dir.suffix == ".txt":
                        print("Nombre: ", dir.name)

            clear()
            continuar()
            input()

        elif opcion == "b":
            print("Vas a leer un documento.\n")
            cancion = input("Ingresa el nombre del archivo: ")
            contenido = mostrar_contenido(path_canciones / cancion )
            print(contenido)
            clear()
            continuar()
            input()

        elif opcion == "c":
            print("Vas a editar un documento\n")

            with open(lista_canciones, "w") as file:
                file.write("Lista de canciones favoritas: ")
                file.close()

            cancion_favorita = input("¿Cuál es tu canción favorita?:\n")

            with open(lista_canciones, "a+") as file:
                file.write(cancion_favorita)
            
            clear()
            print("Puedes verla en el archivo 'lista.txt'")x
            continuar()
            input()  
            
        elif opcion == "x": 
            print("Vas a salir del sistema")
            input()
            break
    except:
        clear()

