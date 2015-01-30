# -*- coding: utf-8 -*-
import scrapy

from pccrawler.items import ParadigitItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class ParadigitSpider(CrawlSpider):
    name = "paradigit"
    allowed_domains = ["www.paradigit.nl"]
    start_urls = (
        "http://www.paradigit.nl",
    )

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="ctl00_mainMenuContentContainer"]/div/ul/li[5]/div/div[1]/ul/li/a', )),callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//div/div[contains(concat(" ", normalize-space(@class), " "), " itemlistcombined-titlecontainer ")]/a', )),callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[contains(concat(' ', normalize-space(@class), ' '), ' itemlistcombined-toppagercontainer ')]/table/tr/td/a[contains(text(),' > ')]", )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
      
        for sel in response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' itemdetail-productcontainer ')]"):
            item = ParadigitItem()
            
            link = []
            herkomst = []
            link.append(response.url)
            herkomst.append("paradigit")

            item['categorie'] = sel.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " breadcrumb ")]/div[2]/a/text()').extract()
            item['naam'] = sel.xpath('div/div[contains(concat(" ", normalize-space(@class), " "), " itemdetail-producttitlecontainer ")]/h1/span/text()').extract()
            item['info'] = sel.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " itemdetail-shortsummarycontainer ")]/span/text()').extract()
            item['stock'] = sel.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " itemdetail-warehousestockcontainer ")]/span/text()').extract()
            #item['prijs'] = round(float(sel.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " itemdetail-salespriceincludingvatcontainer ")]/div/meta[2]/@content').extract()), 2)
            item['prijs'] = sel.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " itemdetail-salespriceincludingvatcontainer ")]/div/meta[2]/@content').extract()
            item['sku'] = sel.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " itemdetail-specificationstab-mpndescriptioncontainer ")]/span/text()').extract()
            item['link'] = link
            item['herkomst'] = herkomst

            yield item
