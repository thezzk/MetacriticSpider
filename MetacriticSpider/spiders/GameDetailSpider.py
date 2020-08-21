# -*- coding: utf-8 -*-
import time
import scrapy
import pandas as pd
import pdb
from scrapy import Request
from MetacriticSpider.items import GameDetailItem

class GamedetailspiderSpider(scrapy.Spider):
    name = 'GameDetailSpider'
    allowed_domains = ['metacritic.com']
    #start_urls = ""
    gameIndex = 0
    urlDataframe = {} 
    def __init__(self):
        self.urlDataframe = pd.read_csv('.\games.csv')
        #pdb.set_trace()
        self.start_urls = [self.urlDataframe.url[self.gameIndex]]
        super().__init__()
    
    def parse(self, response):
        title = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[2]/a/h1/text()').extract_first()
        company = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[3]/ul/li[1]/span[2]/a/text()').extract_first()
        release = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[3]/ul/li[2]/span[2]/text()').extract_first()
        description = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/ul/li/span[2]/span/span[2]/text()').extract_first()
        metascore = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/a/div/span/text()').extract_first()
        platform = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[2]/span/a/text()').extract_first()
        item = GameDetailItem()
        item['title'] = item['company'] = item['release'] = item['description'] = item['metascore'] = item['platform'] = item['otherPlatform'] = item['players'] =  item['genre'] = ""
        
        item['title'] = title
        item['company'] = company
        item['release'] = release
        item['description'] = description
        item['metascore'] = metascore
        item['platform'] = platform
        
      
        otherPlatformLst = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[3]/ul/li[3]/span/a')
        for each in otherPlatformLst:
            item['otherPlatform'] += each.xpath('text()').extract_first() + ','
            
 
        players = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/ul/li[3]/span[2]/text()').extract_first()
        item['players'] = players
    
        
        
        genre = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/ul/li[2]/span[@class="data"]')
        for each in genre:
            item['genre'] += each.xpath('text()').extract_first() + ","
        
       
        yield item
        
        self.gameIndex = self.gameIndex + 1
        if(self.gameIndex < len(self.urlDataframe.url)):
            time.sleep(1)
            next_url = self.urlDataframe.url[self.gameIndex]
            yield Request(next_url)
