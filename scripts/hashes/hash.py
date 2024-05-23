import hashlib


def generarHash(h):
    digest= h.hexdigest()
    return digest

x=0
while x<1:
    print("Elige el numero de algoritmo:")
    print("1. SHA256")
    print("2. SHA512")
    print("3. MD5")
    print("4. Acabar el programa")
    nAlgoritmo= int(input())


    algoritmo = ""
    if nAlgoritmo != 4:

        print("introduce los datos:")
        datos=input()

        if nAlgoritmo ==1:
            algoritmo="sha256"
        elif nAlgoritmo ==2:
            algoritmo="sha512"
        elif nAlgoritmo ==3:
            algoritmo="md5"

        bdatos = bytes(datos, 'utf-8')
        h = hashlib.new(algoritmo, bdatos)
        hash1= generarHash(h)
        print()
        print(hash1)
        print()
        x=0
    else:
        x=1
print("FIN")