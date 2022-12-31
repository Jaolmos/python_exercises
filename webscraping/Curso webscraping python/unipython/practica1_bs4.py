#escrapear links de una pagina.
#separar el texto y el enlace

from bs4 import BeautifulSoup
import csv
import urllib3

f = csv.writer(open("datos.csv", "w"))
f.writerow(['Nombres', 'Enlaces'])

http = urllib3.PoolManager()

web = http.request('GET', 'https://brexitukue.wordpress.com/')
soup = BeautifulSoup(web.data, "lxml")

links=soup.find_all('a')
titulo = soup.title.text

for link in links: 
    link2 = link.get('href')
    textos = link.get_text()
    f.writerow([textos, link2])

