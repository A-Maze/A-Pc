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
					print(ite)
					if u'\u20ac' in item["prijs"][0]:
						item["prijs"][0] = item["prijs"][0][2:]
					print(item["link"][0])
					try:
						self.collection.update({'ean': item["ean"]}, {"$push": {"link" : item["link"][0]}}, upsert=True)
						self.collection.update({'ean': item["ean"]}, {"$push": {"herkomst" : item["herkomst"][0]}}, upsert=True)
						self.collection.update({'ean': item["ean"]}, {"$push": {"prijs" : item["prijs"][0]}}, upsert=True)
						self.collection.update({'ean': item["ean"]}, {"$push": {"stock" : item["stock"][0]}}, upsert=True)
						self.collection.update({'ean': item["ean"]}, {"$push": {"sku" : item["sku"][0]}}, upsert=True)
					except IndexError:
						self.collection.update({'sku': item["sku"]}, {"$push": {"link" : item["link"][0]}}, upsert=True)
						self.collection.update({'sku': item["sku"]}, {"$push": {"herkomst" : item["herkomst"][0]}}, upsert=True)
						self.collection.update({'sku': item["sku"]}, {"$push": {"prijs" : item["prijs"][0]}}, upsert=True)
						self.collection.update({'sku': item["sku"]}, {"$push": {"stock" : item["stock"][0]}}, upsert=True)

				def addToDatabase(collectienaam):
					item["categorie"] = collectienaam


					eanProduct = self.collection.find({'ean':item["ean"]})
					skuProduct = self.collection.find({'sku':item["sku"]})
					totalProduct = eanProduct 
					for doc in totalProduct:
						
						try:
							if item["ean"][0]:
								if (item["ean"][0] in doc["ean"][0]):
									addToList(collectienaam)
									print("oud")
								else:
									pleurindedb(collectienaam)
									print("nieuw")
						except IndexError:
							if item["sku"][0]:
								if (item["sku"][0] in doc["sku"][0]):
									addToList(collectienaam)
									print("oud")
								else:
									pleurindedb(collectienaam)
									print("nieuw")
							
					
						
						

				collectienaam = ""

				#
				#  one love (L)(L)pipelines(L)(L)
				
				

				langeNaam = item["categorie"][0]
				if ("Processoren" or "CPU" or "Processors") in langeNaam:
					self.collection = db["processoren"]
					collectienaam = "processoren"
					addToDatabase(collectienaam)
					
				elif ("Moederbord" or "moederborden") in langeNaam:
					self.collection = db["moederborden"]
					collectienaam = "moederborden"
					addToDatabase(collectienaam)

				elif ("Koeling" or "Koelers" or "Processorkoeling" or "Koelers") in langeNaam:
					self.collection = db["koeling"]
					collectienaam = "koeling"
					addToDatabase(collectienaam)
				elif ("Behuizingen" or "Barebones" or "Barebone") in langeNaam:
					self.collection = db["behuizingen"]
					collectienaam = "behuizingen"
					addToDatabase(collectienaam)
				elif ("Grafische" or "GPU" or "Videokaarten" or "Videokaart") in langeNaam:
					self.collection = db["grafische"]
					collectienaam = "grafische"
					addToDatabase(collectienaam)
				elif ("Harde" or "intern" or "Interne" or "Solid") in langeNaam:
					self.collection = db["harde"]
					collectienaam = "harde"
					addToDatabase(collectienaam)
				elif ("DVD" or "dvd") in langeNaam:
					self.collection = db["dvd"]
					collectienaam = "dvd"
					addToDatabase(collectienaam)
				elif ("Geheugen" or "RAM") in langeNaam:
					self.collection = db["geheugen"]
					collectienaam = "geheugen"
					addToDatabase(collectienaam)
				elif ("Voeding" or "Voedingen") in langeNaam:
					self.collection = db["voeding"]
					collectienaam = "voeding"
					addToDatabase(collectienaam)
				else:
					return

				
			
			
				return item



	