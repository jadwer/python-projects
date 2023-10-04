import time
import os
import shutil
import random

from watchdog.observers  import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'desorganizados'
to_dir = 'organizados'

dir_tree = {
    "image_files": ['.jpg', '.jpeg', '.webp', '.png', '.gif', '.jfif']
}

# Clase Event Handler
class FileMovementHandler(FileSystemEventHandler) :
    def on_created(self, event):
        print(event)
        name, extension = os.path.splitext(event.src_path)
        print(extension)
        for key, value in dir_tree.items() :
            print("Key:" + key)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                full_origin = from_dir + '/' + file_name
                directory = to_dir + '/' + key
                full_destination = directory + '/' + file_name

                print("file_name:" + file_name)
                print("full_origin: " + full_origin)
                print("directory: " + directory)
                print("full_destination: " + full_destination)

                # time.sleep(3)

                if os.path.exists(directory):
                    print("El directorio existe...")

                    if os.path.exists(full_destination) :

                        print("Ese nombre de archivo ya existe en: " + key + "....")
                        print("Renombrando el archivo " + file_name + "....")

                        new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0,999)) + os.path.splitext(file_name)[1]

                        new_full_destination = directory + '/' + new_file_name
    
                        print("Moviendo archivo " + file_name + ".....")
                        # Mueve de origen a destino
                        shutil.move(full_origin, new_full_destination)
                    else :
                        print("Moviendo archivo " + file_name + ".....")
                        # Mueve de origen a destino
                        shutil.move(full_origin, full_destination)
                else : # el directory no existe, lo creamos
                    os.makedirs(directory)
                    print("Moviendo archivo " + file_name + ".....")
                    # Mueve de origen a destino
                    shutil.move(full_origin, full_destination)



# Instancia nuestra clase
event_handler = FileMovementHandler()

# Inicia Observer
observer = Observer()

# Programa observer
observer.schedule(event_handler, from_dir, recursive=True)
print(observer)
# Inicia el observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("Ejecutando...")
except KeyboardInterrupt :
    print("¡Deteniendo!")
    observer.stop()


