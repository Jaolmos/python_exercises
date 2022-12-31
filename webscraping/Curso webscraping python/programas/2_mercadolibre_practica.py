from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Articulo(Item):
    titulo = Field()
    precio = Field()
    descripcion = Field()

class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadoLibre'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20
        # Numero maximo de paginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este numero
    }

    allowed_domains = ['listado.mercadolibre.com.ar', 'articulo.mercadolibre.com.ar', 'www.mercadolibre.com.ar']
    start_urls = ['https://listado.mercadolibre.com.ar/animales-mascotas/gatos/']

    download_delay = 1

    rules = (
        Rule(  # REGLA #1 => HORIZONTALIDAD POR PAGINACION
            LinkExtractor(
                allow=r'/_Desde_'
                # Patron en donde se utiliza "\d+", expresion que puede tomar el valor de cualquier combinacion de numeros
            ), follow=True),
        Rule(  # REGLA #2 => VERTICALIDAD AL DETALLE DE LOS PRODUCTOS
            LinkExtractor(
                allow=r'/MLA'
            ), follow=True, callback='parse_items'),
    # Al entrar al detalle de los productos, se llama al callback con la respuesta al requerimiento
    )
    def parse_items(self, response):

        item = ItemLoader(Articulo(), response)

        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('descripcion', '//div[@class="ui-pdp-description"]/p/text()')
        item.add_xpath('precio', '//span[@class="price-tag-fraction"]/text()')

        yield item.load_item()