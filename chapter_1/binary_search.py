#! python3
# binary_search.py
# Author: Michael Koundouros
"""
Ref: Chapter 1 - Introduction to Algorithms
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
"""


def binary_search(my_list, search_item):
    low = -1
    high = len(my_list)
    mid = (high - low) // 2
    while my_list[mid] != search_item:
        if my_list[mid] < search_item:
            low = mid
            i = 1
        else:
            high = mid
            i = -1
        mid = mid + i*((high - low) // 2)
        if mid == low or mid == high:
            return None
    return mid


def main():
    my_list = [1, 3, 5, 7, 9]
    search_item = 9

    print(f'Search item {search_item} found at index {binary_search(my_list, search_item)}')


if __name__ == '__main__':
    main()
