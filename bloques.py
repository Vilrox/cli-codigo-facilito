#Función para leer un archivo en particular:

def mostrar_contenido(ruta_archivo):
    if ruta_archivo.is_file and ruta_archivo.exists():
        return ruta_archivo.read_text()

#Para mandar a llamar la función:
contenido = mostrar_contenido(path_canciones / "song_1.txt" )


#Para leer TODOS los arcivos con extensión .txt
for dir in path_canciones.iterdir():
        if dir.is_file() and dir.suffix == ".txt":
            contenido = dir.read_text()
            print(contenido)