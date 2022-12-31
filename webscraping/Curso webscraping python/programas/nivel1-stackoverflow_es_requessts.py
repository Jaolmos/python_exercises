import requests
from bs4 import BeautifulSoup

#User agent
headers = {
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"

}

#URL SEMILLA
url = 'https://es.stackoverflow.com/'

#requerimiento al servidor
respuesta = requests.get(url,headers=headers)

# PARSEO DEL ARBOL CON BEAUTIFUL SOUP
soup = BeautifulSoup(respuesta.text)
contenedor_de_preguntas = soup.find(id="questions") # ENCONTRAR UN ELEMENTO POR ID
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="question-summary")
for pregunta in lista_de_preguntas:
    texto_pregunta = pregunta.find('h3').text  # DENTRO DE CADA ELEMENTO ITERADO ENCONTRAR UN TAG
    descripcion_pregunta = pregunta.find(class_='excerpt').text  # ENCONTRAR POR CLASE
    descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '')  # LIMPIEZA DE TEXTO
    print(texto_pregunta)
    print(descripcion_pregunta)
    print()