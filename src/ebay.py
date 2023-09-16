import os
import json
from typing import Any
import requests
from bs4 import BeautifulSoup
from src.web_interface import WebScrap


class Ebay(WebScrap):
    def __init__(self,) -> None:
        super().__init__("Ebay", "https://www.ebay.com/sch/i.html")
        self.directory = "out"
        # Initialize output directory:
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

    def search_item(self, item: str) -> str | None:
        srch_str = item
        url_search = self.search_url + f"?_nkw={srch_str}&ssPageName=GSTL"
        response = requests.get(url_search, timeout=10)
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
                "a", attrs={"class": "pagination__next icon-link"})
            if next_page_element:
                next_page_url = next_page_element.get("href")
                pages_html = requests.get(next_page_url, timeout=10)
                if pages_html.status_code == 200:
                    pages = BeautifulSoup(pages_html.text, "html.parser")
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
            "div", attrs={"class": "ux-layout-section__textual-display ux-layout-section__textual-display--itemId"}).find("span", attrs={"class": "ux-textspans ux-textspans--BOLD"}).text
        img_path_elements = item.findAll(
            "button", attrs={"class": "ux-image-filmstrip-carousel-item image-treatment image"})
        img_path = [img_path.find("img").get("src")
                    for img_path in img_path_elements]
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
