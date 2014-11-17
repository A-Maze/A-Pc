# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import GPU, Geheugen, Moederbord, Behuizing, Processor, Voeding, Koeling, Barebones
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import logging
class TweakersSpider(CrawlSpider):
    name = "tweakers"
    allowed_domains = ["tweakers.net"]
    start_urls = (
        'http://tweakers.net/categorie/49/videokaarten/producten/',
        'http://tweakers.net/categorie/545/geheugen-intern/producten/',
        'http://tweakers.net/categorie/47/moederborden/producten/',
        'http://tweakers.net/categorie/61/behuizingen/producten/',
        'http://tweakers.net/categorie/46/processors/producten/',
        'http://tweakers.net/categorie/664/voedingen/producten/',
        'http://tweakers.net/categorie/488/processorkoeling/producten/',
        'http://tweakers.net/categorie/326/barebones/producten/',


    )
    
    rules = (

    Rule(LinkExtractor(restrict_xpaths =('//a[@class="next"]', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//td[@class="itemname"]/p/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//li[@id="tab_select_specificaties"]/a', )),callback='parse_item',follow=True),
    )

 
    
    def parse_item(self, response):

        for sel in response.xpath('//*[@id="tab:specificaties"]'):
            category = sel.xpath('//*[@id="tweakbaseBreadcrumbCategory"]/a/text()').extract()
            print category
            if "Videokaarten" in category:
                item = GPU()

                item['Categorie'] = sel.xpath().extract()
                item['Merk'] = sel.xpath().extract()
                item['Product'] = sel.xpath().extract()
                item['Uitvoering'] = sel.xpath().extract()
                item['Afbeelding'] = sel.xpath().extract()
                item['Videochip'] = sel.xpath().extract()
                item['Chipset_generatie'] = sel.xpath().extract()
                item['Videochipfabrikant'] = sel.xpath().extract()
                item['Nominale_snelheid_videochip'] = sel.xpath().extract()
                item['Maximale_turbo_frequentie'] = sel.xpath().extract()
                item['Rekenkernen'] = sel.xpath().extract()
                item['Geheugengrootte'] = sel.xpath().extract()
                item['Geheugen_Type'] = sel.xpath().extract()
                item['Geheugen_Nominale_snelheid_videochip'] = sel.xpath().extract()
                item['Geheugen_Busbreedte'] = sel.xpath().extract()
                item['Card_Interface'] = sel.xpath().extract()
                item['Video_uit'] = sel.xpath().extract()
                item['Hoogste_HDMI_versie'] = sel.xpath().extract()
                item['Hoogste_DisplayPort_versie'] = sel.xpath().extract()
                item['Video_Adapter'] = sel.xpath().extract()
                item['DirectX_versie'] = sel.xpath().extract()
                item['OpenGL_versie'] = sel.xpath().extract()
                item['Shader_model'] = sel.xpath().extract()
                item['Lengte'] = sel.xpath().extract()
                item['Hoogte'] = sel.xpath().extract()
                item['Breedte'] = sel.xpath().extract()
                item['Aantal_slots'] = sel.xpath().extract()
                item['Aantal_pins'] = sel.xpath().extract()
                item['Aantal_6_pins'] = sel.xpath().extract()
                item['Aantal_8_pins'] = sel.xpath().extract()
                item['Stroomverbruik'] = sel.xpath().extract()
                item['Type_koeling'] = sel.xpath().extract()
                item['Link_Interface'] = sel.xpath().extract()
                item['EAN'] = sel.xpath().extract()
                item['SKU'] = sel.xpath().extract()
                print "Videokaart"
            elif "Geheugen intern" in category:
                print "Geheugen"
            elif "Moederborden" in category:
                print "Moederbord"
            elif "Behuizingen" in category:
                print "Behuizing"
            elif "Processors" in category:
                print "Processor"
            elif "Voedingen" in category:
                print "Voeding"
            elif "Processorkoeling" in category:
                print "Processorkoeling"
            elif "Barebones" in category:
                print "Barebone"
