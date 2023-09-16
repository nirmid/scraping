
import os
import importlib.util
from src.ebay import Ebay


def main():
    market_place = input("Please enter marketplace:  ").lower()
    if market_place == "ebay":
        scraper = Ebay()
        search_word = input("please enter a search word to scrape:  ")
        result = scraper.search_item(search_word)
        if result:
            scraper.scrap_pages(result)
        else:
            print("There was a problem with the search")
    else:
        print("Marketplace is not configured")


if __name__ == '__main__':
    main()
