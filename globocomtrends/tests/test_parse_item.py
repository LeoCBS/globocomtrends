import unittest
from globocomtrends.spiders import globocom
from responses import fake_response_from_file

class GlobocomSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = globocom.GlobocomSpider()

    def test_parse(self):
        results = self.spider.parse(fake_response_from_file('raw_files/globo.html'))
        for item in results:
            self.assertIsNotNone(item['title'])
            #self.assertIsNotNone(item['commentsCount'])

if __name__ == '__main__':
    unittest.main()
