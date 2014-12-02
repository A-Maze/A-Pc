# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# |																	|
# |																	|
# |                 	 	   pipelines							|
# |																	|
# |							 made with love							|
# |																	|
# |																	|
# -------------------------------------------------------------------			  
import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
import json
import codecs

class PccrawlerPipeline(object):

<<<<<<< HEAD


    def __init__(self):
        var = "bezig"

    def process_item(self, item, spider):
        valid = True
        for data in item:
            # here we only check if the data is not null
            # but we could do any crazy validation we want
            if valid:
                connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
                db = connection[settings['MONGODB_DB']]

                def pleurindedb(collectionName):
                    #if u'\u20ac' in item["prijs"][0]:
                    #    item["prijs"][0] = item["prijs"][0][2:]
                    #log.msg(item["prijs"][0])
                    self.collection.insert(dict(item))
                    log.msg("Item wrote to MongoDB database %s/%s/%s" %
                            (settings['MONGODB_DB'], collectionName, item['categorie']),
                            level=log.DEBUG, spider=spider)

                def addToList(item):
                    print(item)
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
                    try:
                        if self.collection.find({'ean':  item["ean"][0]}).count() > 0:
                            print("true")
                            #addToList(item)
                        else:
                            print("false")
                            pleurindedb(collectienaam)
                    except:
                        if self.collection.find({'sku':  item["sku"][0]}).count() > 0:
                            print("true")
                            #addToList(item)
                        else:
                            print("false")
                            pleurindedb(collectienaam)

                langeNaam = item["categorie"][0]

                processoren = ["Processors", "CPU", "Processoren"]
                moederborden = ["Moederbord", "moederborden", "Moederborden"]
                koeling = ["Koeling", "Koelers", "Processorkoeling", "Koelers", "CPU Koelers"]
                behuizingen = ["Behuizingen", "Barebones", "Barebone"]
                grafische = ["Grafische", "GPU", "Videokaarten", "Videokaart"]
                harde = ["Harde", "Interne harde schijven", "Interne", "Solid State Drives"]
                dvd = ["DVD", "dvd", "DVD / Blu-ray drives"]
                geheugen = ["Geheugen", "RAM", "Geheugen intern"]
                voeding = ["Voeding", "Voedingen"]

                if langeNaam in processoren:
                    self.collection = db["processoren"]
                    collectienaam = "processoren"
                    addToDatabase(collectienaam)
                elif langeNaam in moederborden:
                    self.collection = db["moederborden"]
                    collectienaam = "moederborden"
                    addToDatabase(collectienaam)
                elif langeNaam in koeling:
                    self.collection = db["koeling"]
                    collectienaam = "koeling"
                    addToDatabase(collectienaam)
                elif langeNaam in behuizingen:
                    self.collection = db["behuizingen"]
                    collectienaam = "behuizingen"
                    addToDatabase(collectienaam)
                elif langeNaam in grafische:
                    self.collection = db["grafische"]
                    collectienaam = "grafische"
                    addToDatabase(collectienaam)
                elif langeNaam in harde:
                    self.collection = db["harde"]
                    collectienaam = "harde"
                    addToDatabase(collectienaam)
                elif langeNaam in dvd:
                    self.collection = db["dvd"]
                    collectienaam = "dvd"
                    addToDatabase(collectienaam)
                elif langeNaam in geheugen:
                    self.collection = db["geheugen"]
                    collectienaam = "geheugen"
                    addToDatabase(collectienaam)
                elif langeNaam in voeding:
                    self.collection = db["voeding"]
                    collectienaam = "voeding"
                    addToDatabase(collectienaam)
                else:
                    return



                return item



	
=======
	def __init__(self):
		var = "bezig"
		
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
					self.collection.insert(dict(item))
					log.msg("Item wrote to MongoDB database %s/%s/%s" %
			    	(settings['MONGODB_DB'], collectionName, item['categorie']),
			    	level=log.DEBUG, spider=spider) 

				def addToList(item):	
					if u'\u20ac' in item["prijs"][0]:
						item["prijs"][0] = item["prijs"][0][2:]

					#if herkomst already exists, we must replace all the values where the herkomst is the same....but how?!
					
					#db["my_collection"].update(
					#	    { "ean": item["ean"]},
					#	    { "$set": { 'prijs.'+str(1/2/3)+'.content' : item["wat je wilt"]}}
					#	)
					


					try:
						#get the index of the herkomst where the herkomst = item["herkomst"][0]
						fullItem = self.collection.find({'ean': item["ean"][0]})
					except:
						fullItem = self.collection.find({'sku': item["sku"][0]})
					waardeArray = []
					waardeArrayTwee = []
					find_herkomst = False
					herkomstLocatie = 0
					#zet elk item in de array
					for waardes in fullItem:
						waardeArray.append(waardes)

					# zet elke waarde in het item in een extra array
					for values in waardeArray:
						if "herkomst" in values:
							find_herkomst = True
						if (find_herkomst == True):
							if item["herkomst"][0] in values:
								break
							elif "]" in values:
								break
							else:
								herkomstLocatie += 1

					try:
						self.collection.update({'ean': item["ean"]}, { "$set": { 'link.'+str(herkomstLocatie-1) : item["link"]}}, upsert=False)
						self.collection.update({'sku': item["sku"]}, { "$set": { 'prijs.'+str(herkomstLocatie-1): item["prijs"][0]}}, upsert=False)
						self.collection.update({'ean': item["ean"]}, { "$set": { 'stock.'+str(herkomstLocatie-1) : item["stock"][0]}}, upsert=False)

						try:
							self.collection.update({'ean': item["ean"]}, { "$set": { 'sku.'+str(herkomstLocatie-1) : item["sku"][0]}}, upsert=False)
						except:
							return
					except:
						self.collection.update({'sku': item["sku"]}, { "$set": { 'link.'+str(herkomstLocatie-1): item["link"][0]}}, upsert=False)
						self.collection.update({'sku': item["sku"]}, { "$set": { 'prijs.'+str(herkomstLocatie-1) : item["prijs"][0]}}, upsert=False)
						self.collection.update({'sku': item["sku"]}, { "$set": { 'stock.'+str(herkomstLocatie-1) : item["stock"][0]}}, upsert=False)


				def addToDatabase(collectienaam):
					item["categorie"] = collectienaam
					try:
						if self.collection.find({'ean':  item["ean"][0]}).count() > 0:
							addToList(item)
						else:
							pleurindedb(collectienaam)
					except:
						if self.collection.find({'sku':  item["sku"][0]}).count() > 0:
							addToList(item)
						else:
							pleurindedb(collectienaam)

