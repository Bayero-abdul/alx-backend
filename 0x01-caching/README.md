# Caching Algorithms Project

## Project Overview

This project explores different caching algorithms implemented in Python. Caching is a technique used to store frequently accessed data in a fast-access storage area, improving the overall performance of applications. The following caching algorithms are covered:

1. **Basic Cache**: A simple caching system without a size limit.
2. **FIFO Cache (First-In-First-Out)**: Implements a cache with a limit, removing the oldest item when the limit is reached.
3. **LIFO Cache (Last-In-First-Out)**: Similar to FIFO but removes the newest item when the limit is reached.
4. **LRU Cache (Least Recently Used)**: Removes the least recently used item when the limit is reached.
5. **MRU Cache (Most Recently Used)**: Removes the most recently used item when the limit is reached.

## Learning Objectives

By working on this project, you will gain a deeper understanding of:

- What a caching system is and its importance in optimizing data retrieval.
- The concepts and principles behind different cache replacement policies.
- How to implement caching algorithms in Python.

## Project Structure

- `base_caching.py`: Defines a base caching class with common methods and constants.
- `0-basic_cache.py`: Implements a basic cache class without a size limit.
- `1-fifo_cache.py`: Implements a FIFO cache.
- `2-lifo_cache.py`: Implements a LIFO cache.
- `3-lru_cache.py`: Implements an LRU cache.
- `4-mru_cache.py`: Implements an MRU cache.

## Usage

You can run the provided test scripts (0-main.py, 1-main.py, 2-main.py, 3-main.py, 4-main.py) to see these caching algorithms in action. These scripts demonstrate how to create cache instances, store and retrieve data, and how the different algorithms handle cache limits.

## Requirements

- Python 3.7
- Pycodestyle 2.5 (for code style compliance)
