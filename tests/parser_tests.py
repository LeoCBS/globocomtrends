# -*- coding: utf-8 -*-
import unittest
import os

from globocomtrends.spiders import parser
from tests import fake_response_from_file


class ParserTests(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.current_dir = os.getcwd()

    def test_should_parser_item_from_response(self):
        item = parser.parse_item(
                fake_response_from_file('resources/comments.html')
        )
        self.assertIn('title', item)
        self.assertIn('comments_count', item)
        self.assertEqual(item['comments_count'], 643)


if __name__ == '__main__':
    unittest.main()
