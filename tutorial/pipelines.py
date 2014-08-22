# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import MySQLdb


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class DmozPipeline(object):
    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


class ArticlePipeline(object):
    def process_item(self, item, spider):
        if item['ref']:
            return item
        else:
            raise DropItem("Missing reference in %s"  % item)

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'root', 'tutorial', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):    
        try:
            self.cursor.execute("""INSERT INTO articles (ref, title)  
                            VALUES (%s, %s)""", 
                            (item['ref'].encode('utf-8'), 
                            item['title'].encode('utf-8')))

            self.conn.commit()


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item
