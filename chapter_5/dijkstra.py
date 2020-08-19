#! python3
# dijkstra.py
# Author: Michael Koundouros
"""
Ref: Chapter 5
Ref: Grokking Algorithms: An illustrated guide for programmers and other curious people, A. Bhargava, 2016.
Breadth first search is a search algorithm that runs on graphs. It can help answer two types of questions:
• Question type 1: Is there a path from node A to node B?
• Question type 2: What is the shortest path from node A to node B?
Dijkstra algorithm is an extension of breadth search to account for weighted graphs. Its runtime is O(V log V) where
V is the number of vertives
"""


def dijkstra(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return costs, parents


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# Graph dictionary
graph1 = {}
graph1['start'] = {}
graph1['start']['a'] = 6
graph1['start']['b'] = 2

graph1['a'] = {}
graph1['a']['fin'] = 1

graph1['b'] = {}
graph1['b']['a'] = 3
graph1['b']['fin'] = 5

graph1['fin'] = {}

# Costs Dictionary
infinity = float('inf')             # Define infinity
costs1 = {}
costs1['a'] = 6
costs1['b'] = 2
costs1['fin'] = infinity

# Parents Dictionary
parents1 = {}
parents1['a'] = 'start'
parents1['b'] = 'start'
parents1['fin'] = None


print(dijkstra(graph1, costs1, parents1))
