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



	