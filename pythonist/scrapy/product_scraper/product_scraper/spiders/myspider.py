import scrapy
from product_scraper.items import Product

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


def remove_dollar_sign(value):
    return value.replace('$', '')


class ProductLoader(ItemLoader):
    default_output_processor = TakeFirst()
    price_in = MapCompose(remove_dollar_sign)

class EcomSpider(scrapy.Spider):
    name = 'ecom_spider'
    allowed_domains = ['clever-lichterman-044f16.netlify.com']
    start_urls = ['https://clever-lichterman-044f16.netlify.com/products/taba-cream.1/']

    def parse(self, response):
        l = ItemLoader(item=Product(), response=response)
        l.add_xpath('price', "//div[@class='my-4']/span/text()")
        l.add_xpath('title', '//section[1]//h2/text()')
        l.add_xpath('title', '//title')
        l.add_value('product_url', response.url)
        l.add_xpath('img_url',"//div[@class='product-slider']//img/@src")
        return l.load_item()
        # item = Product()
        # item['product_url'] = response.url
        # item['price'] = response.xpath("//div[@class='my-4']/span/text()").get()
        # item['title'] = response.xpath('//section[1]//h2/text()').get()
        # item['img_url'] = response.xpath("//div[@class='product-slider']//img/@src").get(0)
        # return item

