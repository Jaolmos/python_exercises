import requests
import csv
from bs4 import BeautifulSoup

page = requests.get('https://parascrapear.com')
soup = BeautifulSoup(page.text, 'html.parser')
f=csv.writer(open('frases.csv','w'))
f.writerow(['autor','categoria','frase'])

blockquote_items = soup.find_all('blockquote')


for blockquote in blockquote_items:
    autor= blockquote.find(class_='author').text
    categoria=blockquote.find(class_='cat').text
    frase=blockquote.find('q').text

    f.writerow([autor, categoria, frase])

