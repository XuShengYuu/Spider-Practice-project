# -*- coding: utf-8 -*-
import scrapy
from dy2018_scrapy.items import Dy2018ScrapyItem

class Dy2018Spider(scrapy.Spider):
    name = 'dy2018'
    allowed_domains = ['dy2018.com']
    start_urls = ['https://www.dy2018.com/html/gndy/dyzz/index.html']

    def parse(self, response):
        titles = response.xpath("//*[@id='header']//div[@class='bd3r']//table[@class='tbspan']/tr[2]/td[2]/b/a/text()").extract()
        links = response.xpath("//*[@id='header']//div[@class='bd3r']//table[@class='tbspan']/tr[2]/td[2]/b/a/@href").extract()
        introduces = response.xpath("//*[@id='header']/div[@class='contain']/div[@class='bd2']/div[@class='bd3']/div[@class='bd3r']//tr[4]/td/text()").extract()
        for title,link,introduce in zip(titles,links,introduces):
            item = Dy2018ScrapyItem()
            item['title'] = title
            item['link'] = link
            item['introduce'] = introduce
            yield item
            for i in range(1,10):
                url = 'https://www.dy2018.com/html/gndy/dyzz/index_'+str(i)+'.html'
                yield scrapy.http.Request(url,callback=self.parse)