# -*- coding: utf-8 -*-
import unittest
import os


class ParserTests(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.current_dir = os.getcwd()

    def _join_absolute_path(self, path):
        return os.path.join(self.current_dir, path)

    def test_should_check_utf_8_success(self):
        abs_path = self._join_absolute_path('tests/resource_tests/utf.srt')
        self.assertTrue(attacher.check_charset_utf(abs_path))


if __name__ == '__main__':
    unittest.main()
