from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        generate_key()
    return open("key.key", "rb").read()

def initialize_fernet():
    key = load_key()
    return Fernet(key)

def encrypt_password(password):
    f = initialize_fernet()
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password):
    f = initialize_fernet()
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

