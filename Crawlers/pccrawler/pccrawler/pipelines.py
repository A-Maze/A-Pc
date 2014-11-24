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

				def pleurindedb(collectionName):
					self.collection.insert(dict(item))
					log.msg("Item wrote to MongoDB database %s/%s/%s" %
			    	(settings['MONGODB_DB'], collectionName, item['categorie']),
			    	level=log.DEBUG, spider=spider) 

				

				collectienaam = ""

				#
				#  one love (L)(L)pipelines(L)(L)
				


				langeNaam = item["categorie"][0]
				if ("Processoren" or "CPU" or "Processors") in langeNaam:
					self.collection = db["processoren"]
					for e in self.collection.find({"EAN": item["EAN"] }):
						print e
					collectienaam = "processoren"
				elif ("Moederbord" or "moederborden") in langeNaam:
					self.collection = db["moederborden"]
					for e in self.collection.find({"EAN": item["EAN"] }):
						print e
					collectienaam = "moederborden"
				elif ("Koeling" or "Koelers" or "Processorkoeling") in langeNaam:
					self.collection = db["koeling"]
					for e in self.collection.find({"EAN": item["EAN"] }):
						print e
					collectienaam = "moederborden"
				elif ("Behuizingen" or "Barebones") in langeNaam:
					self.collection = db["behuizingen"]
					for e in self.collection.find({"EAN": item["EAN"] }):
						print e
					collectienaam = "behuizingen"
				elif ("Grafische" or "GPU" or "Videokaarten" or "Videokaart") in langeNaam:
					self.collection = db["grafische"]
					for e in self.collection.find({"EAN": item["EAN"] }):
						print e
					collectienaam = "grafische"
				elif ("Harde" or "Geheugen intern") in langeNaam:
					self.collection = db["harde"]
					for e in self.collection.find({"EAN": item["EAN"] }):
						print e
					collectienaam = "harde"
				elif ("DVD") in langeNaam:
					self.collection = db["dvd"]
					for e in self.collection.find({"EAN": item["EAN"] }):
						print e
					collectienaam = "dvd"
				elif ("Geheugen" or "RAM") in langeNaam:
					self.collection = db["geheugen"]
					for e in self.collection.find({"EAN": item["EAN"] }):
						print e
					collectienaam = "geheugen"
				elif ("Voeding" or "Voedingen") in langeNaam:
					self.collection = db["voeding"]
					for e in self.collection.find({"EAN": item["EAN"] }):
						print e
					collectienaam = "voeding"

				item["categorie"] = collectienaam
				pleurindedb(collectienaam)
			
			
				return item



	