# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import BobItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""


class BobSpider(CrawlSpider):
    name = "bob"
    allowed_domains = ["www.alternate.nl"]
    CONCURRENT_ITEMS = 1000
    CONCURRENT_REQUESTS = 100
    CONCURRENT_REQUESTS_PER_DOMAIN = 1000
    start_urls = (
        'http://www.alternate.nl/html/highlights/page.html?hgid=189&tgid=906&tk=7&lk=7',

        
    )
    
    rules = (

    Rule(LinkExtractor(restrict_xpaths =('//div[@id="navTree"]/ul/li[position()>=4 and position()<20]/ul/li[contains(concat(" ", normalize-space(@class), "  "), " subLevel2 ")]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//div[@id="navTree"]/ul/li[position()>=4 and position()<20]/ul/li[contains(concat(" ", normalize-space(@class), "  "), " subLevel3 ")]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//div[@id="navTree"]/ul/li[position()>=4 and position()<20]/ul/li[contains(concat(" ", normalize-space(@class), "  "), " subLevel4 ")]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//div[contains(concat(" ", normalize-space(@class), "  "), " articleSizePerSite ")]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//a[@class="productLink"]',)),callback='parse_item'),
    )

    
    
        
    
    def parse_item(self, response):

        for sel in response.xpath('//div[@id="details"]'):
            
            item = BobItem()
            item['naam'] =  sel.xpath('//div[@class="productNameContainer"]/h1/span[position() = 2]/text()').extract()
            item['subnaam'] = sel.xpath('//div[@class="productNameContainer"]/h1/span[position() = 3]/text()').extract()
            item['info'] = sel.xpath('//div[@class="productShort"]/ul/li/text()').extract()
            item['stock'] = sel.xpath('//div[@class="availability"]/p/text()').extract()
            item["herkomst"] = ["alternate"]
            if sel.xpath('//div[@id="navTree"]/ul/li[19]/ul/li[@class="treeOpened"]').extract():
                item['categorie'] = ["Voeding"]
            elif "Voedingen" in sel.xpath('//div[@class="breadCrumbs"]/span[position() = 3]/a/span/text()').extract():
                item['categorie'] = ["Voeding"]
            else:
                item['categorie'] = sel.xpath('//div[@class="breadCrumbs"]/span[position() = 2]/a/span/text()').extract()
            item['prijs'] = sel.xpath('//span[@itemprop="price"]/@content').extract()
            item['link'] = response.url
            item['ean'] = [find_between(sel.xpath('//script[contains(. , "upcean")]/text()').extract()[0], "'upcean', '","']);")]

            yield item
            


            



            
  



            
       

