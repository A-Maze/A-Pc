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

                item['categorie'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Categorie")]/td[2]/a/text()').extract()
                item['Merk'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Merk")]/td[2]/a/text()').extract()
                item['Product'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Product")]/td[2]/a/text()').extract()
                item['Uitvoering'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract()
                item['Afbeelding'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Afbeelding")]/td[2]/a/text()').extract()
                item['Videochip'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Videochip")]/td[2]/a/text()').extract()
                item['Chipset_generatie'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Chipset generatie")]/td[2]/a/text()').extract()
                item['Videochipfabrikant'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Videochipfabrikant")]/td[2]/a/text()').extract()
                item['Nominale_snelheid_videochip'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Nominale snelheid videochip")]/td[2]/a/text()').extract()
                item['Maximale_turbo_frequentie'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Maximale turbo frequentie")]/td[2]/a/text()').extract()
                item['Rekenkernen'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Rekenkernen")]/td[2]/a/text()').extract()
                item['Geheugengrootte'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Geheugengrootte")]/td[2]/a/text()').extract()
                item['Geheugen_Type'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Geheugen Type (videokaarten)")]/td[2]/a/text()').extract()
                item['Geheugen_Nominale_snelheid_videochip'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Geheugen Snelheid")]/td[2]/a/text()').extract()
                item['Geheugen_Busbreedte'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Geheugen Busbreedte")]/td[2]/a/text()').extract()
                item['Card_Interface'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Card Interface (Video)")]/td[2]/a/text()').extract()
                item['Video_uit'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Video uit")]/td[2]/a/text()').extract()
                item['Hoogste_HDMI_versie'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Hoogste HDMI-versie")]/td[2]/a/text()').extract()
                item['Hoogste_DisplayPort_versie'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Hoogste DisplayPort versie")]/td[2]/a/text()').extract()
                item['Video_Adapter'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Video Adapter")]/td[2]/a/text()').extract()
                item['DirectX_versie'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "DirectX versie")]/td[2]/a/text()').extract()
                item['OpenGL_versie'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "OpenGL versie")]/td[2]/a/text()').extract()
                item['Shader_model'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Shader model")]/td[2]/a/text()').extract()
                item['Lengte'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Lengte")]/td[2]/a/text()').extract()
                item['Hoogte'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Hoogte")]/td[2]/a/text()').extract()
                item['Breedte'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Breedte")]/td[2]/a/text()').extract()
                item['Aantal_slots'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Aantal slots")]/td[2]/a/text()').extract()
                item['Aantal_pins'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Aantal pins")]/td[2]/a/text()').extract()
                item['Aantal_6_pins'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Aantal 6 pins")]/td[2]/a/text()').extract()
                item['Aantal_8_pins'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Aantal 8 pins")]/td[2]/a/text()').extract()
                item['Stroomverbruik'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Stroomverbruik")]/td[2]/a/text()').extract()
                item['Type_koeling'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Type koeling")]/td[2]/a/text()').extract()
                item['Link_Interface'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "Link Interface")]/td[2]/a/text()').extract()
                item['EAN'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "EAN")]/td[2]/a/text()').extract()
                item['SKU'] = sel.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[contains(td[1], "SKU")]/td[2]/a/text()').extract()
                yield item
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
