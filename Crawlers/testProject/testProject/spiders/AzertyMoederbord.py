import scrapy

from scrapy.http import Request
from testProject.items import TestprojectItem
from scrapy.selector import HtmlXPathSelector

class Davey(scrapy.Spider):
	name = "AzertyMoederbord"
	allowed_domains = ["http://www.azerty.nl"]
	start_urls = (
        'http://azerty.nl/8-5991/socket-am1.html',
        'http://azerty.nl/8-2817/socket-am3-.html',
        'http://azerty.nl/8-2938/socket-fm1.html',
        'http://azerty.nl/8-5213/socket-fm2.html',
        'http://azerty.nl/8-5805/socket-fm2-.html',
        'http://azerty.nl/8-5602/socket-1150.html',
        'http://azerty.nl/8-4924/socket-1155.html',
        'http://azerty.nl/8-3200/socket-2011.html',
        'http://azerty.nl/8-6126/socket-2011-3.html',
        'http://azerty.nl/8-846/socket-478.html',
        'http://azerty.nl/8-849/socket-775.html',
        'http://azerty.nl/8-4222/accessoires.html',
        'http://azerty.nl/8-4224/amd-socket-f.html',
        'http://azerty.nl/8-4225/amd-socket-g34.html',
        'http://azerty.nl/8-5988/intel-socket-1150.html',
        'http://azerty.nl/8-4227/intel-socket-1155.html',
        'http://azerty.nl/8-4231/intel-socket-1366.html',
        'http://azerty.nl/8-4939/intel-socket-2011.html',
        'http://azerty.nl/8-843/met-cpu.html',
        'http://azerty.nl/8-839/overige-moederborden.html',
        'http://azerty.nl/producten/zoek?GROEP_ID=1216&p_tab=8&v_uitgebreid=off&PAGINA=1&SORTERING=levertijd_asc&presentatie=miniatuur-lijst',
        'http://azerty.nl/producten/zoek?GROEP_ID=1216&p_tab=8&v_uitgebreid=off&PAGINA=2&SORTERING=levertijd_asc&presentatie=miniatuur-lijst',
        'http://azerty.nl/producten/zoek?GROEP_ID=1216&p_tab=8&v_uitgebreid=off&PAGINA=3&SORTERING=levertijd_asc&presentatie=miniatuur-lijst',
        'http://azerty.nl/producten/zoek?GROEP_ID=1216&p_tab=8&v_uitgebreid=off&PAGINA=4&SORTERING=levertijd_asc&presentatie=miniatuur-lijst',
        'http://azerty.nl/producten/zoek?GROEP_ID=1216&p_tab=8&v_uitgebreid=off&PAGINA=5&SORTERING=levertijd_asc&presentatie=miniatuur-lijst',
        'http://azerty.nl/producten/zoek?GROEP_ID=1216&p_tab=8&v_uitgebreid=off&PAGINA=6&SORTERING=levertijd_asc&presentatie=miniatuur-lijst',
        'http://azerty.nl/producten/zoek?GROEP_ID=1216&p_tab=8&v_uitgebreid=off&PAGINA=7&SORTERING=levertijd_asc&presentatie=miniatuur-lijst',
    )

	def parse(self, response):
		for sel in response.xpath('//*[contains(concat(" ", normalize-space(@class), "  "), " outer ")]'):
			item = TestprojectItem()
			item['titel'] = sel.xpath('ul/li/a/h3[contains(concat(" ", normalize-space(@class), " "), "")]/text()').extract()
			item['omschrijving'] = sel.xpath('ul/li/ul[contains(concat(" ", normalize-space(@class), " "), "kenmerken ")]/li/text()').extract()
			item['prijs'] = sel.xpath('ul/li/div/span[contains(concat(" ", normalize-space(@class), " "), "prijs_zicht ")]/text()').extract()
			item['image'] = sel.xpath('ul/li/a[contains(concat(" ", normalize-space(@class), " "), " ")]/img/@src').extract()
			item['categorie'] = "Moederbord"
			yield item