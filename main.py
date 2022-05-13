#1. Importar la librería Path de Python
from pathlib import Path 

#Mostrar Bienvenida al usuario.
print("""
Bienvenid@ al CLI de archivos en el Sistema.
Este es el directorio en el cual te encuentras: 
""")
#2. Mostrar la ruta del directorio actual   
print(Path.cwd())

#Guardar nuestra ruta actual en una variable
directorio_actual = Path.cwd() #Conocer en qué directorio estamos ubicados

#3. Crear un objeto de tipo Path
path = Path(directorio_actual)

#4. Definir funciones:
def menu_opciones():
    print("""
    Menú de opciones:
    a) Listar documentos.
    b) Leer un documento.
    c) Editar un documento.
    d) Salir.
    """)


#5. Preguntar al usuario la tarea que desea realizar
menu_opciones()
tarea = input("¿Qué tarea deseas realizar? ")

#while (tarea != "d"):
if tarea == "a":
    print("Vas a listar documentos con extensión .txt")
elif tarea == "b":
    print("Vas a leer un documento.")
elif tarea == "c":
    print("Vas a editar un documento")
elif tarea == "d":
    print("Salir del programa")
else: 
    print("Esa opción no existe")