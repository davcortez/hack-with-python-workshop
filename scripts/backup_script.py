import os

os.mkdir('backup')

for file in os.listdir('.'):
    if file.endswith('.log'):
        os.system(f'cp {file} backup/')
        #os.system(f'copy {file} backup/') WORKS IN WINDOWS

        print(f"Copiado: {file} a backup/")