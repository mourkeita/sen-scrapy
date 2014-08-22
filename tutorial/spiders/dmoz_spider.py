from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem


class DmozSpider(BaseSpider):
    name= "dmoz"
    allowed_domains = ['dmoz.org']
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        for sel in hxs.select('//ul/li'):
            item = DmozItem()
            item['title'] = sel.select('a/text()').extract()
            item['link'] = sel.select('a/@href').extract()
            item['desc'] = sel.select('text()').extract()
            yield item

SPIDER = DmozSpider()
