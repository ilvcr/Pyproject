#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 03 Apr 2018 02:31:16 PM CST
# File Name: strategies3.py
# Description:
              策略三：直接使用保存登陆状态的Cookie模拟登陆

              如果实在没办法了，可以用这种方法模拟登录，虽然麻烦一点，但是成功率100%
"""

import scrapy

class RenrenSpider(scrapy.Spider):
    name = "renren"
    allowed_domains = ["renren.com"]
    start_urls = (
            'http://www.renren.com/111111',
            'http://www.renren.com/222222',
            'http://www.renren.com/333333',
            )

    cookies = {
    "anonymid" : "ixrna3fysufnwv",
    "_r01_" : "1"
    "ap" : "327550029"
    "JSESSIONID" : "abciwg61A_RvtaR53GjOv",
    "depovince" : "GW",
    "springskin" : "set",
    "jebe_key" :
    "f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1486198628950",
    "t" : "691808127750a83d33704a565d8340ae9",
    "societyguester" : "691808127750a83d33704a565d8340ae9",
    "id" : "327550029",
    "xnsid" : "f42b25cf",
    "loginfrom" : "syshome"
    }

    #可以重写Spider类的start_requests方法，附带Cookie值，发送POST请求
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookie = self.cookie, callback = self.parse_page)

    #处理响应
    def parse_page(self, response):
        print("=========================" + response.url)
        with open ("deng.html", "w") as filename:
            filename.write(response.body)

 = {"email" : "mr_mao_hacker@163.com", "password" : "axxxxxxxe"},
