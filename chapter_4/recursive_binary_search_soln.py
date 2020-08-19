#! python3
# recursive_binary_search_soln.py
"""
Ref: Chapter 4
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
EXERCISE 4.4 - This is an example of a divide & conquer algorithm, applied to binary search with recursive functions.
"""


def binary_search(items, target, start=None, end=None):
    if start is None:
        start = 0                                   # 'start' defaults to the 0 index.
    if end is None:
        end = len(items) - 1                        # 'end' defaults to the last index.

    if start > end:                                 # BASE CASE
        return None                                 # The 'target' has not been found.

    mid = (start + end) // 2
    if target == items[mid]:                        # BASE CASE
        return mid                                  # 'target' has been found
    elif target < items[mid]:                       # RECURSIVE CASE
        return binary_search(items, target, start, mid - 1)
    elif target > items[mid]:                       # RECURSIVE CASE
        return binary_search(items, target, mid + 1, end)


print(binary_search([1, 4, 8, 11, 13, 16, 18, 19, 20, 23, 31], 31))
