from abc import ABC, abstractmethod
from typing import Any


class WebScrap(ABC):
    def __init__(self, name: str, search_url: str) -> None:
        """Web interface that hold name and the search-bar URL

        Args:
            name (str): name of the website
            search_url (str): url of the serach-bar in the website
        """
        self.name = name
        self.search_url = search_url

    @abstractmethod
    def search_item(self, item):
        """Returns page result of the item that is being searched 

        Args:
            item : item to be searched in the website

        Returns:
            str: page of the result 
        """
        pass

    @abstractmethod
    def scrap_pages(self, pages) -> None:
        """Scrap the result pages

        Args:
            pages : first page of of the result search
        """
        pass

    @abstractmethod
    def scrap_page(self, page) -> None:
        """Scrap over single page

        Args:
            page: object thats holds all the items of a single page
        """
        pass

    @abstractmethod
    def scrap_item(self, item) -> None:
        """Extracts data from the item page and generates a JSON file

        Args:
            item : item's url
        """
        pass

    @abstractmethod
    def create_json(self, product_id: str, img_path: list[str], price: str, title: str) -> None:
        """Generates a json file according to params

        Args:
            product_id (str)
            img_path (list[str])
            price (str)
            title (str)
        """
