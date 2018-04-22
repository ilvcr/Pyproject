#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : 2018年03月25日 星期日 15时50分38秒
# File Name: douban.py
# Description:
"""
import scrapy
from doubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = "ddouban"
    allowed_domains = ["movie.douban.com"]
    start = 0
    url = "https://movie.douban.com/top250?start="
    end = "&filter="
    start_urls = [url + str(start) + end]


    def parse(self, resonpse):

        item = DoubanspiderItem()


        movies = response.xpath("//div[@class=\'info\']")


        for each in movies:
            title = each.xpath('div[@class="hd"]/a/span[@class="title"]/text()').extract()
            content = each.xpath('div[@class="bd"]/p/text()').extract()
            score = each.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            info = each.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()

            item['title'] = title[0]
            #以;作为分割，将content列表里所有的元素合并成一个新的字符串
            item['content'] = ';'.join(content)
            item['score'] = score[0]
            item['info'] = info[0]

            #提交item

            yield item


        if self.start <= 225:
            self.start += 25
            yield scrapy.Request(self.url + str(self.start) + self.end, callback=self.parse)
