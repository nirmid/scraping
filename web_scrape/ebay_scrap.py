import os
import json
from typing import Any
import requests
from bs4 import BeautifulSoup
from web_interface import WebScrap


class Ebay(WebScrap):
    def __init__(self, name: str, search_url: str) -> None:
        super().__init__(name, search_url)
        self.directory = "out"
        # Initialize output directory:
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

    def search_item(self, item: str) -> str | None:
        param = {
            'nkw': item
        }
        response = requests.get(self.search_url, params=param, timeout=10)
        if response.status_code == 200:
            parsed_html = BeautifulSoup(response.text, "html.parser")
            return parsed_html
        else:
            return None

    def scrap_pages(self, pages: BeautifulSoup) -> None:
        items = [link.get("href") for link in pages.find_all(
            "a", attrs={"class": "s-item__link"})]
        while items is not None:
            self.scrap_page(items)
            next_page_element = pages.find(
                "a", {"aria-label": "Go to the next search page"})
            if next_page_element:
                next_page_url = next_page_element.get("href")
                pages_html = requests.get(next_page_url, timeout=10)
                pages = BeautifulSoup(pages_html.text, "html.parser")
                if pages.status_code == 200:
                    items = [link.get("href") for link in pages.find_all(
                        "a", attrs={"class": "s-item__link"})]
                    continue
                else:
                    print("Couldn't access next page")
                    break
            else:
                break

    def scrap_page(self, page: list[Any]) -> None:
        for item in page:
            item_page = requests.get(item, timeout=10)
            if item_page.status_code == 200:
                item_page_parsed = BeautifulSoup(item_page.text, "html.parser")
                self.scrap_item(item_page_parsed)
            else:
                print("There is a problem accessing item's page:  "+item)

    def scrap_item(self, item: BeautifulSoup) -> None:
        product_id = item.find(
            "span", attrs={"class": "ux-textspans ux-textspans--BOLD"}).text
        img_path = item.find(
            "img", attrs={"class": "ux-image-magnify__image--original"}).get("src")
        price = item.find(
            "div", attrs={"class": "x-price-primary"}).find("span").text
        title = item.find(
            "h1", attrs={"class": "x-item-title__mainTitle"}).find("span").text

        file_data = {
            "Title": title,
            "Image Path": img_path,
            "Price": price
        }

        file_name = f"{self.name}_{product_id}.json"
        file_path = os.path.join(self.directory, file_name)

        with open(file_path, "w") as file:
            json.dump(file_data, file, indent=4)
