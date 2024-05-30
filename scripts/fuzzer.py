import requests

def load_dictionary(file_path):
    with open(file_path, 'r') as archivo:
        return [linea.strip() for linea in archivo]

def fuzz(url, parametro, file):
    for line in file:
        try:
            respuesta = requests.get(url, params={parametro: line})
            print(f"Entrada: {line}, Respuesta: {respuesta.status_code}")
        except Exception as e:
            print(f"Error al enviar entrada: {line}, Error: {e}")

ruta_diccionario = 'diccionario.txt'
diccionario = load_dictionary(ruta_diccionario)

url = 'http://testphp.vulnweb.com/search.php'
parametro = 'test' 

fuzz(url, parametro, diccionario)
