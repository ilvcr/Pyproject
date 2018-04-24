# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
from Cosplay import settings
import os

class ImageDownloadPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:
            images = []
            dir_path = '%s%s' %(settings.IMAGES_STORE, spider.name)

            if not os.path.exixts(dir_path):
                os.makedirs(dir_path)

            for image_url in item['image_urls']:
                us = image_url.split('/')[3:]
                image_file_name = '_'.jion(us)
                file_path = '%s%s'%(dir_path, image_file_name)
                images.appemd(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break


            item['images'] = images
        return item