# -*- coding: utf-8 -*-

from globocomtrends.items import PageInfo


def parse_item(response):
    item = PageInfo()
    print(item)
    item['title'] == response.xpath('//title').extract()
    item['comment_count'] = response.xpath(
            '//div[contains(@id,"glbComentarios-contador")]'
    ).extract()
    return item
