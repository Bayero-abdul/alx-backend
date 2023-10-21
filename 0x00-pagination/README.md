# 0x00. Pagination

## Project Overview
This project focuses on implementing various pagination techniques for a dataset of popular baby names. The project tasks involve writing code for simple pagination, hypermedia pagination, and deletion-resilient hypermedia pagination. You will create a Python server class to paginate the dataset, and you will implement methods for fetching data based on page and page size parameters, as well as handling the impact of deleted items between queries.

## Tasks
The project consists of several tasks:

1. **Simple Helper Function**: Implement a helper function named `index_range` that calculates the start and end indexes for pagination based on page and page size parameters.

2. **Simple Pagination**: Create a `Server` class that allows simple pagination by fetching data based on page and page size parameters. You should also handle assertions to ensure the parameters are valid integers.

3. **Hypermedia Pagination**: Extend the `Server` class with a `get_hyper` method that returns paginated data along with additional hypermedia metadata, including the next page, previous page, and total number of pages.

4. **Deletion-Resilient Hypermedia Pagination**: Implement a `get_hyper_index` method in the `Server` class that ensures deletion-resilient hypermedia pagination. This method calculates the appropriate indexes for retrieving data even when items are deleted between queries.

Follow the instructions in each task to complete the project successfully.

For detailed task descriptions and code examples, please refer to the provided project files.

## Project Structure
The project directory structure is organized as follows:

- `0-simple_helper_function.py`: Contains the implementation of the `index_range` helper function for task 1.
- `1-simple_pagination.py`: Contains the `Server` class and the implementation of simple pagination for task 2.
- `2-hypermedia_pagination.py`: Extends the `Server` class with the `get_hyper` method for task 3.
- `3-hypermedia_del_pagination.py`: Extends the `Server` class with the `get_hyper_index` method for deletion-resilient hypermedia pagination for task 4.
- `0-main.py`, `1-main.py`, `2-main.py`, `3-main.py`: Main files to run and test the tasks with example scenarios.