# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class BobItem(scrapy.Item):
    naam = scrapy.Field()
    subnaam = scrapy.Field()
    info = scrapy.Field()
    stock = scrapy.Field()
    
