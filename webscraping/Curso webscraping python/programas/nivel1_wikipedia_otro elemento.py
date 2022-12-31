#sacamos el texto del titulo historia de la gastronomia de "https://es.m.wikipedia.org/wiki/Wikipedia:Portada"
import requests
from lxml import html

encabezados= {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

url = "https://es.m.wikipedia.org/wiki/Wikipedia:Portada"

respuesta = requests.get(url,headers=encabezados)

parser = html.fromstring(respuesta.text)

titulo = parser.get_element_by_id("Historia_de_la_gastronomía") #obtiene elemento por id
print(titulo.text_content())