# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import GPU, Geheugen, Moederbord, Behuizing, Processor, Voeding, Koeling, Barebones
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class TweakersSpider(CrawlSpider):
    name = "tweakers"
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
    Rule(LinkExtractor(restrict_xpaths =('//p[@class="ellipsis"]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//li[@id="tab_select_specificaties"]/a', )),callback='parse_item',follow=True),
    )

 
    
    def parse_item(self, response):

        for sel in response.xpath('//table[@class="spec-detail"]'):
            category = sel.xpath('tbody/tr[position()==2]/td/a/text()').extract()
            if category == "Videokaarten":

            elif category == "Geheugen intern":

            elif category == "Moederborden":

            elif category == "Behuizingen":

            elif category == "Processors":

            elif category == "Voedingen":

            elif category == "Processorkoeling":

            elif category == "Barebones":

            
  



            
       

