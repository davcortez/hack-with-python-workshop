with open("estudiantes.txt", "r") as file:
    content = file.readlines()
    print(content[0:2])
