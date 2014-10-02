# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import BolItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class BolSpider(CrawlSpider):
    name = "bol"
    allowed_domains = ["www.bol.com"]
    start_urls = (
        'http://www.bol.com/nl/m/computer/computercomponenten/N/16430/index.html',



    )

    rules = (

    Rule(LinkExtractor(restrict_xpaths =('//div[contains(concat(" ", normalize-space(@class), "  "), " cont_station ")]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//span[contains(concat(" ", normalize-space(@class), "  "), " po_enda_fftftf.enav.next ")]/a', )),callback='parse_item',follow=True),
    )



    def parse_item(self, response):

        for sel in response.xpath('//div[contains(concat(" ", normalize-space(@class), "  "), " productlist_block ")]'):
            item = BolItem()
            item['naam'] =  sel.xpath('.//a[contains(concat(" ", normalize-space(@class), "  "), " product_name ")]/text()').extract()
            item['info'] = sel.xpath('.//p[contains(concat(" ", normalize-space(@class), "  "), " product_description ")]/text()').extract()
            item['stock'] = sel.xpath('.//p[contains(concat(" ", normalize-space(@class), "  "), " product_delivery ")]/text()').extract()
            item['categorie'] = sel.xpath('//span[contains(concat(" ", normalize-space(@class), "  "), " bol_header ")]/text()').extract()
            item['prijs'] = sel.xpath('.//div[contains(concat(" ", normalize-space(@class), "  "), " price_block ")]/strong/text()').extract()
            yield item








