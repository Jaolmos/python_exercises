from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

# ABSTRACCION DE DATOS A EXTRAER - DETERMINA LOS DATOS QUE TENGO QUE LLENAR Y QUE ESTARAN EN EL ARCHIVO GENERADO
class Pregunta(Item):
    pregunta = Field()
    descripcion = Field()

# CLASE CORE - SPIDER
class StackOverflowSpider(Spider)
    name = "MiPrimerSpider"
    # Forma de configurar el USER AGENT en scrapy
    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

    # URL SEMILLA
    starts_urls = [https://stackoverflow.com/questions/]

