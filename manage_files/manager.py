from os.path import dirname as path
from os.path import join as path_join
from os.path import abspath

# Obtener el directorio donde se encuentra el script actual
script_dir = path(abspath(__file__))

# Construir la ruta completa al archivo
file_path = path_join(script_dir, "text.txt")

# Abrir el archivo usando la ruta completa
file_write = open(file_path, 'a')


file_write.write("new etx")
file_write.close()
file_reader = open(file_path, 'r')
print(file_reader.read())

file_reader.close()