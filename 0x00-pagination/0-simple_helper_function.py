#!/usr/bin/env python3
"""0-simple_helper_function.py

Simple helper function.

"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns range of indexes to return in a list for those
    particular pagination parameters.
    """
    end_index = page_size * page
    start_index = end_index - page_size
    return (start_index, end_index)
