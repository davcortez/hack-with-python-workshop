#Jonnathan Iñaguazo y Mateo Torres
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
pages = requests.get(url)
soup = BeautifulSoup(pages.content, 'html.parser')

# Equipos
eq = soup.find_all('span', class_='nombre-equipo')
equipment = list()

count = 0
for i in eq:
        if count < 20:
            equipment.append(i.text)
            count += 1
        else:
            break

#print( equipos)

# Puntos
pt = soup.find_all('td', class_='destacado')
points = list()

count = 0
for i in pt:
        if count < 20:
            points.append(i.text)
            count += 1
        else:
            break

#print(puntos)

df = pd.DataFrame({'Nombre':equipment, 'Puntos':points}, index=list(range(1,21)))
print(df)