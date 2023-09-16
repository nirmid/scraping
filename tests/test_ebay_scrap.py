import os
import unittest
from src.ebay import Ebay


class TestEbayScrape(unittest.TestCase):

    def setUp(self) -> None:
        self.ebay_instace = Ebay()

    def test_search(self):
        result_search = self.ebay_instace.search_item("Rolex")
        self.assertIsNotNone(result_search)

    def test_pages_scrap(self):
        result_search = self.ebay_instace.search_item("Rolex")
        self.ebay_instace.scrap_pages(result_search)
        folder = os.listdir(self.ebay_instace.directory)
        self.assertTrue(len(folder) > 0)


if __name__ == '__main__':
    unittest.main()
