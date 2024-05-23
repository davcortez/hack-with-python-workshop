import sqlite3

def initialize_db():
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                      (id INTEGER PRIMARY KEY, service TEXT, username TEXT, password BLOB)''')
    connection.commit()
    connection.close()

def add_password(service, username, encrypted_password):
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
                   (service, username, encrypted_password))
    connection.commit()
    connection.close()

def get_passwords():
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    cursor.execute("SELECT service, username, password FROM passwords")
    rows = cursor.fetchall()
    connection.close()
    return rows
