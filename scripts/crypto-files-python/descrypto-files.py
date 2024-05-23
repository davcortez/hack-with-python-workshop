from cryptography.fernet import Fernet
import os

# Extensión para los archivos encriptados.
extension = 'yaperdiste'

# Función para obtener la contraseña utiliada en el cifrado de los archivos, y almacenada en un archivo en la máquina atacada.
def charger_key():
    return open('key.key', 'rb').read()

# Función para descifrar los archivos afectados y elimionación de la extensión agregada durante el cifrado.
def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        if item.endswith(extension):

            item_orig = item.rsplit('.', 1)[0]
            print(item)
            os.rename(item, item_orig)
            item = item_orig

            with open(item, 'rb') as file:
                encrypted_data = file.read()

            decrypted_data = f.decrypt(encrypted_data)

            with open(item, 'wb') as file:
                file.write(decrypted_data)
        else:
            print('Error decrypting "%s"' %str(item))

if __name__ == '__main__':

    try:
        # Directorio que vamos a cifrar.
        path_to_decrypt = 'test_files'

        # Eliminamos el archivo típico con el mensaje solicitando el rescate.
        os.remove(path_to_decrypt + '\\README.txt')

        # Obtener los archvios del directorio para su descifrado y se guarda en una lista.
        items = os.listdir(path_to_decrypt)
        full_path = [path_to_decrypt + '\\' + item for item in items]

        # Obtener la contraseña utiliada para el cifrado.
        key = charger_key()

        # Desciframos los archivos afectados.
        decrypt(full_path, key)

    except Exception as e:
        print(e)