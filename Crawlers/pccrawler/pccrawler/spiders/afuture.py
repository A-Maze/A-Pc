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
    )



    def parse_item(self, response):

        for sel in response.xpath('//tbody[@id="productlines"]/tr'):
            item = AfutureItem()
            item['naam'] =  sel.xpath('.//a[contains(concat(" ", normalize-space(@class), "  "), " product-overzicht-item-fabrikant ")]/text()').extract()
            item['info'] = sel.xpath('.//a[contains(concat(" ", normalize-space(@class), "  "), " product-overzicht-item-beschrijving ")]/text()').extract()
            item['stock'] = sel.xpath('.//td[4]/text()').extract()
            item['categorie'] = sel.xpath('//div[@id="content"]/h1/text()').extract()
            item['prijs'] = sel.xpath('.//td[3]/text()').extract()
            yield item





