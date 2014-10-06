# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TestprojectItem(scrapy.Item):
	titel = scrapy.Field()
	omschrijving = scrapy.Field()
	prijs = scrapy.Field()
	categorie = scrapy.Field()
	image = scrapy.Field()
