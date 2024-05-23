import sqlite3

def initialize_db():
    try:
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            service TEXT NOT NULL,
            encrypted_password BLOB NOT NULL
        )
        ''')
        conn.commit()
        conn.close()
        print("Base de datos inicializada correctamente.")
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")

def add_password(service, password, cipher_suite):
    try:
        encrypted_password = cipher_suite.encrypt(password.encode())
        
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute('INSERT INTO passwords (service, encrypted_password) VALUES (?, ?)', (service, encrypted_password))
        conn.commit()
        conn.close()
        print(f"Contraseña para {service} añadida correctamente.")
    except Exception as e:
        print(f"Error al añadir contraseña: {e}")

def get_password(service, cipher_suite):
    try:
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute('SELECT encrypted_password FROM passwords WHERE service=?', (service,))
        result = c.fetchone()
        
        if result:
            encrypted_password = result[0]
            decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
            return decrypted_password
        else:
            return None
    except Exception as e:
        print(f"Error al recuperar la contraseña: {e}")
        return None

def list_passwords():
    try:
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute('SELECT id, service, encrypted_password FROM passwords')
        rows = c.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(f"Error al listar las contraseñas: {e}")
        return []
