#! python3
# selectionsort.py
# Author: Michael Koundouros
"""
Ref: Chapter 4
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
Selection Sort - described in chapter 2. Runtime of O(n^2)
"""


def selsort(items, start):

    if items is None or len(items) == 0:              # Base case
        return []
    elif len(items) == 1:
        return items

    if start == 0:
        max_item_list = []

    # find max item
    max_item = 0
    for item in items:
        if item > max_item:
            max_item = item
            print('ok')
            print(max_item)
    max_item_list.append(max_item)
    print(f'max item: {max_item_list}')
    items.remove(max_item)
    print(f'red item: {items}')
    print(f'selsort: {selsort(items, start)}')
    max_item_list.extend(selsort(items, 1))

    return max_item_list


unsorted_list = [5, 4, 1, 8]
print(f'answer: {selsort(unsorted_list, start=0)}')
