# -*- coding: utf-8 -*-
import scrapy


class Dy2018Spider(scrapy.Spider):
    name = 'dy2018'
    allowed_domains = ['dy2018.com']
    start_urls = ['http://dy2018.com/']

    def parse(self, response):
        pass
