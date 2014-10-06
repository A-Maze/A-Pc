import scrapy

from scrapy.http import Request
from pccrawler.items import AzertyItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class Davey(CrawlSpider):
	name = "Davey"
	allowed_domains = ["www.azerty.nl"]
	start_urls = (
        'http://azerty.nl/8/componenten.html',
    )
    
	rules = (
    Rule(LinkExtractor(restrict_xpaths =('//li[contains(concat(" ", normalize-space(@class), "  "), " menu ")]//a', )),callback='parse_item',follow=True),
    )

	def parse_item(self, response):
		for sel in response.xpath('//*[contains(concat(" ", normalize-space(@class), "  "), " outer ")]'):
			item = AzertyItem()
			item['titel'] = sel.xpath('.//h3/text()').extract()[0]
			item['omschrijving'] = sel.xpath('.//[contains(concat(" ", normalize-space(@class), " "), "kenmerken ")]/li/text()').extract()[0]
			item['prijs'] = sel.xpath('.//span[contains(concat(" ", normalize-space(@class), " "), "prijs_zicht ")]/text()').extract()[0]
			item['image'] = sel.xpath('ul/li/a/img/@src').extract()[0]
			item['categorie'] = sel.xpath('//div[@id="zoek-titel"]/h1/text()').extract()[0]
			yield item