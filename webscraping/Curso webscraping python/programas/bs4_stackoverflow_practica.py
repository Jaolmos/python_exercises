import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

url= 'https://es.stackoverflow.com/questions'

respuesta = requests.get(url, headers=headers)


f = csv.writer(open('preguntas.csv', 'w'))
f.writerow(['texto_pregunta', 'descripcion_pregunta'])

soup = BeautifulSoup(respuesta.text)
contenedor_de_preguntas = soup.find(id="questions")
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="question-summary")

for pregunta in lista_de_preguntas:
    texto_pregunta = pregunta.find('h3').text
    descripcion_pregunta = pregunta.find(class_='excerpt').text
    descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '')

    f.writerow([texto_pregunta, descripcion_pregunta])