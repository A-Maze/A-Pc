# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import BobItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class BobSpider(CrawlSpider):
    name = "bob"
    allowed_domains = ["www.alternate.nl"]
    start_urls = (
        'http://www.alternate.nl/html/highlights/page.html?hgid=189&tgid=906&tk=7&lk=7',

        
    )
    
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
    Rule(LinkExtractor(restrict_xpaths =('//div[@id="navTree"]/ul/li/ul/li[contains(concat(" ", normalize-space(@class), "  "), " hasSubs ")]/a', )),callback='parse_item',follow=True),
    )
      # Extract links matching 'item.php' and parse them with the spider's method parse_item
 
    
    def parse_item(self, response):
	items = []
	self.log('Hi, this is an item page! %s' % response.url)
        for sel in response.xpath('//div[contains(concat(" ", normalize-space(@class), "  "), " listRow ")]'):
            item = BobItem()
            item['naam'] =  sel.xpath('//span[contains(concat(" ", normalize-space(@class), " "), " name ")]/span/text()').extract()
            item['subnaam'] = sel.xpath('//span[contains(concat(" ", normalize-space(@class), " "), " additional ")]/text()').extract()
            item['info'] = sel.xpath('//span[contains(concat(" ", normalize-space(@class), " "), " info ")]/text()').extract()
            item['stock'] = sel.xpath('//span[contains(concat(" ", normalize-space(@class), " "), " stockStatusContainer ")]/strong/text()').extract()
            item['categorie'] = sel.xpath('//h1[contains(concat(" ", normalize-space(@class), " "), " seoListingHeadline ")]/text()').extract()
            item['prijs'] = sel.xpath('//span[contains(concat(" ", normalize-space(@class), " "), " price right right10 ")]/text()').extract()
            items.append(item)
        return(items)
            
  



            
       

