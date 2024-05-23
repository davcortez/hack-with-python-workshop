def verificar_robustez_contraseña(contraseña):

    longitud_suficiente = len(contraseña) >= 8
    

    contiene_mayusculas = any(c.isupper() for c in contraseña)
    

    contiene_minusculas = any(c.islower() for c in contraseña)
    

    contiene_digitos = any(c.isdigit() for c in contraseña)
    

    contiene_caracteres_especiales = any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in contraseña)
    

    puntuacion = longitud_suficiente + contiene_mayusculas + contiene_minusculas + contiene_digitos + contiene_caracteres_especiales
    

    if puntuacion >= 5:
        print("¡La contraseña es robusta!")
    else:
        print("La contraseña no es lo suficientemente robusta.")


    print("Puntuación de la contraseña:", puntuacion)


contraseña = input("Introduce tu contraseña: ")


verificar_robustez_contraseña(contraseña)


