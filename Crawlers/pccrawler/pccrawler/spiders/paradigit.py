# -*- coding: utf-8 -*-
import scrapy

from pccrawler.items import ParadigitItem

class BobSpider(scrapy.Spider):
    name = "paradigit"
    allowed_domains = ["www.paradigit.nl"]
    start_urls = (
        'http://www.paradigit.nl/catalog/zpr_08ond/06_pccase/default.aspx',
    )

    def parse(self, response):
        for sel in response.xpath():
            item = ParadigitItem()
            item['category'] = sel.xpath()
            yield item

