import os

file_extensions = ('.db', '.sql', '.key', '.pem')

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(file_extensions):
            print(os.path.join(root, file))
