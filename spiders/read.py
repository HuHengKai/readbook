# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ReadbookItem


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1107_1.html']

    rules = (
        # Rule(LinkExtractor(allow=r'/book/1107_\d+.html'),follow=False),
        #/book/13849069/
        Rule(LinkExtractor(allow=r'/book/\d+/'),callback='parse_item',follow=False),
    )

    def parse_item(self, response):
        item=ReadbookItem()
        print("success")
        name=response.xpath('//div[@class="book-title"]//text()').extract_first()
        price=response.xpath('//p[@class="price"]//span/text()').extract_first()
        print(f"name is {name},price is {price}")
        # img_list =response.xpath('//div[@class="bookslist"]//img')
        # for img in img_list:
        #     src=img.xpath('./@data-original').extract_first()
        #     name=img.xpath('./@alt').extract_first()
        #     book = ReadbookItem(src=src, name=name)
        item["src"]=price
        item["name"]=name
        yield item