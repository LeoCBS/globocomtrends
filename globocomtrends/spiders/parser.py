# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

from globocomtrends.items import PageInfoItem


def parse_item(response):
    item = PageInfoItem()
    soap = BeautifulSoup(response.body, 'html.parser')
    raw_meta = soap.find('meta', attrs={'property': 'og:title'})
    if raw_meta is not None:
        item['title'] = raw_meta['content']

    raw_comments_count = soap.find('div', {'class': 'glbComentarios-contador'})
    if raw_comments_count is not None:
        item['comments_count'] = _string_to_int(raw_comments_count.text)
    return item


def _string_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None
