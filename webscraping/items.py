# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class Contry(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    gdp= Field()
    mobile = Field()
    internet = Field()
