# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item



class LashouPipeline(object):
    def process_item(self, item, spider):
        pass
        return item
        # print  item['name']
        # print 'in pipeline'


class SQLStorePipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='spiders',
                user='root', passwd='build.ns', cursorclass=MySQLdb.cursors.DictCursor,
                charset='utf8', use_unicode=True)

    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):
        # create record if doesn't exist.
        # all this block run on it's own thread
        print item
        tx.execute("select * from lashou_goods where name = %s", (item['name'], ))
        result = tx.fetchone()
        if result:
            print("Item already stored in db: %s" % item)
        else:
            tx.execute(\
                "insert into lashou_goods (name, pic_url,price,page_url) "
                "values (%s, %s,%s,%s)",
                (
                    item['name'],
                    item['pic_url'],
                    item['price'],
                    item['page_url'],
                )
            )
            print("Item stored in db: %s" % item)

    def handle_error(self, e):
        print(e)

