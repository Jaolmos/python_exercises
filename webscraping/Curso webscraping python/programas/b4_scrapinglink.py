#esta es una practica de nicolas marin dispara tus ingresos
import requests
import csv
from bs4 import BeautifulSoup

headers = {
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

url = 'https://parascrapear.com/'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

blockquote_items = soup.find_all('blockquote')

for blockquote in blockquote_items:
    autor = blockquote.find(class_='author').text
    categoria = blockquote.find(class_='cat').text
    frase = blockquote.find('q').text

  #  print([autor,categoria,frase])

  f.write(open)


