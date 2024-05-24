import re

def verificar_contraseña(contraseña):
    puntuación = 0
    criterios = {
        'longitud': len(contraseña) >= 8,
        'mayúsculas': bool(re.search(r'[A-Z]', contraseña)),
        'minúsculas': bool(re.search(r'[a-z]', contraseña)),
        'números': bool(re.search(r'[0-9]', contraseña)),
        'especiales': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña))
    }

    for criterio, cumple in criterios.items():
        if cumple:
            puntuación += 1

    return puntuación, criterios

def main():
    contraseña = input("Ingrese una contraseña: ")
    puntuación, criterios = verificar_contraseña(contraseña)

    if puntuación >=1 and puntuación <=2:
        val="Bajo"
    elif puntuación >=3 and puntuación <=4:
        val="Medio"
    elif puntuación ==5:
        val="Alto"
    elif puntuación ==0:
        val="Bajo"

    print(f"Puntuación de la fortaleza de la contraseña: {puntuación}/5 y su nivel de seguridad es: {val}")
    if puntuación < 5:
        print("La contraseña debe cumplir con los siguientes criterios:")
        if not criterios['longitud']:
            print("- Tener al menos 8 caracteres.")
        if not criterios['mayúsculas']:
            print("- Incluir al menos una letra mayúscula (A-Z).")
        if not criterios['minúsculas']:
            print("- Incluir al menos una letra minúscula (a-z).")
        if not criterios['números']:
            print("- Incluir al menos un dígito (0-9).")
        if not criterios['especiales']:
            print("- Incluir al menos un carácter especial (por ejemplo, !, @, #, $, etc.).")
    else:
        print("¡La contraseña es robusta!")
        

if __name__ == "__main__":
    main()
    
