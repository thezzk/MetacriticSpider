# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class GameDetailItem(scrapy.Item):
    title = scrapy.Field()
    platform = scrapy.Field()
    company = scrapy.Field()
    release = scrapy.Field()
    description = scrapy.Field()
    metascore = scrapy.Field()
    players = scrapy.Field()
    genre = scrapy.Field()
    otherPlatform = scrapy.Field()
    #trailerUrl = scrapy.Field()

class MetacriticspiderItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    pass
