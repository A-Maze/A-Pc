# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import BobItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class BobSpider(CrawlSpider):
    name = "computerland"
    allowed_domains = ["www.computerland.nl"]
    start_urls = (
        'http://www.computerland.nl',

        
    )
    
    rules = (

    Rule(LinkExtractor(restrict_xpaths =('//div[contains(concat(" ", normalize-space(@class), "  "), " dropdown_3columns no_padding_top dropdown_container ")][1]ul/li/a', )),callback='parse_item',follow=True),
    )

 
    
    def parse_item(self, response):

        for sel in response.xpath('//div[contains(concat(" ", normalize-space(@class), "  "), " itemlistcombined-productrowcontainer-210 ")]'):
            item = BobItem()
            item['naam'] =  sel.xpath('a/span/span/h2/span[contains(concat(" ", normalize-space(@class), " "), " name ")]/span/text()').extract()
            item['subnaam'] = sel.xpath('a/span/span/h2/span[contains(concat(" ", normalize-space(@class), " "), " additional ")]/text()').extract()
            item['info'] = sel.xpath('a/span[contains(concat(" ", normalize-space(@class), " "), " info ")]/text()').extract()
            item['stock'] = sel.xpath('a/span[contains(concat(" ", normalize-space(@class), " "), " stockStatusContainer ")]/strong/text()').extract()
            item['categorie'] = sel.xpath('//h1[contains(concat(" ", normalize-space(@class), " "), " seoListingHeadline ")]/text()').extract()
            item['prijs'] = sel.xpath('div/p/span[contains(concat(" ", normalize-space(@class), " "), " price right right10 ")]/text()').extract()
            yield item
            
  



            
       

 
