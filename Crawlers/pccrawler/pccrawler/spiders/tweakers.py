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
    Rule(LinkExtractor(restrict_xpaths =('//li[@id="tab_responseect_specificaties"]/a', )),callback='parse_item',follow=True),
    )

 
    
    def parse_item(self, response):

        for sel in response.xpath('//div[@id="tab:specificaties"]'):
            category = response.xpath('//*[@id="tweakbaseBreadcrumbCategory"]/a/text()').extract()
            print category
            if "Videokaarten" in category:
                item = GPU()

                item['categorie'] = sel.xpath('//*[@id="tweakbaseBreadcrumbCategory"]/a/text()').extract()
                item['Merk'] = sel.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract()
                item['Product'] = sel.xpath('//tr[contains(td[1], "Product")]/td[2]/a/text()').extract()
                item['Uitvoering'] = sel.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract()
                item['Afbeelding'] = sel.xpath('//tr[contains(td[1], "Afbeelding")]/td[2]/a/@href').extract()
                item['Videochip'] = sel.xpath('//tr[contains(td[1], "Videochip")]/td[2]/text()').extract()
                item['Chipset_generatie'] = sel.xpath('//tr[contains(td[1], "Chipset generatie")]/td[2]/text()').extract()
                item['Videochipfabrikant'] = sel.xpath('//tr[contains(td[1], "Videochipfabrikant")]/td[2]/text()').extract()
                item['Nominale_snelheid_videochip'] = sel.xpath('//tr[contains(td[1], "Nominale snelheid videochip")]/td[2]/text()').extract()
                item['Maximale_turbo_frequentie'] = sel.xpath('//tr[contains(td[1], "Maximale turbo frequentie")]/td[2]/text()').extract()
                item['Rekenkernen'] = sel.xpath('//tr[contains(td[1], "Rekenkernen")]/td[2]/text()').extract()
                item['Geheugengrootte'] = sel.xpath('//tr[contains(td[1], "Geheugengrootte")]/td[2]/text()').extract()
                item['Geheugen_Type'] = sel.xpath('//tr[contains(td[1], "Geheugen Type (videokaarten)")]/td[2]/text()').extract()
                item['Geheugen_Nominale_snelheid_videochip'] = sel.xpath('//tr[contains(td[1], "Geheugen Snelheid")]/td[2]/text()').extract()
                item['Geheugen_Busbreedte'] = sel.xpath('//tr[contains(td[1], "Geheugen Busbreedte")]/td[2]/text()').extract()
                item['Card_Interface'] = sel.xpath('//tr[contains(td[1], "Card Interface (Video)")]/td[2]/text()').extract()
                item['Video_uit'] = sel.xpath('//tr[contains(td[1], "Video uit")]/td[2]/text()').extract()
                item['Hoogste_HDMI_versie'] = sel.xpath('//tr[contains(td[1], "Hoogste HDMI-versie")]/td[2]/text()').extract()
                item['Hoogste_DisplayPort_versie'] = sel.xpath('//tr[contains(td[1], "Hoogste DisplayPort versie")]/td[2]/text()').extract()
                item['Video_Adapter'] = sel.xpath('//tr[contains(td[1], "Video Adapter")]/td[2]/text()').extract()
                item['DirectX_versie'] = sel.xpath('//tr[contains(td[1], "DirectX versie")]/td[2]/text()').extract()
                item['OpenGL_versie'] = sel.xpath('//tr[contains(td[1], "OpenGL versie")]/td[2]/text()').extract()
                item['Shader_model'] = sel.xpath('//tr[contains(td[1], "Shader model")]/td[2]/text()').extract()
                item['Lengte'] = sel.xpath('//tr[contains(td[1], "Lengte")]/td[2]/text()').extract()
                item['Hoogte'] = sel.xpath('//tr[contains(td[1], "Hoogte")]/td[2]/text()').extract()
                item['Breedte'] = sel.xpath('//tr[contains(td[1], "Breedte")]/td[2]/text()').extract()
                item['Aantal_slots'] = sel.xpath('//tr[contains(td[1], "Aantal slots")]/td[2]/text()').extract()
                item['Aantal_pins'] = sel.xpath('//tr[contains(td[1], "Aantal pins")]/td[2]/text()').extract()
                item['Aantal_6_pins'] = sel.xpath('//tr[contains(td[1], "Aantal 6 pins")]/td[2]/text()').extract()
                item['Aantal_8_pins'] = sel.xpath('//tr[contains(td[1], "Aantal 8 pins")]/td[2]/text()').extract()
                item['Stroomverbruik'] = sel.xpath('//tr[contains(td[1], "Stroomverbruik")]/td[2]/text()').extract()
                item['Type_koeling'] = sel.xpath('//tr[contains(td[1], "Type koeling")]/td[2]/text()').extract()
                item['Link_Interface'] = sel.xpath('//tr[contains(td[1], "Link Interface")]/td[2]/text()').extract()
                item['EAN'] = sel.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract()
                item['SKU'] = sel.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract()
                yield item
                print "Videokaart"

            elif "Geheugen intern" in category:
                #item naam, komt overeen met de naam in items.py
                item = Geheugen()

                #item attributen komt overeen met de inhoud van het item op items.py.
                #sel.xpath moet overeenkomen met de tweakers html structuur.
                #hier moet tr[1], "Modulegrootte" bijvoorbeeld Uitvoering worden aangepast naar hoe het op tweakers staat voor dit item.
                item['categorie'] = sel.xpath('//*[@id="tweakbaseBreadcrumbCategory"]/a/text()').extract()
                item['Merk'] = sel.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract()
                item['Serie'] = sel.xpath('//tr[contains(td[1], "Serie")]/td[2]/a/text()').extract()
                item['Uitvoering'] = sel.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract()
                item['Afbeelding'] = sel.xpath('//tr[contains(td[1], "Afbeelding")]/td[2]/a/@href').extract()
                item['Geheugengrootte'] = sel.xpath('//tr[contains(td[1], "Geheugengrootte")]/td[2]/text()').extract()
                item['Aantal_pins'] = sel.xpath('//tr[contains(td[1], "Aantal")]/td[2]/text()').extract()
                item['Modulegrootte'] = sel.xpath('//tr[contains(td[1], "Modulegrootte")]/td[2]/text()').extract()
                item['Prijs_per_GB'] = sel.xpath('//tr[contains(td[1], "Prijs per GB (geheugen)")]/td[2]/text()').extract()
                item['Geheugentype'] = sel.xpath('//tr[contains(td[1], "Geheugentype")]/td[2]/text()').extract()
                item['Geheugen_Specificatie'] = sel.xpath('//tr[contains(td[1], "Geheugen Specificatie")]/td[2]/text()').extract()
                item['Low_Voltage_DDR'] = sel.xpath('//tr[contains(td[1], "Low Voltage DDR")]/td[2]/text()').extract()
                item['Geheugen_CAS_Latency'] = sel.xpath('//tr[contains(td[1], "Geheugen CAS Latency")]/td[2]/text()').extract()
                item['Spanning'] = sel.xpath('//tr[contains(td[1], "Spanning")]/td[2]/text()').extract()
                item['Fabrieksgarantie'] = sel.xpath('//tr[contains(td[1], "Fabrieksgarantie")]/td[2]/text()').extract()
                item['Bijzonderheden'] = sel.xpath('//tr[contains(td[1], "Bijzonderheden")]/td[2]/text()').extract()
                item['EAN'] = sel.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract()
                item['SKU'] = sel.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract()
                yield item

                print "Geheugen"
            elif "Moederborden" in category:
                item = Moederbord()
                item['categorie'] = sel.xpath('//*[@id="tweakbaseBreadcrumbCategory"]/a/text()').extract()
                item['Merk'] = sel.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract()
                item['Product'] = sel.xpath('//tr[contains(td[1], "Product")]/td[2]/a/text()').extract()
                item['Uitvoering'] = sel.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract()
                item['Afbeelding'] = sel.xpath('//tr[contains(td[1], "Afbeelding")]/td[2]/a/text()').extract()
                item['Socket'] = sel.xpath('//tr[contains(td[1], "Socket")]/td[2]/text()').extract()
                item['Aantal_socket'] = sel.xpath('//tr[contains(td[1], "Aantal_socket")]/td[2]/text()').extract()
                item['Form_Factor'] = sel.xpath('//tr[contains(td[1], "Form Factor")]/td[2]/text()').extract()
                item['BIOS_of_UEFI'] = sel.xpath('//tr[contains(td[1], "BIOS of UEFI")]/td[2]/text()').extract()
                item['Dual_of_Single_BIOS_UEFI'] = sel.xpath('//tr[contains(td[1], "Dual of Single BIOS/UEFI")]/td[2]/text()').extract()
                item['Moederbordchipset'] = sel.xpath('//tr[contains(td[1], "Moederbordchipset")]/td[2]/text()').extract()
                item['Geheugentype'] = sel.xpath('//tr[contains(td[1], "Geheugentype")]/td[2]/text()').extract()
                item['Maximum_geheugengrootte'] = sel.xpath('//tr[contains(td[1], "Maximum geheugengrootte")]/td[2]/text()').extract()
                item['Hardeschijf_bus'] = sel.xpath('//tr[contains(td[1], "Hardeschijf bus")]/td[2]/text()').extract()
                item['Raid_modi'] = sel.xpath('//tr[contains(td[1], "Raid modi")]/td[2]/text()').extract()
                item['Card_Interface'] = sel.xpath('//tr[contains(td[1], "Card Interface (Moederbord)")]/td[2]/text()').extract()
                item['Aantal_PCIe'] = sel.xpath('//tr[contains(td[1], "Aantal PCIe")]/td[2]/text()').extract()
                item['Link_Interface'] = sel.xpath('//tr[contains(td[1], "Link Interface")]/td[2]/text()').extract()
                item['Verbinding_Ethernet'] = sel.xpath('//tr[contains(td[1], "Verbinding Ethernet")]/td[2]/text()').extract()
                item['Netwerkchip'] = sel.xpath('//tr[contains(td[1], "Netwerkchip")]/td[2]/text()').extract()
                item['Bluetooth_aanwezig'] = sel.xpath('//tr[contains(td[1], "Bluetooth aanwezig")]/td[2]/text()').extract()
                item['Verbinding_USB'] = sel.xpath('//tr[contains(td[1], "Verbinding USB")]/td[2]/text()').extract()
                item['Video_uit'] = sel.xpath('//tr[contains(td[1], "Video uit")]/td[2]/text()').extract()
                item['Verbinding'] = sel.xpath('//tr[contains(td[1], "Verbinding")]/td[2]/text()').extract()
                item['Audio_kanalen'] = sel.xpath('//tr[contains(td[1], "Audio kanalen")]/td[2]/text()').extract()
                item['Audio_uitgangen'] = sel.xpath('//tr[contains(td[1], "Audio uitgangen")]/td[2]/text()').extract()
                item['Audiochip'] = sel.xpath('//tr[contains(td[1], "Audiochip")]/td[2]/text()').extract()
                item['EAN'] = sel.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract()
                item['SKU'] = sel.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract()
                yield item 
                print "Moederbord"
            elif "Behuizingen" in category:
                item['categorie'] = sel.xpath('//*[@id="tweakbaseBreadcrumbCategory"]/a/text()').extract()
                item['Merk'] = sel.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract()
                item['Serie'] = sel.xpath('//tr[contains(td[1], "Serie")]/td[2]/a/text()').extract()
                item['Product'] = sel.xpath('//tr[contains(td[1], "Product")]/td[2]/a/text()').extract()
                item['Uitvoering'] = sel.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract()
                item['Behuizingtype'] = sel.xpath('//tr[contains(td[1], "Behuizingtype")]/td[2]/text()').extract()
                item['Form_Factor'] = sel.xpath('//tr[contains(td[1], "Form Factor")]/td[2]/text()').extract()
                item['Behuizing_Panel'] = sel.xpath('//tr[contains(td[1], "Behuizing Panel")]/td[2]/text()').extract()
                item['Materialen_Staal'] = sel.xpath('//tr[contains(td[1], "Materialen Staal")]/td[2]/text()').extract()
                item['Grafische_kaart_maximum_lengte'] = sel.xpath('//tr[contains(td[1], "Grafische kaart maximum lengte")]/td[2]/text()').extract()
                item['CPU_koeler_maximum_hoogte'] = sel.xpath('//tr[contains(td[1], "CPU koeler maximum hoogte")]/td[2]/text()').extract()
                item['Kleuren'] = sel.xpath('//tr[contains(td[1], "Kleuren")]/td[2]/text()').extract()
                item['Behuizing_bay_intern'] = sel.xpath('//tr[contains(td[1], "Behuizing bay intern")]/td[2]/text()').extract()
                item['Behuizing_bay_extern'] = sel.xpath('//tr[contains(td[1], "Behuizing bay extern")]/td[2]/text()').extract()
                item['Aansluitingen_voorzijde'] = sel.xpath('//tr[contains(td[1], "Aansluitingen voorzijde")]/td[2]/text()').extract()
                item['Inclusief_voeding'] = sel.xpath('//tr[contains(td[1], "Inclusief voeding")]/td[2]/text()').extract()
                item['Voeding_plaats'] = sel.xpath('//tr[contains(td[1], "Voeding plaats")]/td[2]/text()').extract()
                item['Voeding_form_factor'] = sel.xpath('//tr[contains(td[1], "Voeding form factor")]/td[2]/text()').extract()
                item['Fan_poorten'] = sel.xpath('//tr[contains(td[1], "Fan poorten")]/td[2]/text()').extract()
                item['Meegeleverde_fans'] = sel.xpath('//tr[contains(td[1], "Meegeleverde fans")]/td[2]/text()').extract()
                item['Kabelmanagement'] = sel.xpath('//tr[contains(td[1], "Kabelmanagement")]/td[2]/text()').extract()
                item['Hoogte'] = sel.xpath('//tr[contains(td[1], "Hoogte")]/td[2]/text()').extract()
                item['Breedte'] = sel.xpath('//tr[contains(td[1], "Breedte")]/td[2]/text()').extract()
                item['Diepte'] = sel.xpath('//tr[contains(td[1], "Diepte")]/td[2]/text()').extract()
                item['Volume'] = sel.xpath('//tr[contains(td[1], "Volume")]/td[2]/text()').extract()
                item['Gewicht'] = sel.xpath('//tr[contains(td[1], "Gewicht")]/td[2]/text()').extract()
                item['Fabrieksgarantie'] = sel.xpath('//tr[contains(td[1], "Fabrieksgarantie")]/td[2]/text()').extract()
                item['Bijzonderheden'] = sel.xpath('//tr[contains(td[1], "Bijzonderheden")]/td[2]/text()').extract()
                item['EAN'] = sel.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract()
                item['SKU'] = sel.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract()
                print "Behuizing"
            elif "Processors" in category:
                print "Processor"
            elif "Voedingen" in category:
                print "Voeding"
            elif "Processorkoeling" in category:
                print "Processorkoeling"
            elif "Barebones" in category:
                print "Barebone"
