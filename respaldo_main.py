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
def menu_opciones():
    print("""
    Menú de opciones:
    a) Listar documentos.
    b) Leer un documento.
    c) Editar un documento.
    d) Salir.
    """)

def opcion():
    pass
    

def mostrar_contenido(ruta_archivo):
    if ruta_archivo.is_file and ruta_archivo.exists():
        return ruta_archivo.read_text()





#5. Preguntar al usuario la tarea que desea realizar
menu_opciones()


tarea = input(YELLOW+"¿Qué tarea deseas realizar?\n")
#while (tarea != "d"):
if tarea == "a":
    print("Vas a listar documentos con extensión .txt")
    #input("¿Conoces el nombre del archivo?") #Esto se puede hacer en una función
    #Para que se repita en las tres opciones

    if path_canciones.is_dir():
        for dir in path_canciones.iterdir():

            if dir.is_file() and dir.suffix == ".txt":
                print("Nombre: ", dir.name)

    menu_opciones()

   

elif tarea == "b":
    print("Vas a leer un documento.")

    cancion = input("Ingresa el nombre del archivo: ")

    
    contenido = mostrar_contenido(path_canciones / cancion )
    print(contenido)

    

elif tarea == "c":
    print("Vas a editar un documento")

    with open(lista_canciones, "w") as file:
        file.write("Lista de canciones favoritas: ")
        file.close()

    cancion_favorita = input("¿Cuál es tu canción favorita?:\n")

    with open(lista_canciones, "a+") as file:
        file.write(cancion_favorita)
    
elif tarea == "d":
    print("Salir del programa")
else: 
    print("Esa opción no existe")