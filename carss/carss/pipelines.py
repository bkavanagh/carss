# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from models import Car
from peewee import *


class CarssPipeline(object):

    def process_item(self, item, spider):
        print 'PROCESSING ITEM {}'.format(item.get('ref'))
        c = Car(**item)
        try:
            c.save()
        except IntegrityError as ex:
            pass
        return item
