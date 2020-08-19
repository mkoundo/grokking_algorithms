#! python3
# recursive_max.py
# Author: Michael Koundouros
"""
Ref: Chapter 4
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
EXERCISE 4.3
"""


def rec_max(my_list):
    # Function to find maximum number in a list recursively
    while my_list:
        return max(my_list.pop(), rec_max(my_list))
    return 0


def main():
    my_list = [1, 3, 4, 5, 8, 5, 7]
    print(f'Maximum is {rec_max(my_list)}')


if __name__ == '__main__':
    main()
