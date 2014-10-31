# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
import json
import codecs

class PccrawlerPipeline(object):

	

	
        
    

	def process_item(self, item, spider):
		valid = True
		
		settings["CATEGORIE"] = "processoren"
		for data in item:
          # here we only check if the data is not null
          # but we could do any crazy validation we want
			if valid:
				langeNaam = item["categorie"][0]
				if "Moederbord" in langeNaam:
					print 'success'
					settings["CATEGORIE"] = "moederborden"
				else:
					settings["CATEGORIE"] = "processoren"
				self.collection.insert(dict(item))
				log.msg("Item wrote to MongoDB database %s/%s" %
		    	(settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
		    	level=log.DEBUG, spider=spider) 
			return item


	def __init__(self):
		connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
		db = connection[settings['MONGODB_DB']]
		self.collection = db[settings["CATEGORIE"]]