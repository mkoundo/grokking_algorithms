#! python3
# binary_search.py
# Author: Michael Koundouros
"""
Ref: Chapter 1 - Introduction to Algorithms
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
Book Solution
"""


def binary_search(search_list, item):
    low = 0
    high = len(search_list) - 1
    while low <= high:
        mid = (low + high)
        guess = search_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def main():
    my_list = [1, 3, 5, 7, 9]
    search_item = 5

    print(f'Search item {search_item} found at index {binary_search(my_list, search_item)}')


if __name__ == '__main__':
    main()
