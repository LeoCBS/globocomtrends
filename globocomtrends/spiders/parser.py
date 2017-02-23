# -*- coding: utf-8 -*-

import scrapy


def parse_item(response):
    item = scrapy.Item()
    item['title'] == response.xpath('//title').extract()
    item['comment_count'] = response.xpath(
            '//div[contains(@id,"glbComentarios-contador")]'
    ).extract()
    return item
