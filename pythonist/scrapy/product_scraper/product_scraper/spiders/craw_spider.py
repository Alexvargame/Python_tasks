import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from product_scraper.items import Product


class MySpider(CrawlSpider):
    name = 'crawl_spider'
    allowed_domains = ['clever-lichterman-044f16.netlify.com']
    start_urls = ['https://clever-lichterman-044f16.netlify.com/products/']

    rules = (

        Rule(LinkExtractor(allow=('products',)), callback='parse_product'),
    )
    def parse_product(self,response):
        item = Product()
        item['product_url'] = response.url
        item['price'] = response.xpath("//div[@class='my-4']/span/text()").get()
        item['title'] = response.xpath('//section[1]//h2/text()').get()
        item['img_url'] = response.xpath("//div[@class='product-slider']//img/@src").get(0)
        return item