# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class UsagovScrappingItem(scrapy.Item):
    link = scrapy.Field()
    body = scrapy.Field()

class usagovScrappingDataset(scrapy.Item):
	title = scrapy.Field()
	paragraph = scrapy.Field()
