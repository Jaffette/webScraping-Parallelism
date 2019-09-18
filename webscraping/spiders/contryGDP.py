from scrapy.spiders import CrawlSpider,Rule
from webscraping.items import Contry
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

class ContrySpider(CrawlSpider):
    name = 'gdp'
    allowed_domains = ["cia.gov"]
    main_domain = 'https://www.cia.gov/library/publications/the-world-factbook'
    start_urls = ['https://www.cia.gov/library/publications/the-world-factbook/geos/af.html']

    rules = [
        Rule(LinkExtractor(allow="https://www.cia.gov/library/publications/the-world-factbook/geos/af.html"),callback='parse_item', follow=True)]
    
    def parse_item(self,response):
        filtro = response.xpath('//select/option/@value').extract()
        for site in filtro[2:]:
            newUrl = self.main_domain+site[2:]
            yield Request(newUrl, callback=self.parse_gdp, dont_filter=True)
          
    def parse_gdp(self,response):
        item = Contry()
        gdp= response.xpath("//div[@id='field-gdp-official-exchange-rate']/div/span[@class='subfield-number']/text()").extract_first()
        if gdp is not None:
            gdp= self.convertGDP(gdp)
            name = response.xpath("//*[@id='geos_title']/span[1]/text()").extract_first()
            item['name'] = name
            item['gdp'] = gdp
            yield(item)
    
    def convertGDP(self,gdp):
        if 'million' in gdp:
            gdp = gdp[1:-8]
            gdp = float(gdp)*10**6
            return gdp
        elif 'billion' in gdp:
            gdp = gdp[1:-8]
            gdp = float(gdp)*10**9
            return gdp
        elif 'trillion' in gdp:
            gdp = gdp[1:-9]
            gdp = float(gdp)*10**12 
            return gdp
       


       
