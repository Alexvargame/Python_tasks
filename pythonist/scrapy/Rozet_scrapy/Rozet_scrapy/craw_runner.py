from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import SmartItem

import re
import json


class SmartPhoneSpider(CrawlSpider):
    COUNT_SMART=2
    name='smartphoneItems'
    allowed_domains =['rozetka.com.ua']#,'kinotochka.co']
    start_urls=['https://rozetka.com.ua/mobile-phones/c80003/']
    # base_url='https://rozetka.com.ua/mobile-phones/c80003/page=%s'
    # start_urls=[base_url%1, 'https://rozetka.com.ua/mobile-phones/c80003']
    rules=[Rule(LinkExtractor(allow=r'mobile-phones/c80003/page\=(?:2|3)/'),callback='parse_items',cb_kwargs={'is_article': True}),
          Rule(LinkExtractor(allow=start_urls[0]),callback='parse_items',cb_kwargs={'is_article': True})]
    #print(rules[0].link_extractor.allow_res,rules[0].link_extractor.allow_domains)
    def parse_items(self, response,is_article):
        global smarts_lst
        smarts_lst = []
        if is_article:
            count=0
            url = response.url
            lnks = response.xpath(
                '//div[@class = "layout layout_with_sidebar"]/section[@class = "content content_type_catalog"]'
                '/rz-grid[@class = "ng-star-inserted"]/ul[@class = "catalog-grid ng-star-inserted"]'
                '/li[@class = "catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted"]').xpath('.//a')
            for l in lnks:
                smart=SmartItem()
                if l.xpath('@title').extract_first() != '':
                    yield scrapy.Request(l.xpath('@href').extract_first(), callback = self.parse_os,
                                         meta={
                                            'title_l':l.xpath('@title').extract_first(),
                                            'link_l':l.xpath('@href').extract_first(),

                                         })
                    count+=1
                    if  count >1:
                        return smarts_lst
        return smarts_lst
    def parse_os(self,responce):
        smart=SmartItem()
        if responce.xpath('//p[@class = "product-about__brief ng-star-inserted"]/text()').extract_first():
            smart_os = responce.xpath('//p[@class = "product-about__brief ng-star-inserted"]/text()').extract_first()
            smart_os=[os.strip().split() for os in smart_os.split('/')]
            smart_os = ' '.join([os for os in smart_os if os[0] in ['Android', 'iOS']][0])
        else:
            smart_os = f'Нет данных'
        price = responce.xpath('//div[@class = "product-price__wrap ng-star-inserted"]')\
            .xpath('.//p[contains(@class,"product-price__big")]/text()').extract_first()
        price = ' '.join(price.split("xa"))
        smart = {
            'title': responce.meta['title_l'],
            'link': responce.meta['link_l'],
            'smart_os': smart_os,
            'price': price,

        }
        smarts_lst.append(smart)
        return smart

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(SmartPhoneSpider)
    reactor.stop()

def main():
    crawl()
    reactor.run()

if __name__ == "__main__":
    main()