import scrapy
from product_scraper.items import Product


from scrapy.loader.processors import TakeFirst, MapCompose, Join
from scrapy.spiders import SitemapSpider


class SitemapSpider(SitemapSpider):
    name = "sitemap_spider"
    sitemap_urls = ['https://clever-lichterman-044f16.netlify.com/sitemap.xml']
    sitemap_rules = [
        ('/products/', 'parse_product')
    ]
    def parse_product(self,response):
        item = Product()
        item['product_url'] = response.url
        item['price'] = response.xpath("//div[@class='my-4']/span/text()").get()
        item['title'] = response.xpath('//section[1]//h2/text()').get()
        item['img_url'] = response.xpath("//div[@class='product-slider']//img/@src").get(0)
        return item