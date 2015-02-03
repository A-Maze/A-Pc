# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# |                                                                 |
# |                                                                 |
# |                            pipelines                            |
# |                                                                 |
# |                          made with love                         |
# |                                                                 |
# |                                                                 |
# -------------------------------------------------------------------             
import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
import json
import codecs

#azerty mist graphisce kaarten

#bob mist optische(dvd) / processoren

class PccrawlerPipeline(object):

	def __init__(self):
		var = "bezig"
		
        def process_item(self, item, spider):
		valid = True
		for data in item:
			if valid:
				connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
				db = connection[settings['MONGODB_DB']]

			

				def find_between( s, first, last ):
				    try:
				        start = s.index( first ) + len( first )
				        end = s.index( last, start )
				        return s[start:end]
				    except ValueError:
				        return ""

				
				
					
					
				def addToDatabase(collectienaam):
					filterEuroSign()
					item["prijs"][0] = str(item["prijs"][0]).replace(",",("."))				
					item["prijs"][0] = float(item["prijs"][0])
					item["categorie"] = collectienaam


					try:
						for ean in item["ean"]:
							if self.collection.find({'ean': {'$regex' :  ean}}).count() > 0:
								addToList()


					except:
						try:
							for sku in item["sku"]:
								if self.collection.find({'SKU': {'$regex' : sku}}).count() > 0:
									addToList()
									
						except KeyError:
							return

				def addNewItemToDatabase(collectionName):
					filterEuroSign()		
					self.collection.insert(dict(item))
					log.msg("Item wrote to MongoDB database %s/%s/%s" %
			    	(settings['MONGODB_DB'], collectionName, item['categorie']),
			    	level=log.DEBUG, spider=spider) 

				def filterEuroSign():
					try:
						if u'\u20ac' in item["prijs"][0]:
							item["prijs"][0] = item["prijs"][0][2:]
					except:
						return
						

				def addExistingItemInList(foundLocation,herkomstLocatie):
						if (foundLocation == True):
							replaceValues(herkomstLocatie)
						else:
							addValues()

				def replaceValues(herkomstLocatie):
					try:
						self.collection.update({'ean': item["ean"]}, { "$set": { 'link.'+str(herkomstLocatie) : item["link"]}}, upsert=False)
						self.collection.update({'ean': item["ean"]}, { "$set": { 'prijs.'+str(herkomstLocatie): item["prijs"][0]}}, upsert=False)
						self.collection.update({'ean': item["ean"]}, { "$set": { 'stock.'+str(herkomstLocatie) : item["stock"][0]}}, upsert=False)
						try:
							self.collection.update({'ean': item["ean"]}, { "$set": { 'sku.'+str(herkomstLocatie) : item["sku"][0]}}, upsert=False)
						except KeyError:
							return
					except IndexError:
						self.collection.update({'SKU': {'$regex' : item["sku"]}}, { "$set": { 'link.'+str(herkomstLocatie): item["link"][0]}}, upsert=False)
						self.collection.update({'SKU': {'$regex' : item["sku"]}}, { "$set": { 'prijs.'+str(herkomstLocatie) : item["prijs"][0]}}, upsert=False)
						self.collection.update({'SKU': {'$regex' : item["sku"]}}, { "$set": { 'stock.'+str(herkomstLocatie) : item["stock"][0]}}, upsert=False)

				def addValues(): 
					if (spider.name != "paradigit"):
						try:
							print "ean"
							self.collection.update({'ean': item["ean"]}, {"$push": {"naam" : item["naam"][0]}}, upsert=False)
							self.collection.update({'ean': item["ean"]}, {"$push": {"subnaam" : item["subnaam"][0]}}, upsert=False)
							self.collection.update({'ean': item["ean"]}, {"$push": {"link" : item["link"][0]}}, upsert=False)
							self.collection.update({'ean': item["ean"]}, {"$push": {"herkomst" : item["herkomst"][0]}}, upsert=False)
							self.collection.update({'ean': item["ean"]}, {"$push": {"prijs" : item["prijs"][0]}}, upsert=False)
							self.collection.update({'ean': item["ean"]}, {"$push": {"stock" : item["stock"][0]}}, upsert=False)
							try:
								if self.collection.find({'SKU': {'$regex' : item["sku"][0]}}).count() > 0:
									return
								else:
									self.collection.update({'ean': item["ean"]}, {"$push": {"SKU" : item["sku"][0]}}, upsert=True)
							except KeyError:
								return
						except IndexError:
							for values in item["sku"]:
								self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"naam" : item["naam"][0]}}, upsert=False)
								self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"prijs" : item["prijs"][0]}}, upsert=False)
								self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"link" : item["link"][0]}}, upsert=False)
								self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"herkomst" : item["herkomst"][0]}}, upsert=False)
								self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"stock" : item["stock"][0]}}, upsert=False)
								self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"subnaam" : item["subnaam"][0]}}, upsert=False)
							
					else:
						print "sku"
						for values in item["sku"]:
							self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"naam" : item["naam"][0]}}, upsert=False)
							self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"prijs" : item["prijs"][0]}}, upsert=False)
							self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"link" : item["link"][0]}}, upsert=False)
							self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"herkomst" : item["herkomst"][0]}}, upsert=False)
							self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"stock" : item["stock"][0]}}, upsert=False)
							self.collection.update({'SKU': {'$regex' : values}}, {"$push": {"subnaam" : item["subnaam"][0]}}, upsert=False)

				def addToList():	
					filterEuroSign()
					try:
						for ean in item["ean"]:
							fullItem = self.collection.find({'ean': {'$regex' :  ean}})
					except:
						for sku in item["sku"]:
							fullItem = self.collection.find({'SKU': {'$regex' :  sku}})
				
					waardeArray = []
					foundLocation = False
					herkomstLocatie = 0
					#zet elk item in de array
					for waardes in fullItem:
						waardeArray.append(waardes)
					
					subString = str(waardeArray[0])
					herkomstString = find_between(subString, "herkomst': [" , "]")	
					herkomstArray = herkomstString.split()
					for values in herkomstArray:
						if item["herkomst"][0] in values:
							foundLocation = True
							
							break;
						else:
							herkomstLocatie += 1
					addExistingItemInList(foundLocation,herkomstLocatie)
					
				categorieNaam = item["categorie"][0]
				processoren = ["Processors", "CPU", "Processoren"]
				moederborden = ["Moederbord", "moederborden", "Moederborden"]
				koeling = ["Koeling", "Koelers", "Processorkoeling", "Koelers", "CPU Koelers", "Ventilatoren"]
				behuizingen = ["Behuizingen", "Barebones", "Barebone"]
				grafische = ["Grafische kaarten","kaart","Grafische", "GPU", "Videokaarten", "Videokaart", "grafische", "Grafische kaart"]
				harde = ["Harde", "Interne harde schijven", "Interne", "Solid State Drives", "Solid state drives", "Harddisk", "Harddisk Intern", "Harde schijven intern", "SSD's"]
				dvd = ["DVD", "dvd", "DVD / Blu-ray drives", "Optische drives", "DVD / Blu Ray"]
				geheugen = ["Geheugen", "RAM", "Geheugen intern", "Geheugen PC & Server"]
				voeding = ["Voeding", "Voedingen"]

				if categorieNaam in processoren:
					self.collection = db["processoren"]
					collectienaam = "processoren"
					addToDatabase(collectienaam)				
				elif categorieNaam in moederborden:
					self.collection = db["moederborden"]
					collectienaam = "moederborden"
					addToDatabase(collectienaam)
				elif categorieNaam in koeling:
					self.collection = db["koeling"]
					collectienaam = "koeling"
					addToDatabase(collectienaam)
				elif categorieNaam in behuizingen:
					self.collection = db["behuizingen"]
					collectienaam = "behuizingen"
					addToDatabase(collectienaam)
				elif categorieNaam in grafische:
					self.collection = db["grafische"]
					collectienaam = "grafische"
					addToDatabase(collectienaam)
				elif categorieNaam in harde:
					self.collection = db["harde"]
					collectienaam = "harde"
					addToDatabase(collectienaam)
				elif categorieNaam in dvd:
					self.collection = db["dvd"]
					collectienaam = "dvd"
					addToDatabase(collectienaam)
				elif categorieNaam in geheugen:
					self.collection = db["geheugen"]
					collectienaam = "geheugen"
					addToDatabase(collectienaam)
				elif categorieNaam in voeding:
					self.collection = db["voeding"]
					collectienaam = "voeding"
					addToDatabase(collectienaam)
				else:
					return
				
				return item

				
