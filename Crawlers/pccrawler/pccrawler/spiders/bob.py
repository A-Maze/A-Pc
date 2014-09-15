# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import BobItem
from scrapy.selector import HtmlXPathSelector

class BobSpider(scrapy.Spider):
    name = "bob"
    allowed_domains = ["www.alternate.nl"]
    start_urls = (
        'http://www.alternate.nl/html/product/listing.html?filter_5=&filter_4=&filter_3=&filter_2=&filter_1=&size=500&bgid=10846&lk=9487&tk=7&navId=11572#listingResult',
    )

    def parse(self, response):
        for sel in response.xpath('//*[contains(concat(" ", normalize-space(@class), "  "), " listRow ")]'):
            item = BobItem()
            item['naam'] =  sel.xpath('a/span/span/h2/span[contains(concat(" ", normalize-space(@class), " "), " name ")]/span/text()').extract()
            item['subnaam'] = sel.xpath('a/span/span/h2//span[contains(concat(" ", normalize-space(@class), " "), " additional ")]/text()').extract()
            item['info'] = sel.xpath('a/span[contains(concat(" ", normalize-space(@class), " "), " info ")]/text()').extract()
            item['stock'] = sel.xpath('a/span[contains(concat(" ", normalize-space(@class), " "), " stockStatusContainer ")]/strong/text()').extract()
            yield item

