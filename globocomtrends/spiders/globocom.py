# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class GlobocomSpider(CrawlSpider):
    name = 'globocom'
    allowed_domains = ['globo.com']
    start_urls = ['http://globo.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        i['title'] = response.xpath('//title').extract()
        return i
