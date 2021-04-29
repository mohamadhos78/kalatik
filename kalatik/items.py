# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class KalatikItem(scrapy.Item):
    title = Field()
    description = Field()
    colors = Field()
    price = Field()
    brand = Field()