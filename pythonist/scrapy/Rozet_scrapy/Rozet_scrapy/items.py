# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmartItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    smart_os = scrapy.Field()
    price = scrapy.Field()