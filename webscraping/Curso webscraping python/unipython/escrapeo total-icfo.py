# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:52:26 2021

@author: josea
"""

from bs4 import BeautifulSoup
import csv
import urllib3

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

download_delay = 1

f = csv.writer(open("datos2.csv", "w"))
f.writerow(["Names" , "Position" ])
http = urllib3.PoolManager()
i_list=range(1, 1500, 1)
for i in i_list:
  web = http.request('GET', 'https://www.icfo.eu/people/people_details?people_id=' + str(i))
  soup = BeautifulSoup(web.data, "lxml")
  nameyesp = soup.find_all('h4')
  print(str(i)+'***************')
  if len(nameyesp) >0:
      nameyesp = soup.find_all('h4')
      namef = nameyesp[0].get_text()
      pos=soup.find_all(class_='position')
      posf = pos[0].get_text()
      f.writerow([namef, posf])
  else:
       print('url vacia')