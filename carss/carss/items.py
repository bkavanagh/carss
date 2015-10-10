# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarssItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    mileage = scrapy.Field()
    year = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    engine = scrapy.Field()
    fuel = scrapy.Field()
    ref = scrapy.Field()
    thumb = scrapy.Field()


