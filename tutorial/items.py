# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GoodItem(scrapy.Item):
    name = scrapy.Field()
    pic_url = scrapy.Field()
    price = scrapy.Field()
    page_url = scrapy.Field()