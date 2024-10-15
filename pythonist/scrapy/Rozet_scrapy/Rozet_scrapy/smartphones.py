from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
class SmartPhoneSpider(CrawlSpider):
    name='smartphone'
    allowed_domains =['rozetka.com.ua']#,'kinotochka.co']
    start_urls=['https://rozetka.com.ua/mobile-phones/c80003/']
    # base_url='https://rozetka.com.ua/mobile-phones/c80003/page=%s'
    # start_urls=[base_url%1, 'https://rozetka.com.ua/mobile-phones/c80003']
    rules=[Rule(LinkExtractor(allow=r'mobile-phones/c80003/page\=\d{1}/'),callback='parse_items',follow=True,cb_kwargs={'is_article': True})]
    def parse_items(self, response,is_article):
        smarts=[]
        url = response.url

        if is_article:
            print('ISART', is_article)
            print('URL is: {}'.format(url))
            lnks = response.xpath(
                '//div[@class = "layout layout_with_sidebar"]/section[@class = "content content_type_catalog"]'
                '/rz-grid[@class = "ng-star-inserted"]/ul[@class = "catalog-grid ng-star-inserted"]'
                '/li[@class = "catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted"]').xpath('.//a')
            for l in lnks:
                s_dict={'name': '','link': ''}
                if l.xpath('@title').extract_first() != '':
                    s_dict['name']=l.xpath('@title').extract_first()
                    s_dict['link']=l.xpath('@href').extract_first()
                    smarts.append(s_dict)

                    print(f"{l.xpath('@title').extract_first()}:{l.xpath('@href').extract_first()}")
            # lnk = response.xpath('//div[@class = "custom1-item"]/a[@class = "custom1-img"]').xpath('@href').extract()
            # print('lnk', lnk)

# class SmartPhoneSpider(CrawlSpider):
#     name='smartphone'
#     allowed_domains =['kinovibe.co']#,'kinotochka.co']
#     start_urls=['https://kinovibe.co/genrefilm/istoricheskiy/']
#     rules=[Rule(LinkExtractor(allow=r'genrefilm\/.*'),callback='parse_items',follow=True,cb_kwargs={'is_article': True})]
#     def parse_items(self, response,is_article):
#         url = response.url
#         print('ISART',is_article)
#         print('URL is: {}'.format(url))
#         if is_article:
#             text= response.xpath('//div[@class = "custom1-item"]/a/div[@class = "custom1-title"]/text()').extract()
#             print('txt', text)
#             lnk = response.xpath('//div[@class = "custom1-item"]/a[@class = "custom1-img"]').xpath('@href').extract()
#             print('lnk', lnk)
#         input()
#         title = response.css('h1::text').extract_first()
#         print('Title is: {}'.format(title))


