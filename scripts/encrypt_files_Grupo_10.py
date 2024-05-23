# Names : Wilson Castillo, Pablo Lucero,Juan jara

import os
import base64
import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

def derive_key(password, salt):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path, password):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    with open(file_path, "wb") as file:
        file.write(salt + fernet.encrypt(data))

def decrypt_file(file_path, password):
    with open(file_path, "rb") as file:
        salt = file.read(16)
        encrypted = file.read()
    key = derive_key(password, salt)
    fernet = Fernet(key)
    with open(file_path, "wb") as file:
        file.write(fernet.decrypt(encrypted))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3 or sys.argv[1] not in ["encrypt", "decrypt"]:
        print("Uso: python script.py <encrypt/decrypt> <file_path>")
        sys.exit(1)
    password = getpass.getpass('Contraseña: ')
    if sys.argv[1] == "encrypt":
        encrypt_file(sys.argv[2], password)
    else:
        decrypt_file(sys.argv[2], password)
