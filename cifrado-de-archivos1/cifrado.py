import PySimpleGUI as sg
from cryptography.fernet import Fernet
import os

def encrypt_file(file, key):
    try:
        with open(file, 'rb') as f:
            content = f.read()
        fernet = Fernet(key)
        encrypted_content = fernet.encrypt(content)
        encrypted_file = file + '.encrypted'
        with open(encrypted_file, 'wb') as f:
            f.write(encrypted_content)
        key_file = file + '.key'
        with open(key_file, 'wb') as kf:
            kf.write(key)
        sg.popup("Éxito", f"El archivo '{file}' ha sido cifrado con éxito.\n"
                            f"El archivo cifrado se guardó como '{encrypted_file}'.\n"
                            f"La clave se ha guardado en '{key_file}'.")
    except Exception as e:
        sg.popup("Error", f"Error al cifrar el archivo: {e}")

def decrypt_file(file, key):
    try:
        fernet = Fernet(key)
        with open(file, 'rb') as f:
            encrypted_content = f.read()
        decrypted_content = fernet.decrypt(encrypted_content)
        decrypted_file = os.path.splitext(file)[0] + '_descifrado.txt'
        with open(decrypted_file, 'wb') as f:
            f.write(decrypted_content)
        sg.popup("Éxito", f"El archivo '{file}' ha sido descifrado con éxito.\n"
                            f"El archivo descifrado se guardó como '{decrypted_file}'.")
    except Exception as e:
        sg.popup("Error", f"Error al descifrar el archivo: {e}")

layout_encrypt = [
    [sg.Text("Selecciona un archivo para cifrar:")],
    [sg.InputText(), sg.FileBrowse()],
    [sg.Button("Cifrar")]
]

layout_decrypt = [
    [sg.Text("Selecciona un archivo cifrado:")],
    [sg.InputText(), sg.FileBrowse()],
    [sg.Text("Selecciona el archivo de clave:")],
    [sg.InputText(), sg.FileBrowse()],
    [sg.Button("Descifrar")]
]

layout = [
    [sg.TabGroup([
        [sg.Tab('Cifrar', layout_encrypt), sg.Tab('Descifrar', layout_decrypt)]
    ])]
]

window = sg.Window("Cifrado y Descifrado de Archivos", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Cifrar":
        file = values[0]
        if file:
            key = Fernet.generate_key()
            encrypt_file(file, key)
        else:
            sg.popup("Error", "No se ha seleccionado ningún archivo para cifrar.")
    elif event == "Descifrar":
        file = values[1]
        key_file = values[2]
        if file and key_file:
            if os.path.exists(key_file):
                with open(key_file, 'rb') as kf:
                    key = kf.read()
                decrypt_file(file, key)
            else:
                sg.popup("Error", f"No se encontró el archivo de clave '{key_file}'. No se puede descifrar el archivo.")
        else:
            sg.popup("Error", "No se ha seleccionado algún archivo o la clave para descifrar.")

window.close()