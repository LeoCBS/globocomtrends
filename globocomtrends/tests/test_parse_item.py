import unittest
from globocomtrends.spiders.globocom import GlobocomSpider
from globocomtrends.tests import fake_response_from_file

class GlobocomSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = GlobocomSpider()

    def test_parse(self):
        results = self.spider.parse(fake_response_from_file('raw_files/globo.html'))
        for item in results:
            self.assertIsNotNone(item['title'])
            #self.assertIsNotNone(item['commentsCount'])

if __name__ == '__main__':
    unittest.main()
