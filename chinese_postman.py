from graph import Graph
from node import Node
from a_star import astar_search
from dfs import targetet_DFS

def odd_nodes(graph):
    odd_list = []
    graph_structure = graph.structure()
    print('grap_structure ', graph_structure)

    for node in graph_structure.keys():
        adjacent_nodes = graph.get(node)
        count = len(adjacent_nodes)
        for i in graph_structure.keys():
            if i != node:
                edges = graph.get(i)
                if node in edges:
                    count += 1

        if count % 2 != 0:
            odd_list.append(node)

    print(odd_list)
    return odd_list


def possible_pairings(odd_list):
    pairs = []
    for i in range(len(odd_list)-1):
        pairs.append([])
        for j in range(i+1, len(odd_list)):
            pairs[i].append([odd_list[i], odd_list[j]])
    print(pairs)
    return pairs


def get_pairs(pairs, done = [], final = []):
    global l
    if pairs[0][0][0] not in done:
        done.append(pairs[0][0][0])

        for i in pairs[0]:
            f = final[:]
            val = done[:]
            if i[1] not in val:
                f.append(i)
            else:
                continue

            if len(f) == l:
                pairings_sum.append(f)
                return
            else:
                val.append(i[1])
                get_pairs(pairs[1:], val, f)

    else:
        get_pairs(pairs[1:], done, final)


def calculate_pairings(pairings_sum, graph):
    min_sums = []

    for i in pairings_sum:
        s = 0
        for j in range(len(i)):
            print('i:', i)
            # print(astar_search(graph, i[j][0], i[j][1]))
            print(targetet_DFS(graph, i[j][0], i[j][1]))
            s += targetet_DFS(graph, i[j][0], i[j][1])
        min_sums.append(s)

    print(min_sums)

def calculate_pairings_dfs(pairings_sum, graph):
    min_sums = []
    paths = []
    aux_i = 0
    for i in pairings_sum:
        s = 0
        paths.append([])
        for j in range(len(i)):
            path, cost = targetet_DFS(graph, i[j][0], i[j][1])
            paths[aux_i].append(path)
            print('Cost of: ', i[j][0], 'to: ', i[j][1], 'is:', cost)
            s += cost
        min_sums.append(s)
        aux_i += 1
        print('Total cost of tuple: ', s)

    print(min_sums)
    return paths, min_sums

def add_edges():
    pass


def calculate_total_distance():
    pass

l = 0
pairings_sum = []

def start(graph):
    global l
    odd_list = odd_nodes(graph)
    pairs = possible_pairings(odd_list)
    l = (len(pairs)+1)//2
    print('l', l)
    print(pairs[0][0][0])

    get_pairs(pairs)
    print(pairings_sum)
    paths, min_sums = calculate_pairings_dfs(pairings_sum, graph)
    print(paths)
    print(min_sums)
    # calculate_pairings(pairings_sum, graph)


# Fiz com base nos exemplos, temos que verificar com um code para ter ctz
# https://towardsdatascience.com/chinese-postman-in-python-8b1187a3e5a

