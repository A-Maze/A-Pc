# -*- coding: utf-8 -*-
import scrapy

from pccrawler.items import ParadigitItem

class ParadigitSpider(scrapy.Spider):
    name = "paradigit"
    allowed_domains = ["www.paradigit.nl"]
    start_urls = (
        'http://www.paradigit.nl/catalog/zpr_08ond/06_pccase/default.aspx'
    )

    def parse_item(self, response):
        for sel in response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' itemlistcombined-productrowcontainer-210 ')]"):
            item = ParadigitItem()
            item['naam'] = sel.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " itemlistcombined-titlecontainer ")]/a/span/text()').extract()

            yield item