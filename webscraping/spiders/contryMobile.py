from scrapy.spiders import CrawlSpider,Rule
from webscraping.items import Contry
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest
from scrapy.http import Request

class ContrySpider(CrawlSpider):
    name = 'mobile'
    main_domain = 'https://www.cia.gov/library/publications/the-world-factbook'
    allowed_domains = ["cia.gov"]
    start_urls = ['https://www.cia.gov/library/publications/the-world-factbook/geos/af.html']

    rules = [Rule(LinkExtractor(allow="https://www.cia.gov/library/publications/the-world-factbook/geos/af.html"),callback='parse_item', follow=True)]
    

    def parse_item(self,response):
        filtro = response.xpath('//select/option/@value').extract()
        for site in filtro[2:]:
            newUrl = self.main_domain+site[2:]
            yield Request(newUrl, callback=self.parse_mobile, dont_filter=True)

    def parse_mobile(self,response):
        item = Contry()
        mobile = response.xpath("//*[@id='field-telephones-mobile-cellular']/div[1]/span[2]/text()").extract_first()
        if mobile is not None:
            name = response.xpath("//*[@id='geos_title']/span[1]/text()").extract_first()
            item['name'] = name
            item['mobile'] = self.convertmobile(mobile)
            yield item
          
    def convertmobile(self,internet):
        if 'million' in internet:
            internet = internet[:-8]
            internet = float(internet)*10**6
            return internet
        else:
            internet = int(internet.replace(',',''))
            return internet