<<<<<<< HEAD
				categorieNaam = item["categorie"][0]
				if ("Processoren" or "CPU" or "Processors") in categorieNaam:
					self.collection = db["processoren"]
					collectienaam = "processoren"
					addToDatabase(collectienaam)				
				elif ("Moederbord" or "moederborden") in categorieNaam:
					self.collection = db["moederborden"]
					collectienaam = "moederborden"
					addToDatabase(collectienaam)
				elif ("Koeling" or "Koelers" or "Processorkoeling" or "Koelers") in categorieNaam:
					self.collection = db["koeling"]
					collectienaam = "koeling"
					addToDatabase(collectienaam)
				elif ("Behuizingen" or "Barebones" or "Barebone") in categorieNaam:
					self.collection = db["behuizingen"]
					collectienaam = "behuizingen"
					addToDatabase(collectienaam)
				elif ("Grafische" or "GPU" or "Videokaarten" or "Videokaart") in categorieNaam:
					self.collection = db["grafische"]
					collectienaam = "grafische"
					addToDatabase(collectienaam)
				elif ("Harde" or "intern" or "Interne" or "Solid") in categorieNaam:
					self.collection = db["harde"]
					collectienaam = "harde"
					addToDatabase(collectienaam)
				elif ("DVD" or "dvd") in categorieNaam:
					self.collection = db["dvd"]
					collectienaam = "dvd"
					addToDatabase(collectienaam)
				elif ("Geheugen" or "RAM") in categorieNaam:
					self.collection = db["geheugen"]
					collectienaam = "geheugen"
					addToDatabase(collectienaam)
				elif ("Voeding" or "Voedingen") in categorieNaam:
=======
				langeNaam = item["categorie"][0]

				processoren = ["Processors", "CPU", "Processoren"]
				moederborden = ["Moederbord", "moederborden", "Moederborden"]
				koeling = ["Koeling", "Koelers", "Processorkoeling", "Koelers", "CPU Koelers"]
				behuizingen = ["Behuizingen", "Barebones", "Barebone"]
				grafische = ["Grafische", "GPU", "Videokaarten", "Videokaart"]
				harde = ["Harde", "Interne harde schijven", "Interne", "Solid State Drives"]
				dvd = ["DVD", "dvd", "DVD / Blu-ray drives"]
				geheugen = ["Geheugen", "RAM", "Geheugen intern"]
				voeding = ["Voeding", "Voedingen"]

				if langeNaam in processoren:
					self.collection = db["processoren"]
					collectienaam = "processoren"
					addToDatabase(collectienaam)
				elif langeNaam in moederborden:
					self.collection = db["moederborden"]
					collectienaam = "moederborden"
					addToDatabase(collectienaam)
				elif langeNaam in koeling:
					self.collection = db["koeling"]
					collectienaam = "koeling"
					addToDatabase(collectienaam)
				elif langeNaam in behuizingen:
					self.collection = db["behuizingen"]
					collectienaam = "behuizingen"
					addToDatabase(collectienaam)
				elif langeNaam in grafische:
					self.collection = db["grafische"]
					collectienaam = "grafische"
					addToDatabase(collectienaam)
				elif langeNaam in harde:
					self.collection = db["harde"]
					collectienaam = "harde"
					addToDatabase(collectienaam)
				elif langeNaam in dvd:
					self.collection = db["dvd"]
					collectienaam = "dvd"
					addToDatabase(collectienaam)
				elif langeNaam in geheugen:
					self.collection = db["geheugen"]
					collectienaam = "geheugen"
					addToDatabase(collectienaam)
				elif langeNaam in voeding:
>>>>>>> 70e434357644b7119463dd6907ac7ca55ba9b6c5
					self.collection = db["voeding"]
					collectienaam = "voeding"
					addToDatabase(collectienaam)
				else:
					return
<<<<<<< HEAD
=======


			
>>>>>>> 70e434357644b7119463dd6907ac7ca55ba9b6c5
				return item
>>>>>>> 8299f653fb5ba60ffce8eb45d7c7a6e79dfc0a55
