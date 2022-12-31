import requests
from lxml import html

encabezados= {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

url ="https://www.wikipedia.org/"

respuesta = requests.get(url,headers=encabezados)

parser = html.fromstring(respuesta.text) #definimos una variable para parsear

#Obtener todos los idiomas pagina con xpath

idiomas = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()") #Entre todo el arbol busca
# todos los divs cuya clase contenga 'central-featured-lang, en todos los strong busca el texto

print(idiomas)