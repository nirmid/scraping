from abc import ABC, abstractmethod


class webScrap(ABC):
    def __init__(self, name: str, search_url: str) -> None:
        self.name = name
        self.search_url = search_url

    @abstractmethod
    def search_item(self, item: str) -> str:
        """Returns URL as str of the item that is being searched 

        Args:
            item (str): item to be searched in the website

        Returns:
            str: URL of the result 
        """
        pass

    def scrap_pages(self, pages_url: str) -> None:
        """Scrap the result pages

        Args:
            pagesURL (str): first page of URL of the result search
        """
        pass

    def scrap_page(self, page_url: str) -> None:
        """Scrap over single page

        Args:
            pageURL (str): single result page URL
        """
        pass

    def scrap_item(self, item_url: str) -> None:
        """Extracts data from the item page and generates a JSON file

        Args:
            itemURL (str): item URL
        """
        pass
