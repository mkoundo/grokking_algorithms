#! python3
# recursive_sum.py
# Author: Michael Koundouros
"""
Ref: Chapter 4
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
EXERCISE 4.1
"""


def rec_sum(my_list):
    # Function to sum numbers in a list recursively
    while my_list:
        total = my_list.pop() + rec_sum(my_list)
        return total
    return 0


def main():
    my_list = [1, 3, 4, 5, 8]
    print(f'Sum is {rec_sum(my_list)}')


if __name__ == '__main__':
    main()
