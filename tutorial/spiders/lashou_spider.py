#encoding: utf-8
import scrapy
from scrapy.selector import Selector
from scrapy.http import  Request
from tutorial.items import GoodItem

class DmozSpider(scrapy.Spider):
    name = "lashou"
    allowed_domains = ["lashou.com"]
    start_urls = [
        "http://beijing.lashou.com/cate/meishi",
    ]

    def parse(self, response):
        sel = Selector(response)

        next_page = sel.xpath('//*[@id="main"]/div/div[2]/div[2]/a[@class="pagedown"]/@href').extract_first()

        good_list = sel.xpath('//*[@id="main"]/div/div[2]/div[1]')
        for g in good_list.xpath('div'):
            item = GoodItem()
            pic_url = g.xpath('a/img/@src').extract_first()
            name = g.xpath('h3/a[1]/text()').extract_first()
            price = g.xpath('div/span[1]/text()').extract_first()

            item['name'] = name
            item['pic_url'] = pic_url
            item['price'] = price
            item['page_url'] = response.url

            yield item

        next_page_url = None
        if next_page:
            next_page_url = "http://beijing.lashou.com/cate/meishi/"+next_page.split("/")[-1]


        if next_page_url:
            yield Request(next_page_url, callback=self.parse)
