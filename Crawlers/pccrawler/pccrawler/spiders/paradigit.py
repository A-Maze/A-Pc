# -*- coding: utf-8 -*-
import scrapy

from pccrawler.items import ParadigitItem
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class ParadigitSpider(CrawlSpider):
    name = "paradigit"
    allowed_domains = ["www.paradigit.nl"]
    start_urls = (
        "http://www.paradigit.nl/catalog/zpr_08ond/06_pccase/default.aspx",
    )

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[contains(concat(' ', normalize-space(@class), ' '), ' itemlistcombined-toppagercontainer ')]/a[contains(text(),' > ')]", )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
      
        for sel in response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' itemlistcombined-productrowcontainer-210 ')]"):
            item = ParadigitItem()
            item['naam'] = sel.xpath('div/div[contains(concat(" ", normalize-space(@class), " "), " itemlistcombined-titlecontainer ")]/a/span//text()').extract()[0]

            yield item