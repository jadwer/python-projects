import os
import shutil

# origen
from_dir = "/Users/jadwer/dev/shay/python/c112/desorganizados"
# destino
to_dir = "/Users/jadwer/dev/shay/python/c112/organizados"
# Tipos de archivo

#images = ['.gif', '.jpg', '.png', '.jpeg', '.jfif']
#documents = ['.pdf', '.doc', '.docx', '.txt']

# ver la lista de archivos
list_of_files = os.listdir(from_dir)
# print(list_of_files)


# Validar tipo de archivo
# mover archivo al destino correspondiente
for file_name in list_of_files :
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if(extension == '') :
        continue
    if extension in ['.gif', '.jpg', '.png', '.jpeg', '.jfif'] :
#    if extension in images :
        full_origin = from_dir + '/' + file_name
        images_dir = to_dir + '/' + 'image_files'
        full_destination = images_dir + '/' + file_name

        # print("Origen completo: ", full_origin)
        # print("Carpeta de destino", images_dir)
        # print("ruta completa de destino: ", full_destination)

        if os.path.exists(images_dir) : 
            print("Si existe carpeta... moviendo " + file_name + ".......")
            shutil.move(full_origin, full_destination)
        else :
            print("No existe... creando carpeta .......")
            os.makedirs(images_dir)
            print("Moviendo " + file_name + ".......")
            shutil.move(full_origin, full_destination)

"""
    if extension in documents :
        full_origin = from_dir + '/' + file_name
        documents_dir = to_dir + '/' + 'documents_files'
        full_destination = documents_dir + '/' + file_name

        # print("Origen completo: ", full_origin)
        # print("Carpeta de destino", documents_dir)
        # print("ruta completa de destino: ", full_destination)

        if os.path.exists(documents_dir) : 
            print("Si existe carpeta... moviendo " + file_name + ".......")
            shutil.move(full_origin, full_destination)
        else :
            print("No existe... creando carpeta .......")
            os.makedirs(documents_dir)
            print("Moviendo " + file_name + ".......")
            shutil.move(full_origin, full_destination)
"""
