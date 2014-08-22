# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    title = Field()
    link = Field()
    desc = Field()


class ArticleItem(Item):
    ref = Field()  
    category = Field()
    url = Field() 
    title = Field()
    source = Field()


class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()
