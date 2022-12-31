
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos
team = soup.find_all('span', class_='nombre-equipo')
equipos = list()

count = 0
for i in team:
    if count < 20:
        equipos.append(i.text)
    else:
        break
    count +=1

#print(equipos, len(equipos))

#Puntos
points = soup.find_all('td', class_='destacado')
puntos = list()

count = 0
for i in points:
    if count < 20:
        puntos.append(i.text)
    else:
        break
    count +=1

df = pd.DataFrame({"Equipo":equipos, "Puntos":puntos}, index=list(range(1,21)))

print(df)