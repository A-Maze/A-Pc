import scrapy

from scrapy.http import Request
from testProject.items import TestprojectItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class Davey(scrapy.Spider):
	name = "Davey"
	allowed_domains = ["http://www.azerty.nl"]
	start_urls = (
        'http://www.azerty.nl',
    )
    
	rules = (

    Rule(LinkExtractor(restrict_xpaths =('//div[contains(concat(" ", normalize-space(@class), "  "), " menu ")]/ul/li/ul/[contains(concat(" ", normalize-space(@class), "  "), " leaf ")]/a', )),callback='parse_item',follow=True),
    #Rule(LinkExtractor(restrict_xpaths =('//div[contains(concat(" ", normalize-space(@class), "  "), " articleSizePerSite ")]/a', )),callback='parse_item',follow=True),
    )

	def parse(self, response):
		for sel in response.xpath('//*[contains(concat(" ", normalize-space(@class), "  "), " outer ")]'):
			item = TestprojectItem()
			item['titel'] = sel.xpath('ul/li/a/h3[contains(concat(" ", normalize-space(@class), " "), "")]/text()').extract()[0]
			item['omschrijving'] = sel.xpath('ul/li/ul[contains(concat(" ", normalize-space(@class), " "), "kenmerken ")]/li/text()').extract()[0]
			item['prijs'] = sel.xpath('ul/li/div/span[contains(concat(" ", normalize-space(@class), " "), "prijs_zicht ")]/text()').extract()[0]
			item['image'] = sel.xpath('ul/li/a[contains(concat(" ", normalize-space(@class), " "), " ")]/img/@src').extract()[0]
			item['categorie'] = sel.xpath('//div[@id="zoek-titel"]/h1[contains(concat(" ", normalize-space(@class), " "), "")]/text()').extract()[0]
			yield item