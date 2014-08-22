# -*- coding: utf-8 -*-
import os
import re
import urlparse
from scrapy import log
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class SenewebSpider(BaseSpider):
    name= "seneweb"
    allowed_domains = ['seneweb.com']
    domain = 'http://www.seneweb.com' 
    start_urls = [
        "http://www.seneweb.com"
    ]

    def parse(self, response):
	hxs = HtmlXPathSelector(response)
	filename = ' '
	i = 0
	for ligne in hxs.select("//div[@class='w_300box_regular']"):
	    # Item's reference
	    ref = ligne.select("./div[@class='thumb-div']/span/a/@href").extract()
	    # Item's category
	    category = ligne.select("./div/span[@class='frontBox315_cap']/text()").extract()
	    # Item's url
	    url = ligne.select("./div/a/@href").extract()
	    # Item's title object
	    title = ligne.select("./div/a/text()").extract()
	    refa = re.sub('.html', '', (ref[0].split("_")[-1]))
	    urla = urlparse.urljoin(self.domain, url[0])
	    # Item's source
	    source = ligne.select("./div/span[@class='front_source_span']/text()").extract()
	    # Item's title 
            article_name = title[0]
	    category_dir_name = category[0]
	    # Directory name of the project
	    root_path = os.path.dirname(__file__)
	    # Category's path
	    category_dir_path_rel = 'Articles/'+category_dir_name
	    # Item's category absolute path
	    category_dir_path_abs = os.path.join(root_path, category_dir_path_rel)
	    if not os.path.exists(category_dir_path_abs):
	        os.mkdir(category_dir_path_abs)
	    # Item's absolute path
	    article_path_abs = os.path.join(category_dir_path_abs, article_name)
	    i += 1
	    log.msg(u"Article scrapé n° %s" % category[0], level=log.INFO)
	    log.msg(u"URL de l'article scrapé est : %s" % urla, level=log.INFO)
            with open(article_path_abs, 'wb') as f:
                f.write(u"La réfrence de l'annonce est %s.\n" % refa)
	 	f.write('\n')
	        f.write("La catgorie de l'article est : %s.\n" % category[0]) 		               
		f.write('\n')
	        f.write("L'url de l'aticle est ici : %s.\n" % urla)                
		f.write('\n')
	        f.write("Titre de l'article : %s.\n" % title[0])
		f.write('\n')
		f.write("La source est : %s \n" % source[0])
		f.write('\n')
		
SPIDER = SenewebSpider()

