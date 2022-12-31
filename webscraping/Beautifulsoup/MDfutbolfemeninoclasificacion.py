#Clasificacion liga futbol femenino en Mundodeportivo

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.mundodeportivo.com/resultados/futbol/regional/categoria/primera_division_femenina'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos
team = soup.find_all('div', class_='team')
equipos = list()
count = 0
for i in team:
    if count < 20:
        equipos.append(i.text)
    else:
        break
    count += 1


points = soup.find_all('div', class_='num_pts')
puntos = list()

count = 0
for i in points:
    if count < 20:
        puntos.append(i.text)
    else:
        break
    count += 1



df = pd.DataFrame({"Equipo":equipos, "Puntos":puntos}, index=list(range(1,21)))

print(df)