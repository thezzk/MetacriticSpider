# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class GameImageItem(scrapy.Item):
    gameId = scrapy.Field()
    imageFileName = scrapy.Field()
    imageUrl = scrapy.Field()

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
    userRatesCnt = scrapy.Field()
    imageUrl = scrapy.Field()
    trailerUrl = scrapy.Field()
    gameId = scrapy.Field()
    #imageLocalpath = scrapy.Field()
    #file_urls = scrapy.Field()
    #files = scrapy.Field()

class MetacriticspiderItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
