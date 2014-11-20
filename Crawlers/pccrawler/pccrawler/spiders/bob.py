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

    Rule(LinkExtractor(restrict_xpaths =('//div[@id="navTree"]/ul/li[position()>=4 and position()<=19 or position() = 28 or position() = 29 or position = 36]/ul/li[contains(concat(" ", normalize-space(@class), "  "), " subLevel2 ")]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//div[@id="navTree"]/ul/li[position()>=4 and position()<=19 or position() = 28 or position() = 29 or position = 36]/ul/li[contains(concat(" ", normalize-space(@class), "  "), " subLevel3 ")]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//div[@id="navTree"]/ul/li[position()>=4 and position()<=19 or position() = 28 or position() = 29 or position = 36]/ul/li[contains(concat(" ", normalize-space(@class), "  "), " subLevel4 ")]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//div[contains(concat(" ", normalize-space(@class), "  "), " articleSizePerSite ")]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//a[@class="productLink"]',)),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('', )),callback='parse_item',follow=True),
    )

    

        
    
    def parse_item(self, response):
        
        

        for sel in response.xpath('//div[@id="coreProductInfos"]'):
            item = BobItem()
            
            item['naam'] =  sel.xpath('a/span/span/h2/span[contains(concat(" ", normalize-space(@class), " "), " name ")]/span/text()').extract()
            item['subnaam'] = sel.xpath('a/span/span/h2/span[contains(concat(" ", normalize-space(@class), " "), " additional ")]/text()').extract()
            item['info'] = sel.xpath('a/span[contains(concat(" ", normalize-space(@class), " "), " info ")]/text()').extract()
            item['stock'] = sel.xpath('a/span[contains(concat(" ", normalize-space(@class), " "), " stockStatusContainer ")]/strong/text()').extract()
            item['categorie'] = sel.xpath('//h1[contains(concat(" ", normalize-space(@class), " "), " seoListingHeadline ")]/text()').extract()
            item['prijs'] = sel.xpath('div/p/span[contains(concat(" ", normalize-space(@class), " "), " price right right10 ")]/text()').extract()
            item['link'] = "http://www.alternate.nl" + sel.xpath('a[@class="productLink"]/@href').extract()[0]
            item['EAN'] = sel.xpath('//head/script[position() = 1]/@src').extract()[0].split('ean=', 1)
            yield item
            
            
            

            for sel in response.xpath('//div[@id="coreProductInfos"]'):
                item['EAN'] = sel.xpath('//head/script[position() = 1]/@src').extract()[0]
                
           
           

            yield item


            



            
  



            
       

