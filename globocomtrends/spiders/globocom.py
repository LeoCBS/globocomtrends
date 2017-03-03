# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import parser


class GlobocomSpider(CrawlSpider):
    name = 'globocom'
    allowed_domains = ['globo.com']
    start_urls = ['http://globo.com/']

    rules = (
        Rule(
            LinkExtractor(allow=r'.html'),
            callback='parse_item', follow=True
        ),
    )

    def parse_item(self, response):
        return parser.parse_item(response)
