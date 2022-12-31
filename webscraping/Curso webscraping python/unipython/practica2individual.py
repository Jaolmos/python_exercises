# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:38:08 2021

@author: josea
"""

from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()
i_list=range(1, 1944, 1)
web = http.request('GET', 'https://www.icfo.eu/people/people_details?people_id=296')
soup = BeautifulSoup(web.data, "lxml")
nameyesp = soup.find_all('h4')
print(nameyesp[0].get_text())
pos=soup.find_all(class_='position')
print(pos[0].get_text())
titulo=soup.find_all(class:='tit')