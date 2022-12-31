#extraccion precio kindle paperwhite en amazon.es

import requests
from bs4 import BeautifulSoup

encabezados = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}
url = 'https://www.amazon.es/Staging-Product-Not-Retail-Sale/dp/B0774LNRQJ/ref=sr_1_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=kindle+paperwhite&qid=1622918011&sr=8-2'
page = requests.get(url, headers = encabezados)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

resultado = soup.find('span', id = 'priceblock_ourprice')
precio_texto = resultado.text
precio_texto = precio_texto.replace('€','').replace(',','.')

precio_actual = float(precio_texto)
#print(precio_actual)
print('Analizando los datos...')

precio_deseado = 143.99
print("\nEl precio máximo deseado para este producto es de "+ str(precio_deseado)+"€\n")
global hay_oferta
#Funcion precio deseado
def Oferta_Precio_Deseado(precio_actual, precio_deseado):
    if(precio_actual < precio_deseado):
        print("¡¡¡OFERTA!!! Kindle PaperWhite está por debajo del precio máximo de deseado de "+str(precio_deseado)+"€. Está a "+str(precio_actual)+"€. ¡¡¡Ahorras "+str(precio_deseado-precio_actual)+"€!!!")
        return False

    elif(precio_actual>precio_deseado):
        print("El precio ha subido a "+ str(precio_actual) + "€.")
        return False

    else:
        print("De momento no hay oferta, sigue al precio de "+str(precio_actual)+"€.")
        return False


hay_oferta = Oferta_Precio_Deseado(precio_actual, precio_deseado)

if(hay_oferta):
    print("Nueva Oferta!!! Avisamos al usuario!!!")
    #avisar por telegram
    import aviso_telegram
    aviso_telegram
else:
    print("Actualmente, no hay oferta")






