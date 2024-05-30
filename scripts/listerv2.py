import os
import argparse

parser = argparse.ArgumentParser(description='Lista archivos sensibles')
parser.add_argument('extensions', type=tuple, help='Lista de extensiones')
args = parser.parse_args()

for root, dirs, files in os.walk('.'):
    for file in files:

        if file.endswith(args.extensions):
            print(os.path.join(root, file))
