from grupaldb import initialize_db, add_password, get_password, list_passwords
from grupalcryptography import generate_key, load_key
from cryptography.fernet import Fernet

def main():
    initialize_db()
    generate_key()
    
    key = load_key()
    cipher_suite = Fernet(key)
    print("Clave de cifrado cargada.")

    while True:
        print("Gestor de Claves")
        print("1. Añadir contraseña")
        print("2. Recuperar contraseña")
        print("3. Listar todas las contraseñas (Depuración)")
        print("4. Salir")
        
        choice = input("Elija una opción: ")
        
        if choice == '1':
            service = input("Ingrese el nombre del servicio: ")
            password = input("Ingrese la contraseña: ")
            add_password(service, password, cipher_suite)
            print("Contraseña añadida con éxito!")
        
        elif choice == '2':
            service = input("Ingrese el nombre del servicio: ")
            password = get_password(service, cipher_suite)
            if password:
                print(f"La contraseña para {service} es: {password}")
            else:
                print("Servicio no encontrado.")
        
        elif choice == '3':
            passwords = list_passwords()
            for row in passwords:
                print(f"ID: {row[0]}, Servicio: {row[1]}, Contraseña cifrada: {row[2]}")
        
        elif choice == '4':
            break
        
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
