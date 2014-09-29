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
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="ctl00_mainMenuContentContainer"]/div/ul/li[6]/div/div[1]/ul/li/a', )),callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[contains(concat(' ', normalize-space(@class), ' '), ' itemlistcombined-toppagercontainer ')]/table/tr/td/a[contains(text(),' > ')]", )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
      
        for sel in response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' itemlistcombined-productrowcontainer-210 ')]"):
            item = ParadigitItem()
            item['categorie'] = sel.xpath('//a[contains(concat(" ", normalize-space(@class), " "), " activebreadcrumbhyperlink ")]/text()').extract()[0]
            item['naam'] = sel.xpath('div/div[contains(concat(" ", normalize-space(@class), " "), " itemlistcombined-titlecontainer ")]/a/span/text()').extract()[0]
            item['info'] = sel.xpath('div/div[contains(concat(" ", normalize-space(@class), " "), " itemlistcombined-shortsummarycontainer ")]/a/span/text()').extract()[0]
            item['stock'] = sel.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " itemlistcombined-warehousedeliverytimecontainer ")]/span/text()').extract()[0]
            item['prijs'] = round(float(sel.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " itemlistcombined-salespriceincludingvatcontainer ")]/div/meta[2]/@content').extract()[0]), 2)

            yield item