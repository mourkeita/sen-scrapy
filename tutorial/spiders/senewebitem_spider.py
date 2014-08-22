import os
import re
import urlparse
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial.items import ArticleItem


class SenewebItemSpider(BaseSpider):
    name= "senewebitem"
    allowed_domains = ['seneweb.com']
    domain = 'http://www.seneweb.com' 
    start_urls = [
        "http://www.seneweb.com"
    ]

    def parse(self, response):
	hxs = HtmlXPathSelector(response)
	filename = ' '
	item = ArticleItem()
	for ligne in hxs.select("//div[@class='w_300box_regular']"):
	    ref = ligne.select("./div[@class='thumb-div']/span/a/@href").extract()
	    if ref:  
		item['ref'] = re.sub('.html', '', (ref[0].split("_")[-1]))
		category = ligne.select("./div/span[@class='frontBox315_cap']/text()").extract()
		item['category'] = category[0]
		url = ligne.select("./div/a/@href").extract()
		item['url'] = urlparse.urljoin(self.domain, url[0]) 
		title = ligne.select("./div/a/text()").extract()
		item['title'] = title[0]
		refa = re.sub('.html', '', (ref[0].split("_")[-1]))
		source = ligne.select("./div/span[@class='front_source_span']/text()").extract()
		item['source'] = source[0]
		yield item

SPIDER = SenewebItemSpider()

