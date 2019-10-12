import unittest

from model.news import News

class TestNews(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_news_from_dict(self):
        news = News.news_from_dict(
            {
                "author": "1",
                "title": "b"
            }
        )
        actual = news.author
        expected = '1'

        self.assertEqual(actual, expected)

        actual = news.title
        expected = 'b'

        self.assertEqual(actual, expected)



    def test_to_string(self):
        news = News.news_from_dict(
            {
                "author": "1",
                "title": "b"
            }
        )

        actual = news.to_string()
        expected = 'Author: 1, Title: b'
        self.assertEqual(actual, expected)

        