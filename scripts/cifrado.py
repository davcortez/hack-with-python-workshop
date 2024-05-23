#INtegrantes: Josue Matailo, Mateo Galan, Andres Aucay 

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_message() -> str:
    message = input("Ingrese el mensaje a cifrar: ")
    password = input("Ingrese la clave para cifrar el mensaje: ")

    salt, iv = os.urandom(16), os.urandom(16)
    key = generate_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()

    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()

    return urlsafe_b64encode(salt + iv + encrypted_message).decode()

def decrypt_message(encoded_message: str) -> str:
    for attempt in range(2):
        password = input("Ingrese la clave para descifrar el mensaje: ")

        try:
            encrypted_data = urlsafe_b64decode(encoded_message.encode())
            salt, iv, encrypted_message = encrypted_data[:16], encrypted_data[16:32], encrypted_data[32:]
            key = generate_key(password, salt)

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()

            padded_message = decryptor.update(encrypted_message) + decryptor.finalize()
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            message = unpadder.update(padded_message) + unpadder.finalize()
            
            return message.decode()
        
        except Exception:
            print("Clave incorrecta. Inténtelo de nuevo.")
    
    print("Demasiados intentos fallidos. No se pudo descifrar el mensaje.")
    return None

mensaje_cifrado = encrypt_message()
print(f"Mensaje cifrado: {mensaje_cifrado}")

mensaje_descifrado = decrypt_message(mensaje_cifrado)
if mensaje_descifrado:
    print(f"Mensaje descifrado: {mensaje_descifrado}")
else:
    print("No se pudo descifrar el mensaje.")
