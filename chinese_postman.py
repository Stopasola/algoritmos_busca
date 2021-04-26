from node import Node
from graph import Graph

def odd_nodes(graph):
    odd_list = []

    graph_structure = graph.structure()
    print('grap_structure ', graph_structure)
    print('grap_structure values', graph_structure.values())
    print('grap_structure keys', graph_structure.keys())

    count = 0
    for node in graph_structure.keys():
        print('node', node)
        for values in graph_structure.values():
            for i in values:
                if node == i:
                    count += 1
        print('count', count)
        count = 0


def possible_pairings():
    pass


def calculate_pairings():
    pass


def add_edges():
    pass


def calculate_total_distance():
    pass


def start(graph):
    odd_nodes(graph)


# Fiz com base nos exemplos, temos que verificar com um code para ter ctz
# https://towardsdatascience.com/chinese-postman-in-python-8b1187a3e5a

