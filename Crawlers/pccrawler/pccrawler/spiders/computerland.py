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

    Rule(LinkExtractor(restrict_xpaths =('//div/div/div/div[contains(concat(" ", normalize-space(@class), "  "), "megamenu_container megamenu_dark_bar megamenu_light")]/ul[contains(concat(" ", normalize-space(@class), "  "), "megamenu")]/li[2]/div/ul/li/a', )),callback='parse_item',follow=True),
    Rule(LinkExtractor(restrict_xpaths =('//a[contains(concat(" ", normalize-space(@class), "  "), " PagerHyperlinkStyle ")]', )),callback='parse_item',follow=True),
    )



    def parse_item(self, response):

        for sel in response.xpath('//div[contains(concat(" ", normalize-space(@class), "  "), " itemlistcombined-productrowcontainer-210 ")]'):
            item = ComputerlandItem()
            item['naam'] =  sel.xpath('div/div/a/span["@id=ctl00_ContentPlaceHolder1_itemListCombined_itemListTiledASPxCallbackPanel_itemListRepeater_ctl16_titleDescriptionLabel"]/text()').extract()
            item['subnaam'] = sel.xpath('div/div/a/span["@id=ctl00_ContentPlaceHolder1_itemListCombined_itemListTiledASPxCallbackPanel_itemListRepeater_ctl16_shortSummaryLabel"]/text()').extract()
            item['info'] = sel.xpath('div/div/a/span["@id=ctl00_ContentPlaceHolder1_itemListCombined_itemListTiledASPxCallbackPanel_itemListRepeater_ctl16_shortSummaryLabel"]/text()').extract()
            item['stock'] = sel.xpath('div/div/div/span["@id=ctl00_ContentPlaceHolder1_itemListCombined_itemListTiledASPxCallbackPanel_itemListRepeater_ctl16_warehouseDeliveryTimeLabel"]/text()').extract()
            item['categorie'] = sel.xpath('//a[contains(concat(" ", normalize-space(@class), " "), " activebreadcrumbhyperlink ")]/@title').extract()
            item['prijs'] = sel.xpath('div[contains(concat(" ", normalize-space(@class), " "), "itemlistcombined-salespriceincludingvatcontainer")]/div/meta[2]/@content').extract()
            yield item









