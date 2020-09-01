 # -*- coding: utf-8 -*-
import time
import scrapy
import pandas as pd
import pdb
import re
from scrapy import Request
from MetacriticSpider.items import GameImageItem

class GamedetailspiderSpider(scrapy.Spider):
    name = 'GameImageSpider'
    allowed_domains = ['metacritic.com']
    custom_settings = {
        'ITEM_PIPELINES':{
            'MetacriticSpider.pipelines.MetacriticspiderPipeline': 300,
        }
    }
 
    gameIndex = 0
    gameDetailDf = {} 
    def __init__(self):
        self.gameDetailDf = pd.read_csv('./GameDetail.csv')
        self.start_urls = [self.gameDetailDf.imageUrl[self.gameIndex]]
        super().__init__()
    
    def gameImgErrback(self, failure):
        pdb.set_trace()
    
    def parse(self, response):
        item = GameImageItem()
        item['gameId'] = item['imageFileName'] = item['imageUrl'] = "" 
        item['imageUrl'] = [self.gameDetailDf.imageUrl[self.gameIndex]]
        item['gameId'] = self.gameDetailDf.gameId[self.gameIndex]
       
        yield item
        self.gameIndex = self.gameIndex + 1
        if(self.gameIndex < len(self.gameDetailDf.imageUrl)):
            time.sleep(1)
            next_url = self.gameDetailDf.imageUrl[self.gameIndex]
            #if(int(self.gameIndex) >= 32):
            #    pdb.set_trace()
            yield Request(url=next_url, callback=self.parse, errback=self.gameImgErrback, dont_filter=True)
