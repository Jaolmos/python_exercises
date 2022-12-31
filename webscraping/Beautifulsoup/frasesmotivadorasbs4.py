#Escrapear una url con frases motivadoras de frases.net

import requests
import csv
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

url = 'https://www.frasess.net/frases-motivadoras-511.html'
respuesta = requests.get(url,headers=headers)
soup = BeautifulSoup(respuesta.text, 'html.parser')

f = csv.writer(open('frasesmotivadoras.csv', 'w'))
f.writerow(['autor', 'frase'])
blockquote_items = soup.find_all('div', class_='quote')
for blockquote in blockquote_items:
    autor = blockquote.find('div', class_="quote_author").text
    frase = blockquote.find('div', class_="quote_text").text


    f.writerow([autor, frase])

