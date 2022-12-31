from scrapy.item import  Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
#from scrapy.crawler import Crawlerprocess

class Noticia(Item):

    titular = Field()
    descripcion = Field()

class EluniversoSpider(Spider)
    name = "Mi segundo spider"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    start_urls = ['https://www.eluniverso.com/deportes']

    def parse(self, response):
        sel = Selector(response)