#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 03 Apr 2018 02:17:09 PM CST
# File Name: strategies2.py
# Description:
              策略二：标准的模拟登陆步骤

              正统模拟登录方法：

              1. 首先发送登录页面的get请求，获取到页面里的登录必须的参数（比如说zhihu登陆界面的 _xsrf）

              2. 然后和账户密码一起post到服务器，登录成功
"""
import scrapy

class Renren2spider(scrapy.Spider):
    name = "renren2"
    allowed_domain2 = ["renren.com"]
    start_urls = (
            "http://www.renren.com/Plogin.do"
            )

    #处理start_urls里的登陆url的响应内容，提取登陆需要的参数(如果需要的话)
    def parse(self, response):
        #提取登陆需要的参数
        #_xsrf = response.xpath("//_xsrf").extract()[0]


        #发送请求参数，并调用指定回掉函数处理
        yield scrapy.FormRequest.from_response(
                    response,
                    formdata = {"email" : "mr_mao_hacker@163.com", "password" : "axxxxxxxe"},#,"_xsrf" = _xsrf},
                    callback = self.parse_page
                    )

    #获取登陆成功状态，访问需要登陆后才能访问的页面
    def parse_page(self, response):
        url = "http://www.renren.com/422167102/profile"
        yield scrapy.Request(url, callback = self.parse_newpage)

    #处理响应内容
    def parse_newpage(self, response):
        with open("xiao.html", "w") as filename:
            filename.write(response.body)
