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
import time


def qsort(items, pivot_choice):

    if len(items) < 2:
        return items                        # Base case: 0 or 1 items
    elif len(items) == 2:
        return [min(items), max(items)]     # Base case: 2 items

    # Partition the list
    if pivot_choice:
        pivot = random.choice(items)            # choose random pivot for average runtime of O(n log n)
    else:
        pivot = items[0]                        # Choose first item in list as pivot

    items.remove(pivot)
    left_array = [item for item in items if item <= pivot]
    right_array = [item for item in items if item > pivot]

    # Recurse partitioned list
    sorted_items = qsort(left_array, pivot_choice)
    sorted_right = qsort(right_array, pivot_choice)
    sorted_items.append(pivot)
    sorted_items.extend(sorted_right)

    return sorted_items


# Create unsorted list from random numbers
unsorted_set = {int(10000*random.random()) for _ in range(1100)}    # create a set to avoid duplicate entries
unsorted_list = list(unsorted_set)

# removing the pivot in the qsort function also affects
# the unsorted list because unsorted_list and items point to the same
# list in memory. Therefore use a copy:
unsorted_list_copy = unsorted_list.copy()

start_time = time.time()
print(qsort(unsorted_list, False))
end_time = time.time()
print(f'First item pivot done in {end_time-start_time}s')

start_time = time.time()
print(qsort(unsorted_list_copy, True))
end_time = time.time()
print(f'Random pivot done in {end_time-start_time}s')
