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
        'http://www.informatique.nl/?M=GRP&H=017',
        'http://www.informatique.nl/?M=GRP&H=008',



    )

    rules = (

    Rule(LinkExtractor(restrict_xpaths =('////*[@id="content"]/table/tbody/tr/td/table/tbody/tr[2]/td/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//ul[@id="pages"]/li[1]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//*[@id="detailview"]/li/a', )),callback='parse_item',follow=True),
    
    )



    def parse_item(self, response):

        for sel in response.xpath('//*[@id="product-details"]'):
            item = InformatiqueItem()
            item['categorie'] = sel.xpath('//*[@id="breadcrumb"]/li[3]/a/span/text()').extract()
            item['naam'] =  sel.xpath('//*[@id="hdr"]/h1/text()').extract()
            item['stock'] = sel.xpath('//*[@id="details"]/tbody/tr[7]/td[2]/text()[1]').extract()
            item['prijs'] = sel.xpath('//*[@id="price"]/p[@class="verkoopprijs"]/text()').extract()
            item['link'] = response.url
            item['sku'] = sel.xpath('//span[@itemprop="sku"]/text()').extract()

            yield item


