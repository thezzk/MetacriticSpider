# -*- coding: utf-8 -*-
import time
import scrapy
from scrapy import Request
from MetacriticSpider.items import MetacriticspiderItem

class MetacriticgamesSpider(scrapy.Spider):
    name = 'metacriticGames'
    allowed_domains = ['metacritic.com']
    start_urls = ['https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?page=0']
#class="clamp-summary-wrap"
#//*[@id="main_content"]/div[1]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/a
#//*[@id="main_content"]/div[1]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/a/h3
    endPage = 4
    curPage = 0
    def parse(self, response):
        
        #items = []
        print(len(response.xpath("//td[@class='clamp-summary-wrap']")))
        for each in response.xpath("//td[@class='clamp-summary-wrap']"):
            item = MetacriticspiderItem()
            url = each.xpath("a/@href").extract()
            name = each.xpath("a/h3/text()").extract()
            item['url'] = "https://www.metacritic.com" + str(url[0])
            item['name'] = name[0]
            yield item
        self.curPage = self.curPage + 1
        if(self.curPage < self.endPage):
            time.sleep(3)
            next_url = 'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?page=' + str(self.curPage)
            yield Request(next_url)
