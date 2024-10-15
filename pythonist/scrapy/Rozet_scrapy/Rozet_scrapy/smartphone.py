import scrapy

class ArticleSpider(scrapy.Spider):
    name='article'
    def start_requests(self):
        urls =['https://rozetka.com.ua/mobile-phones/c80003/']
        #     [
        # 'http://en.wikipedia.org/wiki/Python_''%28programming_language%29',
        #     'https://en.wikipedia.org/wiki/Functional_programming',
        #     'https://en.wikipedia.org/wiki/Monty_Python']

        return [scrapy.Request(url=url,callback=self.parse) for url in urls]
    def parse(self, response):
        print('RESPONCE',response)
        url = response.url
        title =response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))
        lnks = response.xpath(
            '//div[@class = "layout layout_with_sidebar"]/section[@class = "content content_type_catalog"]'
            '/rz-grid[@class = "ng-star-inserted"]/ul[@class = "catalog-grid ng-star-inserted"]'
            '/li[@class = "catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted"]').xpath('.//a')
        for  l in lnks:
            if l.xpath('@title').extract_first()!='':
                print(f"{l.xpath('@title').extract_first()}:{l.xpath('@href').extract_first()}")
        lnk = response.xpath('//div[@class = "custom1-item"]/a[@class = "custom1-img"]').xpath('@href').extract()
        print('lnk', lnk)

#
# class ArticleSpider(scrapy.Spider):
#     name='article'
#     def start_requests(self):
#         urls =['https://kinovibe.co/genrefilm/istoricheskiy/']
#         #     [
#         # 'http://en.wikipedia.org/wiki/Python_''%28programming_language%29',
#         #     'https://en.wikipedia.org/wiki/Functional_programming',
#         #     'https://en.wikipedia.org/wiki/Monty_Python']
#
#         return [scrapy.Request(url=url,callback=self.parse) for url in urls]
#     def parse(self, response):
#         url = response.url
#         title =response.css('h1::text').extract_first()
#         print('URL is: {}'.format(url))
#         print('Title is: {}'.format(title))
#         lnks = response.xpath('//div[@class = "custom1-item"]/a/div[@class = "custom1-title"]/text()').extract()
#         print('lnk',lnks)
#         lnk = response.xpath('//div[@class = "custom1-item"]/a[@class = "custom1-img"]').xpath('@href').extract()
#         print('lnk', lnk)

