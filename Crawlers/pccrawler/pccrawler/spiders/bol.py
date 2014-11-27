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

    Rule(LinkExtractor(restrict_xpaths =('//div[@class="cont_station"]/a', )),follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//div[@class="width_88 left_button tst_searchresults_next"]/span/a', )),follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//*[@id="list_view"]/div[1]/div/div[1]/div[1]/a[1]', )),callback='parse_item'),
    )



    def parse_item(self, response):
        item = BolItem()
        item['categorie'] = response.xpath('//*[@id="option_block_4"]/li[last()-1]/a/text()').extract()
        item['naam'] = response.xpath('//*[@id="main_block"]/div[2]/div/h1/text()').extract()
        item['stock'] = response.xpath('//p[@itemprop="availability"]/text()').extract()
        item['prijs'] = response.xpath('//*[@id="main_block"]/div[4]/div[1]/div[1]/div[1]/div/p/span/meta/@content').extract()
        item['link'] = response.url
        item['ean'] = response.xpath('//*[@data-attr-key="EAN"]/td[2]/text()').extract()
        yield item





