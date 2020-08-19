#! python3
# breadth_first.py
# Author: Michael Koundouros
"""
Ref: Chapter 5
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
Breadth first search is a search algorithm that runs on graphs. It can help answer two types of questions:
• Question type 1: Is there a path from node A to node B?
• Question type 2: What is the shortest path from node A to node B?
The breadth first search algorithm has runtime of O(V+E), where V is the number of vertices and E is the number of edges
"""


from collections import deque


def breadth_search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []                           # List to keep track of names already searched

    # In Python, there’s a specific object in the collections module that you can use for linked lists called deque
    # (pronounced “deck”), which stands for double-ended queue.
    # collections.deque uses an implementation of a linked list in which you can access, insert, or remove elements
    # from the beginning or end of a list with constant O(1) performance.
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)      # Marks this person as searched
    return False


def person_is_seller(name):
    return name[-1] == 'm'                          # Return true if person's name ends with letter m


graph1 = dict()
graph1['you'] = ['alice', 'bob', 'claire']
graph1['bob'] = ['anuj', 'peggy']
graph1['alice'] = ['peggy']
graph1['claire'] = ['thom', 'jonny']
graph1['anuj'] = []
graph1['peggy'] = []
graph1['thom'] = []
graph1['jonny'] = []


print(breadth_search(graph1, 'you'))
