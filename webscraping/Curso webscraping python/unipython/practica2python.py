from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
i_list=range(1, 1944, 1)
web = http.request('GET', 'https://www.icfo.eu/lang/about-icfo/people/people_details?people_id=296')
soup = BeautifulSoup(web.data, "lxml")
name = soup.find_all('h4')
print(name[0].getText())
mail=soup.find(class_='about')
print(mail.getText())