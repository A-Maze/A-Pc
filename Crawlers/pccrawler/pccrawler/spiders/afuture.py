# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import AfutureItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class AfutureSpider(CrawlSpider):
    name = "afuture"
    allowed_domains = ["afuture.nl"]
    start_urls = (
        'https://www.afuture.nl',
    )

    rules = (

    Rule(LinkExtractor(restrict_xpaths =('//ul[@id="mainnav"]/li[2]/ul[1]/li/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//ul[@id="mainnav"]/li[2]/ul[1]/li/ul/li/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//a[contains(concat(" ", normalize-space(@class), "  "), " product-overzicht-item-fabrikant ")]', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//li[contains(concat(" ", normalize-space(@class), "  "), " last active ")]/a[contains(concat(" ", normalize-space(@class), "  "), " paginate ")]', )),callback='parse_item',follow=True),
    )



    def parse_item(self, response):

        for sel in response.xpath('//div[@id="content-tab-specificaties"]'):
            item = AfutureItem()
            #categorie = sel.xpath('//table[@id="product-content-table"]/tbody/tr[1]/th/text()').extract()
            categorie = sel.xpath('//table[@id="product-content-table"]/tr[1]/th/text()').extract()
            print categorie
            if "Processormodel" in categorie:
                item['categorie'] = "Processoren"
            if "Chipset moederbord" in categorie:
                item['categorie'] = "Moederbord"
            if "Kloksnelheid processor" in categorie:
                item['categorie'] = "Grafische"
            if "Opslagcapaciteit harde schijf" in categorie:
                item['categorie'] = "Harde"
            if "Intern" in categorie:
                item['categorie'] = "Harde"
            if "Leessnelheid CD" in categorie:
                item['categorie'] = "DVD"
            else:
                item['categorie'] = "unknown"

            print item['categorie']

            item['naam'] = sel.xpath('//div[@id="content"]/h1[1]/text()').extract()
            item['stock'] = sel.xpath('//div[@id="product-lever-informatie-content"]/p[1]/span[contains(concat(" ", normalize-space(@class), "  "), " product-leverinformatie-row-inhoud ")]/text()').extract()
            item['prijs'] = sel.xpath('//span[@id="product-detail-prijs-incl"]/text()').extract()
            item['link'] = response.url
            item['sku'] = sel.xpath('//table[@id="product-detail-informatie"]/tr[2]/td/text()').extract()
            item['ean'] = sel.xpath('//table[@id="product-detail-informatie"]/tr[3]/td/text()').extract()



            yield item