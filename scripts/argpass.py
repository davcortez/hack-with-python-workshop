import argparse

parser = argparse.ArgumentParser(description='Descripción del programa')
parser.add_argument('archivo', type=str, help='Nombre del archivo a procesar')
parser.add_argument('--modo', choices=['lectura', 'escritura'], default='lectura', help='Modo de operación')
args = parser.parse_args()

print(f"Archivo: {args.archivo}")
print(f"Modo: {args.modo}")