# -*- coding: utf-8 -*-
import time
import scrapy
import pandas as pd
import pdb
import re
from scrapy import Request
from MetacriticSpider.items import GameDetailItem

class GamedetailspiderSpider(scrapy.Spider):
    name = 'GameDetailSpider'
    allowed_domains = ['metacritic.com']
    custom_settings = {
        'ITEM_PIPELINES':{
        }
    }
    #start_urls = ""
    gameIndex = 0
    urlDataframe = {} 
    def __init__(self):
        self.urlDataframe = pd.read_csv('./GameUrls.csv')
        #pdb.set_trace()
        self.start_urls = [self.urlDataframe.url[self.gameIndex]]
        super().__init__()
    
    def parse(self, response):
        title = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[2]/a/h1/text()').extract_first()
        
        company = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[3]/ul/li[1]/span[2]/a/text()').extract_first()
        
        release = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[3]/ul/li[2]/span[2]/text()').extract_first()
        
        descriptionPath = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]')#/div/div/div[2]/div[2]/div[1]/ul/li/span[2]/span/span[2]/text()').extract_first()
        #description = ""
        description = descriptionPath.xpath('//*[@class="summary_detail product_summary"]/span[2]/span/text()').extract_first()
        #pdb.set_trace()
        if description == None or description.strip() == "": #collapse item or None
            description = descriptionPath.xpath('//*[@class="summary_detail product_summary"]/span[2]/span/span[2]/text()').extract_first()
            if description == None:
                description = ""
        
        metascore = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]')#/div/div/div[2]/div[1]/div[1]/div/div/a/div/span/text()
        metascore = metascore.xpath('//*[@class="metascore_w xlarge game positive"]/span/text()').extract_first()
        
        platform = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[2]/span/a/text()').extract_first()
        
        players = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]')#.extract_first()#/div/div/div[2]/div[2]/div[2]/ul/li[3]/span[2]/text()
        players = players.xpath('//*[@class="summary_detail product_players"]/span[2]/text()').extract_first()
        
        
        userRatesCnt = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]')#div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/p/span[2]/a/text()').extract_first()
        userRatesCnt = userRatesCnt.xpath('//*[@class="userscore_wrap feature_userscore"]/div[2]/p/span[2]/a/text()').extract_first()
        
        imageUrl = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]')
        imageUrl = imageUrl.xpath('//*[@class="product_image large_image"]/@src').extract_first()
        #//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div[1]/div/img
        #//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div/img
        #<img class="product_image large_image" src="https://static.metacritic.com/images/products/games/2/1d340c792338fa16de96bd8b60d3cab5-98.jpg" alt="Persona 5 Royal Image">
        #pdb.set_trace()
        trailerUrl = response.xpath('//*[@id="videoContainer_wrapper"]/@data-mcvideourl').extract_first()
        item = GameDetailItem()
        item['title'] = item['company'] = item['release'] = item['description'] = item['metascore'] = item['platform'] = item['otherPlatform'] = item['players'] =  item['genre'] = item['userRatesCnt'] = item['imageUrl'] = item['trailerUrl'] = ""
        
        item['title'] = title
        item['company'] = company
        item['release'] = release
        item['description'] = description
        item['metascore'] = metascore
        item['platform'] = platform
        item['players'] = players
        item['userRatesCnt'] = userRatesCnt
        item['imageUrl'] = [imageUrl]
        item['trailerUrl'] = trailerUrl
        item['gameId'] = self.gameIndex
        # if trailerUrl != None:
            # item['file_urls'] = [trailerUrl]
        # else:
            # #pdb.set_trace()
            # item['file_urls'] = []
            
        otherPlatformLst = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[3]/ul/li[3]/span/a')
        for each in otherPlatformLst:
            item['otherPlatform'] += each.xpath('text()').extract_first() + ','
            
 
    
        
        genre = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]')
        genre = genre.xpath('//*[@class="summary_detail product_genre"]/span[@class="data"]')
        for each in genre:
            item['genre'] += each.xpath('text()').extract_first() + ","
        
       
        yield item
        
        self.gameIndex = self.gameIndex + 1
        if(self.gameIndex < len(self.urlDataframe.url)):
            time.sleep(1)
            next_url = self.urlDataframe.url[self.gameIndex]
            yield Request(next_url)
