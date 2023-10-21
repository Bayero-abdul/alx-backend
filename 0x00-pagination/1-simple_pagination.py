#!/usr/bin/env python3
"""1-simple_pagination.py """


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """Returns range of indexes to return in a list for those
        particular pagination parameters.
        """
        end_index = page_size * page
        start_index = end_index - page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets a page within a certain range of indexes in a dataset list. """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start_index, end_index = Server.index_range(page, page_size)
        d = self.dataset()
        return [] if start_index >= len(d) else d[start_index: end_index]
