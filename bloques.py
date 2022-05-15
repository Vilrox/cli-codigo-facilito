#Función para leer un archivo en particular:

def mostrar_contenido(ruta_archivo):
    if ruta_archivo.is_file and ruta_archivo.exists():
        return ruta_archivo.read_text()

#Para mandar a llamar la función:
contenido = mostrar_contenido(path_canciones / "we_are_the_world.txt" )


#Para leer TODOS los archivos con extensión .txt
for dir in path_canciones.iterdir():
        if dir.is_file() and dir.suffix == ".txt":
            contenido = dir.read_text()
            print(contenido)

#Para añadir a un archivo 
with open(path_canciones, "a") as archivo:
    archivo.write("Escribe tus canciones favoritas")
    archivo.close()
