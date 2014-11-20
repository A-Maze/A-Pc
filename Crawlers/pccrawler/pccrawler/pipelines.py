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

	

	def __init__(self):
		poep = "kaas"
		
        def process_item(self, item, spider):
		valid = True
		for data in item:
          # here we only check if the data is not null
          # but we could do any crazy validation we want
			if valid:
				connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
				db = connection[settings['MONGODB_DB']]

				def pleurindedb():
					self.collection.insert(dict(item))
					log.msg("Item wrote to MongoDB database %s/%s/%s" %
			    	(settings['MONGODB_DB'], settings['MONGODB_COLLECTION'], item['categorie'][0]),
			    	level=log.DEBUG, spider=spider) 

				langeNaam = item["categorie"][0]
				if "Moederbord" or "moederborden" in langeNaam:
					self.collection = db["moederborden"]
					pleurindedb()
				elif "Processoren" or "CPU" or "Processors" in langeNaam:
					self.collection = db["processoren"]
					pleurindedb()
				elif "Koeling" or "Koelers" or "Processorkoeling" in langeNaam:
					self.collection = db["koeling"]
					pleurindedb()
				elif "Behuizingen" or "Barbones" in langeNaam:
					self.collection = db["behuizingen"]
					pleurindedb()
				elif "Grafische" or "GPU" or "Videokaarten" in langeNaam:
					self.collection = db["grafische"]
					pleurindedb()
				elif "Harde" or "Geheugen intern" in langeNaam:
					self.collection = db["harde"]
					pleurindedb()
				elif "DVD" in langeNaam:
					self.collection = db["dvd"]
					pleurindedb()
				elif "Geheugen" or "RAM" in langeNaam:
					self.collection = db["geheugen"]
					pleurindedb()
				elif "Voeding" or "Voedingen" in langeNaam:
					self.collection = db["voeding"]
					pleurindedb()
				
				
		    	
		    	
			return item

	