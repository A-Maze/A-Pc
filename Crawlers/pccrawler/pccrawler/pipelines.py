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
					if u'\u20ac' in item["prijs"][0]:
						item["prijs"][0] = item["prijs"][0][2:]
					log.msg(item["prijs"][0])
					self.collection.insert(dict(item))
					log.msg("Item wrote to MongoDB database %s/%s/%s" %
			    	(settings['MONGODB_DB'], collectionName, item['categorie']),
			    	level=log.DEBUG, spider=spider) 

				def addToList(item):
					self.collection.update({'ean': item["ean"]}, {"$push": {"naam" : item["naam"][0]}}, upsert=False)
					self.collection.update({'ean': item["ean"]}, {"$push": {"subnaam" : item["subnaam"][0]}}, upsert=False)
					self.collection.update({'ean': item["ean"]}, {"$push": {"link" : item["link"][0]}}, upsert=False)
					self.collection.update({'ean': item["ean"]}, {"$push": {"herkomst" : item["herkomst"][0]}}, upsert=False)
					self.collection.update({'ean': item["ean"]}, {"$push": {"prijs" : item["prijs"][0]}}, upsert=False)
					self.collection.update({'ean': item["ean"]}, {"$push": {"stock" : item["stock"][0]}}, upsert=False)

				collectienaam = ""

				#
				#  one love (L)(L)pipelines(L)(L)
				


				langeNaam = item["categorie"][0]
				if ("Processoren" or "CPU" or "Processors") in langeNaam:
					self.collection = db["processoren"]
					if self.collection.find({"ean": item["ean"] }):					
						addToList(item)

					collectienaam = "processoren"
				elif ("Moederbord" or "moederborden") in langeNaam:
					self.collection = db["moederborden"]
					if  self.collection.find({"ean": item["ean"] }):
						addToList(item)
					collectienaam = "moederborden"
				elif ("Koeling" or "Koelers" or "Processorkoeling" or "Koelers") in langeNaam:
					self.collection = db["koeling"]
					if  self.collection.find({"ean": item["ean"] }):
						addToList(item)
					collectienaam = "koeling"
				elif ("Behuizingen" or "Barebones" or "Barebone") in langeNaam:
					self.collection = db["behuizingen"]
					if self.collection.find({"ean": item["ean"] }):
						addToList(item)
					collectienaam = "behuizingen"
				elif ("Grafische" or "GPU" or "Videokaarten" or "Videokaart") in langeNaam:
					self.collection = db["grafische"]
					if self.collection.find({"ean": item["ean"] }):
						addToList(item)
					collectienaam = "grafische"
				elif ("Harde" or "Geheugen intern" or "Interne") in langeNaam:
					self.collection = db["harde"]
					if self.collection.find({"ean": item["ean"] }):
						addToList(item)
					collectienaam = "harde"
				elif ("DVD" or "dvd") in langeNaam:
					self.collection = db["dvd"]
					if self.collection.find({"ean": item["ean"] }):
						addToList(item)
					collectienaam = "dvd"
				elif ("Geheugen" or "RAM") in langeNaam:
					self.collection = db["geheugen"]
					if self.collection.find({"ean": item["ean"] }):
						addToList(item)
					collectienaam = "geheugen"
				elif ("Voeding" or "Voedingen") in langeNaam:
					self.collection = db["voeding"]
					if self.collection.find({"ean": item["ean"] }):
						addToList(item)
					collectienaam = "voeding"
				else:
					return

				item["categorie"] = collectienaam
				pleurindedb(collectienaam)
			
			
				return item



	