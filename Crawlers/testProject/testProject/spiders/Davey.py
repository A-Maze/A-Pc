import scrapy

from scrapy.http import Request
from testProject.items import TestprojectItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class Davey(CrawlSpider):
	name = "Davey"
	allowed_domains = ["http://www.azerty.nl"]
	start_urls = (
        'http://azerty.nl/8-5824/-met-cpu.html',
    )
    
	rules = (

    Rule(LinkExtractor(restrict_xpaths =('/html/body/div[2]/div[5]/div/ul/li/ul/li[4]/ul/li[1]/ul/li[1]/a', )),callback='parse_item',follow=True),
    #Rule(LinkExtractor(restrict_xpaths =('//div[contains(concat(" ", normalize-space(@class), "  "), " articleSizePerSite ")]/a', )),callback='parse_item',follow=True),
    )

	def parse_item(self, response):
		for sel in response.xpath('//*[contains(concat(" ", normalize-space(@class), "  "), " outer ")]'):
			item = TestprojectItem()
			item['titel'] = sel.xpath('ul/li/a/h3/text()').extract()[0]
			item['omschrijving'] = sel.xpath('ul/li/ul[contains(concat(" ", normalize-space(@class), " "), "kenmerken ")]/li/text()').extract()[0]
			item['prijs'] = sel.xpath('ul/li/div/span[contains(concat(" ", normalize-space(@class), " "), "prijs_zicht ")]/text()').extract()[0]
			item['image'] = sel.xpath('ul/li/a/img/@src').extract()[0]
			item['categorie'] = sel.xpath('//div[@id="zoek-titel"]/h1/text()').extract()[0]
			yield item