#! python3
# quicksort_randompivot.py
# Author: Michael Koundouros
"""
Ref: Chapter 4
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
Quicksort - A sorting routine using divide & conquer and recursion. Runtime is O(n log n)
Choose pivot at random
Assume list has no duplicate elements
"""


import random


def qsort(items):

    if len(items) < 2:
        return items                        # Base case: 0 or 1 items
    elif len(items) == 2:
        return [min(items), max(items)]     # Base case: 2 items

    # Partition the list
    pivot = random.choice(items)            # choose random pivot for average runtime of O(n log n)
    items.remove(pivot)
    left_array = [item for item in items if item <= pivot]
    right_array = [item for item in items if item > pivot]

    # Recurse partitioned list
    sorted_items = qsort(left_array)
    sorted_right = qsort(right_array)
    sorted_items.append(pivot)
    sorted_items.extend(sorted_right)

    return sorted_items


unsorted_list = [32, 65, 64, 35, 69, 6, 42, 52, 21, 60]
print(qsort(unsorted_list))
