# -*- coding: utf-8 -*-
import unittest
import os

from globocomtrends.spiders import parser


class ParserTests(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.current_dir = os.getcwd()

    def test_should_parser_item_from_response(self):
        item = parser.parse_item(
                fake_response_from_file('resources/comments.html')
        )
        self.assertIsNotNone(item['title'])


if __name__ == '__main__':
    unittest.main()
