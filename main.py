#1. Importar la librería Path de Python
from pathlib import Path 
import cli_titulo
import cli_funciones

cli_titulo.imprimir_título()
input()
#Mostrar Bienvenida al usuario.
print("""
Bienvenid@ al CLI de archivos en el Sistema.
Este es el directorio en el cual te encuentras: 
""")
#2. Mostrar la ruta del directorio actual   
print(Path.cwd())
print("\n")

cli_funciones.continuar()
input()
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


while True:
    try:
        """
        print("¿Qué tarea deseas realizar:
        Menú de opciones:
            Presiona a para Listar documentos.
            Presiona b para Leer un documento.
            Presiona c para Editar un documento.
            Presiona x para Salir.")"""
        cli_funciones.imprimir_menu()

        opcion = input()
    
        if opcion == "a":
            print("Ésta es la lista de documentos con extensión '.txt':\n")
            if path_canciones.is_dir():
                for dir in path_canciones.iterdir():

                    if dir.is_file() and dir.suffix == ".txt":
                        print("Nombre: ", dir.name)

            cli_funciones.clear()
            cli_funciones.continuar()
            input()

        elif opcion == "b":
            print("Vas a leer un documento.\n")
            cancion = input("Ingresa el nombre del archivo:")
            contenido = cli_funciones.mostrar_contenido(path_canciones / cancion )
            print(contenido)
            cli_funciones.clear()
            cli_continuar()
            input()

        elif opcion == "c":
            print("Vas a editar un documento\n")

            #with open(lista_canciones, "w") as file:
                #file.write("Lista de canciones favoritas: \n")
                #file.close()

            cancion_favorita = input("¿Cuál es tu canción favorita?:\n")

            with open(lista_canciones, "a") as file:
                file.write(cancion_favorita + "\n")
                file.close()
                
            cli_funciones.clear()
            print("Puedes verla en el archivo 'lista.txt'")
            cli_funciones.continuar()
            input()  
            
        elif opcion == "x": 
            print("Vas a salir del sistema")
            input()
            break
        else:
            print("Esta opción no es válida \n")
            #cli_funciones.continuar()
            cli_funciones.clear()
    except:
        cli_funciones.clear()

