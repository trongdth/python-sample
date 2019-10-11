import unittest

from bl.news import update_feed

class TestSample1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_update_feed(self):
        actual = update_feed(country='us')
        expected = True
        self.assertEquals(actual, expected)