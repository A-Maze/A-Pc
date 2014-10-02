# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import InformatiqueItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class InformatiqueSpider(CrawlSpider):
    name = "informatique"
    allowed_domains = ["www.informatique.nl"]
    start_urls = (
        'http://www.informatique.nl/?M=GRP&H=007',
        'http://www.informatique.nl/?M=GRP&H=033',
        'http://www.informatique.nl/?M=GRP&H=057',
        'http://www.informatique.nl/?M=GRP&H=020',
        'http://www.informatique.nl/?M=GRP&H=012',
        'http://www.informatique.nl/?M=GRP&H=110',
        'http://www.informatique.nl/?M=USL&G=559',
        'http://www.informatique.nl/?M=GRP&H=037',
        'http://www.informatique.nl/?M=GRP&H=021',
        'http://www.informatique.nl/?M=GRP&H=074',
        'http://www.informatique.nl/?M=GRP&H=017',
        'http://www.informatique.nl/?M=GRP&H=008',
        'http://www.informatique.nl/?M=GRP&H=082',
        'http://www.informatique.nl/?M=GRP&H=062',
        'http://www.informatique.nl/?M=GRP&H=011',



    )

    rules = (

    Rule(LinkExtractor(restrict_xpaths =('//div[@id="content"]/table/tbody/tr/td/table/tbody/tr/td/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//ul[@id="pages"]/li[1]/a', )),callback='parse_item',follow=True),
    )



    def parse_item(self, response):

        for sel in response.xpath('//ul[@id="detailview"]/li'):
            item = InformatiqueItem()
            item['naam'] =  sel.xpath('div[@id="title"]/a/text()').extract()
            item['subnaam'] = sel.xpath('div[@id="title"]/a/text()').extract()
            item['info'] = sel.xpath('div[@id="description"]/ul/li/text()').extract()
            item['stock'] = sel.xpath('div[@id="stock"]/text()').extract()
            item['categorie'] = sel.xpath('//div[@id="wrapper_content"]/div[@id="hdr"]/h1/text()').extract()
            item['prijs'] = sel.xpath('div[@id="price"]/text()').extract()
            yield item








