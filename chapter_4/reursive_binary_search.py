#! python3
# recursive_binary_search.py
# Author: Michael Koundouros
"""
Ref: Chapter 4
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
EXERCISE 4.4 - This is an example of a divide & conquer algorithm, applied to binary search and utilises
recursive functions.
"""


def bin_search(my_list, search_item):
    # Function to binary search a list recursively
    last = len(my_list) - 1
    mid = last // 2
    print(my_list, mid)

    if my_list[mid] == search_item:
        print('here', my_list, mid)
        return mid

    elif my_list[mid] > search_item:
        new_list = my_list[:mid]
        i = -1
        print('greater', my_list, mid)

    else:
        new_list = my_list[mid + 1:]
        i = 1
        print('less', my_list, mid)

    idx = mid + i * bin_search(new_list, search_item)
    return idx


def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    search_item = 6

    print(f'Search item {search_item} found at index {bin_search(my_list, search_item)}')


if __name__ == '__main__':
    main()
