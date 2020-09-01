# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import pdb

# class MetacriticspiderPipeline(object):
    # def process_item(self, item, spider):
        # return item


class MetacriticspiderPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info):
        for image_url in item['imageUrl']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        l =list()
        for p in image_paths:
           l.append(p.split('/')[-1])
        item['imageFileName'] = l
        return item