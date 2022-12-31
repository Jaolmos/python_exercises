import requests
from lxml import html

encabezados= {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

url ="https://www.wikipedia.org/"

respuesta = requests.get(url,headers=encabezados)

parser = html.fromstring(respuesta.text) #definimos una variable para parsear
#con request
#ingles = parser.get_element_by_id("js-link-box-en")  #Obtener elemento por id

#print(ingles.text_content()) #saca el contenido en texto scrapeado

#con xpath

ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")  #En todo el arbol busca el tag a cuyo atributo sea id = "js-link-box-en" hasta el hijo directo con tag strong
print(ingles)
