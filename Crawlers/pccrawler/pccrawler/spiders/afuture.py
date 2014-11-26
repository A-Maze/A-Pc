# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import AfutureItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class AfutureSpider(CrawlSpider):
    name = "Afuture"
    allowed_domains = ["www.afuture.nl/"]
    start_urls = (
        'https://afuture.nl/',



    )

    rules = (

    Rule(LinkExtractor(restrict_xpaths =('//ul[@id="mainnav"]/li[2]/ul[1]/li/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//ul[@id="mainnav"]/li[2]/ul[1]/li/ul/li/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//li[contains(concat(" ", normalize-space(@class), "  "), " last active ")]/a[contains(concat(" ", normalize-space(@class), "  "), " paginate ")]', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//a[contains(concat(" ", normalize-space(@class), "  "), " product-overzicht-item-fabrikant ")]', )),callback='parse_item',follow=True),
    )



    def parse_item(self, response):

        for sel in response.xpath('//div[@id="content"]'):
            item = AfutureItem()
            item['categorie'] = ''
            item['naam'] =  sel.xpath('h1[1]/text()').extract()
            item['stock'] = sel.xpath('//div[@id="product-lever-informatie-content"]/p[1]/span[contains(concat(" ", normalize-space(@class), "  "), " product-leverinformatie-row-inhoud ")]/text()').extract()
            item['prijs'] = sel.xpath('span[@id="product-detail-prijs-incl"]/text()').extract()
            item['prijs'] = item['prijs'][2:]
            item['link'] = response.url

            yield item