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
            category = sel.xpath('table/tbody/tr[2]/td[2]/a/text()').extract()
            logging.warning(category)
            if category == "Videokaarten":
                logging.warning("Videokaart")
            elif category == "Geheugen intern":
                logging.warning("Geheugen")
            elif category == "Moederborden":
                logging.warning("Moederbord")
            elif category == "Behuizingen":
                logging.warning("Behuizing")
            elif category == "Processors":
                logging.warning("Processor")
            elif category == "Voedingen":
                logging.warning("Voeding")
            elif category == "Processorkoeling":
                logging.warning("Processorkoeling")
            elif category == "Barebones":
                logging.warning("Barebone")
