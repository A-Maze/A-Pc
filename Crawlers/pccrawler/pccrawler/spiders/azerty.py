# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import AzertyItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class AzertySpider(CrawlSpider):
    name = "azerty"
    allowed_domains = ["azerty.nl"]
    start_urls = (
        'http://azerty.nl/8/componenten.html',


    )

    rules = (

    Rule(LinkExtractor(restrict_xpaths =('//*[@id="_producten_zoek_"]/div[5]/div/ul/li/ul/li[position()=4 or position()=5 or (position()>=7 and position()<=9) or position()=11 or position()=13 or position()=14 or position()=16 or position()=17 or position()=20]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//li[@class="node open group"]/ul/li/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//li[@class="info"]/a', )),callback='parse_item',follow=True),
    )



    def parse_item(self, response):

        for sel in response.xpath('//div[@id="artikel-informatie"]'):
            item = AzertyItem()
            item['naam'] =  sel.xpath('//h1[@class="artikel"]/text()').extract()
            item['subnaam'] = sel.xpath('//div[contains(h1[1],@class="artikel")]/h2/text()').extract()
            item['stock'] = sel.xpath('//div[@class="leverbaar-tekst"]/text()').extract()
            item['categorie'] = sel.xpath('//*[@id="product-detail-left-menu"]/div[2]/div/ul/li/ul/li[@class="node open group"]/a/text()').extract()
            item['prijs'] = sel.xpath('//span[@class="groot"]/text()').extract()
            item['link'] = response.url
            item['EAN'] = sel.xpath('//ul[contains(li[1], "Ean &apos; s")]/li[2]/text()').extract()
            item['SKU'] = sel.xpath('//ul[contains(li[1], "Sku &apos; s")]/li[2]/text()').extract()
            yield item



