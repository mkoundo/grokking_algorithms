#! python3
# recursive_count.py
# Author: Michael Koundouros
"""
Ref: Chapter 4
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
EXERCISE 4.2
"""


def rec_count(my_list):
    # Function to count numbers in a list recursively
    while my_list:
        return 1 + rec_count(my_list[1:])
    return 0


def main():
    my_list = [1, 3, 4, 5, 8]
    print(f'Count is {rec_count(my_list)}')


if __name__ == '__main__':
    main()
