# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import TestItem
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


class TestSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["www.alternate.nl"]
    start_urls = (
        'http://www.alternate.nl/html/product/listing.html?navId=1362&tk=7&lk=9361',
        'http://www.alternate.nl/html/product/listing.html?navId=690&tk=7&lk=9327',
        'http://www.alternate.nl/html/product/listing.html?navId=980&tk=7&lk=9564',
        'http://www.alternate.nl/html/product/listing.html?navId=11898&bgid=8215&tk=7&lk=9344',
        'http://www.alternate.nl/html/product/listing.html?navId=11622&tk=7&lk=9419',
        'http://www.alternate.nl/html/product/listing.html?navId=17510&tk=7&lk=9492',
        'http://www.alternate.nl/html/product/listing.html?navId=1686&tk=7&lk=9501',
        'http://www.alternate.nl/html/product/listing.html?navId=11604&bgid=8215&tk=7&lk=9533'



        
    )
    
    rules = (
    Rule(LinkExtractor(restrict_xpaths =('//div[@class="listRow"][1]/a[@class="productLink"]',)),callback='parse_item'),
    )

    
    
        
    
    def parse_item(self, response):

        for sel in response.xpath('//div[@id="details"]'):
            item = TestItem()
            item['naam'] =  sel.xpath('//div[@class="productNameContainer"]/h1/span[position() = 2]/text()').extract()
            item['subnaam'] = sel.xpath('//div[@class="productNameContainer"]/h1/span[position() = 3]/text()').extract()
            item['info'] = sel.xpath('//div[@class="productShort"]/ul/li/text()').extract()
            item['stock'] = sel.xpath('//div[@class="availability"]/p/text()').extract()

            if sel.xpath('//div[@id="navTree"]/ul/li[19]/ul/li[@class="treeOpened"]').extract():
                item['categorie'] = ["Voeding"]
            elif "Voedingen" in sel.xpath('//div[@class="breadCrumbs"]/span[position() = 3]/a/span/text()').extract():
                item['categorie'] = ["Voeding"]
            else:
                item['categorie'] = sel.xpath('//div[@class="breadCrumbs"]/span[position() = 2]/a/span/text()').extract()
            item['prijs'] = sel.xpath('//span[@itemprop="price"]/@content').extract()
            item['link'] = response.url
            item['ean'] = find_between(sel.xpath('//script[contains(. , "upcean")]/text()').extract()[0], "'upcean', '","']);")
            yield item
            


            



            
  



            
       

