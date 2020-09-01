# -*- coding: utf-8 -*-
import time
import scrapy
import pandas as pd
from scrapy import Request
from MetacriticSpider.items import MetacriticspiderItem

class MetacriticgamesSpider(scrapy.Spider):
    name = 'metacriticGames'
    allowed_domains = ['metacritic.com']
    start_urls = ['https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?page=0']
    #endPage = 4
    #curPage = 0
    urlIndex = 0
    
    def __init__(self):
        self.urlDataframe = pd.read_csv('./TarUrls.csv')
        self.start_urls = [self.urlDataframe.TarUrl[self.urlIndex]]
        super().__init__()
    
    def parse(self, response):
        
       
        print(len(response.xpath("//td[@class='clamp-summary-wrap']")))
        for each in response.xpath("//td[@class='clamp-summary-wrap']"):
            item = MetacriticspiderItem()
            url = each.xpath("a/@href").extract()
            name = each.xpath("a/h3/text()").extract()
            item['url'] = "https://www.metacritic.com" + str(url[0])
            item['name'] = name[0]
            yield item
        self.urlIndex = self.urlIndex + 1
        if(self.urlIndex < len(self.urlDataframe.TarUrl)):
            time.sleep(1)
            next_url = self.urlDataframe.TarUrl[self.urlIndex]
            yield Request(next_url)
