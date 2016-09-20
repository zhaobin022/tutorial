#encoding: utf-8
import scrapy
from scrapy.selector import Selector

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        base_url = response.url
        x = Selector(response)

        raw_urls  = x.select("//a/@href").extract()
        urls  = []
        for url in raw_urls:
            if 'http' not in url:
                url = base_url + url
            urls.append(url)
        print urls
        print '2222222222222222222222222222222222222222222222222222'
#    def parse(self, response):
#        for sel in response.xpath('//ul/li'):
#            item = DmozItem()
#            item['title'] = sel.xpath('a/text()').extract()
#            item['link'] = sel.xpath('a/@href').extract()
#            item['desc'] = sel.xpath('text()').extract()
#            yield item
