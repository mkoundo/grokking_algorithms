#! python3
# recursive_factorial_search.py
# Author: Michael Koundouros
"""
n! example using recursion
"""


def n_factorial(n):
    if n == 0:
        return 1
    return n * n_factorial(n-1)


n = 6
print(f'{n}! = {n_factorial(n)}')
