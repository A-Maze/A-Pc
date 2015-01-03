# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pccrawler.items import ComputerlandItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class ComputerlandSpider(CrawlSpider):
    name = "computerland"
    allowed_domains = ["www.computerland.nl"]
    start_urls = (
        'http://www.computerland.nl',


    )

    rules = (

    Rule(LinkExtractor(restrict_xpaths =('//ul[@class="dropdown_flyout"][1]/li/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//table[@class="PagerContainerTable"]/tbody/tr/td[last()-1]/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//div[@class="itemlistcombined-productcontainer"]/div/div/div/a', )),callback='parse_item',follow=True),
    )



    def parse_item(self, response):

        for sel in response.xpath('//*[@id="detailTab-specifications"]'):
            item = ComputerlandItem()
            item['categorie'] =  sel.xpath('//*[@id="aspnetForm"]/div[4]/div[1]/div/div[2]/a').extract()
            item['naam'] = sel.xpath('//*[@id="ctl00_ContentPlaceHolder1_itemDetail_productTitleLabel"]/text()').extract()
            item['subnaam'] = sel.xpath('//*[@id="ctl00_ContentPlaceHolder1_itemDetail_shortSummaryLabel"]/text()').extract()
            item['stock'] = sel.xpath('//*[@id="ctl00_ContentPlaceHolder1_itemDetail_wareHouseDeliveryTimeLabel"]/text()').extract()
            item['prijs'] = sel.xpath('//*[@id="ctl00_ContentPlaceHolder1_itemDetail_salespriceIncludingVATPriceLabel_pricePlaceHolder"]/meta[2]/@content').extract()
            item['link'] = response.url
            item['sku'] = sel.xpath('//*[@id="ctl00_ContentPlaceHolder1_itemDetail_itemDetailTabManufacturerProductNumberTextLabel"]/text()').extract() 
            yield item









