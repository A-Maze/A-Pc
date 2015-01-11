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
            link = []
            herkomst = []
            link.append(response.url)
            herkomst.append("azerty")
            
            prijs = sel.xpath('//*[@id="_producten_product_detail"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/span[1]/text()').extract()
           
            item['naam'] =  sel.xpath('//h1[@class="artikel"]/text()').extract()
            item['subnaam'] = sel.xpath('//*[@id="_producten_product_detail"]/div[1]/div[1]/div[1]/div/h2').extract()
            item['stock'] = sel.xpath('//*[@id="_producten_product_detail"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/text()').extract()
            item['categorie'] = sel.xpath('//*[@id="product-detail-left-menu"]/div[2]/div/ul/li/ul/li[@class="node open group"]/a/text()').extract()
            item['prijs'] = prijs
            item['link'] = link
            item['ean'] = sel.xpath('//ul[contains(li[1], "'+"Ean's"+'")]/li[2]/text()').extract()
            item['sku'] = sel.xpath('//ul[contains(li[1], "'+"Sku's"+'")]/li[2]/text()').extract()
            item["herkomst"] = herkomst
            yield item


