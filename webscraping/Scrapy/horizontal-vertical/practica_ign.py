# Extraccion de datos en IGN sobre las pestañas analisis noticias y video. horizontal y verticalmente.

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class Analisis(Item):
    titulo = Field()
    calificacion = Field()


class Noticias(Item):
    titulo = Field()
    contenido = Field()


class Video(Item):
    titulo = Field()
    fecha_de_publicacion = Field()


class IGNcrawler(CrawlSpider):
    name = 'ign'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 200
    }

    allowed_domains = ['es.ign.com']
    start_urls = ['https://es.ign.com/se/?model=&q=playstation']

    download_delay = 1

    rules = (
        Rule(
            LinkExtractor(
                allow=r'type='
            ), follow=True),  # HORIZONTALIDAD POR TIPO => No tiene callback ya que aqui no voy a extraer datos
        Rule(LinkExtractor(
            allow=r'&page=\d+'
        ), follow=True),
        # HORIZONTALIDAD DE PAGINACION EN CADA TIPO => No tiene callback ya que aqui no voy a extraer datos
        # Una regla por cada tipo de contenido donde ire verticalmente
        # Cada una tiene su propia funcion parse que extraera los items dependiendo de la estructura del HTML donde esta cada tip

        Rule(
            LinkExtractor(  #VERTICALIDAD DE ANALISIS
                allow=r'/review/'
            ), follow=True, callback='parse_analisis'),
        Rule(
            LinkExtractor(  #VERTICALIDAD DE NOTICIAS
                allow=r'/news/'
            ), follow=True, callback='parse_noticias'),
        Rule(
            LinkExtractor(  #VERTICALIDAD DE VIDEOS
                allow=r'/video/'
            ), follow=True, callback='parse_videos'),

    )

    # ANALISIS
    def parse_analisis(self, response):
        item = ItemLoader(Analisis(), response)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('calificacion', '//span[@class="side-wrapper side-wrapper hexagon-content"]/text()')
        yield item.load_item()

    # NOTICIAS
    def parse_noticias(self, response):
        item = ItemLoader(Noticias(), response)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('contenido', '//div[@id="id_text]//*/text()')
        yield item.load_item()

    # VIDEOS

    def parse_videos(self, response):
        item = ItemLoader(Video(), response)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('fecha_de_publicacion', '//span[@class="publish-date"]/text()')
        yield item.load_item()

# scrapy runspider practica_ign.py -o practica_ign.json -t json

