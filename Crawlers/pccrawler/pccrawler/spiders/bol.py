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

    Rule(LinkExtractor(restrict_xpaths =('//div[@class="cont_station"]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//div[@class="width_88 left_button tst_searchresults_next"]/span/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//a[@class="product_name"]', )),callback='parse_item',follow=True),
    )



    def parse_item(self, response):

        for sel in response.xpath('//div[@class="product_description"]'):
            item = BolItem()
            categorie = sel.xpath('//*[@id="main_block"]/div[3]/div[5]/div/div[1]/div[5]/table/tbody/tr[2]/td/span[2]/a/text()').extract()
            naam = sel.xpath('//*[@id="main_block"]/div[2]/div/h1/text()').extract()
            stock = sel.xpath('//p[@itemprop="availability"]/text()').extract()
            prijs = sel.xpath('//span[@class="product-price-bol"]/meta/@content').extract()
            link = response.url
            ean = sel.xpath('//tr[@data-attr-key="EAN"]/td[2]/text()').extract()
            yield item





