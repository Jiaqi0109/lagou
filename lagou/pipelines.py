# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql


class MysqlPipeline(object):

    def __init__(self):
        self.conn = None
        self.cur = None
        with open('./KEYWORDS/cid.txt', 'r') as f:
            id = f.read()
        self.cid = id.split('-')

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='jiaqi0109',
            db='lagou',
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        if not hasattr(item, 'table_name'):
            return item
        cols, values = zip(*item.items())

        if 'cid' in cols and 'pid' not in cols:
            cid = str(values[cols.index('cid')])
            if cid not in self.cid:
                self.cid.append(cid)
            else:
                return item

        sql = "INSERT INTO `%s` (%s) VALUES (%s)" % (item.table_name, ','.join(cols), ','.join(['%s'] * len(values)))
        self.cur.execute(sql, values)
        self.conn.commit()
        # print(self.cur._last_executed)
        return item

    def close_spider(self, spider):
        with open('./KEYWORDS/cid.txt', 'w') as f:
            f.write('-'.join(id for id in self.cid))
        self.cur.close()
        self.conn.close()