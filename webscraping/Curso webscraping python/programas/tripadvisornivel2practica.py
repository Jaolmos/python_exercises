from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Hotel(Item):
    nombre = Field
    precio = Field
    descripcion = Field
    servicios = Field

class TripadVisor(CrawlSpider):
    name = 'Hoteles'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    starts_url = ['https://www.tripadvisor.es/Hotels-g187517-Cartagena_Municipality_of_Cartagena-Hotels.html']
    download_delay = 2
    rules = (
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-'
            ),follow=True,callback='parse_hotel'

        ),


    )

    def parse_hotel(self, response):
        sel = Selector(response)
        item = ItemLoader(Hotel(),sel)
        item.add_xpath('nombre','//h1[@id="Heading"]/text()')
        item.add_xpath('precio','//div[@class="CEf5oHnZ"]/text()')
        item.add_xpath('descripcion','//div[@class="_2f_ruteS _1bona3Pu _2-hMril5"]/div[1]/text()')
        item.add_xpath('servicios','//div[contains("amenity_text")]/text()')

        yield item.load_item()


#scrapy runspider tripadvisornivel2practica.py -o tripadvisor.csv -t csv
#scrapy runspider tripadvisornivel2practica.py -o tripadvisor.json -t json
