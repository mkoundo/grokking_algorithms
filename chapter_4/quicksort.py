#! python3
# quicksort.py
# Author: Michael Koundouros
"""
Ref: Chapter 4
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
Quicksort - A sorting routine using divide & conquer and recursion. Runtime is O(n log n)
Assume pivot is first element in list
Assume list has no duplicate elements
"""


def qsort(items):

    if len(items) < 2:
        return items                        # Base case: 0 or 1 items
    elif len(items) == 2:
        return [min(items), max(items)]     # Base case: 2 items

    # Partition the list
    pivot = items[0]
    left_array = [item for item in items[1:] if item <= pivot]
    right_array = [item for item in items[1:] if item > pivot]

    # Recurse partitioned list
    sorted_items = qsort(left_array)
    sorted_right = qsort(right_array)
    sorted_items.append(pivot)
    sorted_items.extend(sorted_right)

    return sorted_items


unsorted_list = [33, 9, 10, 12, 51, 21, 56, 61]
print(qsort(unsorted_list))
