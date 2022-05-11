#1. Importar la librería Path de Python
from pathlib import Path 

print("""
Bienvenid@ al CLI de archivos en el Sistema.
Este es el directorio en el cual te encuentras: 
""")
#2. Obtener la ruta del directorio actual   
print(Path.cwd())

#3. Crear un objeto de tipo Path
directorio_actual = Path.cwd() #Conocer en qué directorio estamos ubicados
path = Path(directorio_actual)#Crear un objeto de tipo Path

#4. Mostrarle al usuario las opciones a elegir
print("""
Menú de opciones:
a) Listar documentos.
b) Leer un documento.
c) Editar un documento.
d) Salir.
""")
#5. Preguntar al usuario la tarea que desea realizar
listar = print(input("¿Qué tarea deseas realizar? "))
