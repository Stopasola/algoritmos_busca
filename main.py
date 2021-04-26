import csv
from a_star import astar_search
from graph import Graph
import dfs

def open_csv():
    reading_list = list()
    aux_list = list()
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row:
                aux_list.append(row)
            else:
                reading_list.append(aux_list[:])
                aux_list.clear()

    print('reading_list:', reading_list)
    return reading_list


def write_csv(graph):

    with open(filename, mode='a') as graph_file:
        employee_writer = csv.writer(graph_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for g in graph:
            employee_writer.writerow(g)
        employee_writer.writerow([])


def example_graph():
    # Create a graph
    graph = Graph()
    # Create graph connections (Actual distance)
    graph.connect('Frankfurt', 'Wurzburg', 111)
    Node('Wurzburg', 'Frankfurt')
    graph.connect('Frankfurt', 'Mannheim', 85)
    Node('Mannheim', 'Frankfurt')
    graph.connect('Wurzburg', 'Nurnberg', 104)
    Node('Nurnberg', 'Wurzburg')
    graph.connect('Wurzburg', 'Stuttgart', 140)
    Node('Stuttgart', 'Wurzburg')
    graph.connect('Wurzburg', 'Ulm', 183)
    Node('Ulm', 'Wurzburg')
    graph.connect('Mannheim', 'Nurnberg', 230)
    Node('Nurnberg', 'Mannheim')
    graph.connect('Mannheim', 'Karlsruhe', 67)
    Node('Karlsruhe', 'Mannheim')
    graph.connect('Karlsruhe', 'Basel', 191)
    Node('Basel', 'Karlsruhe')
    graph.connect('Karlsruhe', 'Stuttgart', 64)
    Node('Stuttgart', 'Karlsruhe')
    graph.connect('Nurnberg', 'Ulm', 171)
    Node('Ulm', 'Nurnberg')
    graph.connect('Nurnberg', 'Munchen', 170)
    Node('Munchen', 'Nurnberg')
    graph.connect('Nurnberg', 'Passau', 220)
    Node('Passau', 'Nurnberg')
    graph.connect('Stuttgart', 'Ulm', 107)
    Node('Ulm', 'Stuttgart')
    graph.connect('Basel', 'Bern', 91)
    Node('Bern', 'Basel')
    graph.connect('Basel', 'Zurich', 85)
    Node('Zurich', 'Basel')
    graph.connect('Bern', 'Zurich', 120)
    Node('Zurich', 'Bern')
    graph.connect('Zurich', 'Memmingen', 184)
    Node('Memmingen', 'Zurich')
    graph.connect('Memmingen', 'Ulm', 55)
    Node('Ulm', 'Memmingen')
    graph.connect('Memmingen', 'Munchen', 115)
    Node('Munchen', 'Memmingen')
    graph.connect('Munchen', 'Ulm', 123)
    Node('Ulm', 'Munchen')
    graph.connect('Munchen', 'Passau', 189)
    Node('Passau', 'Munchen')
    graph.connect('Munchen', 'Rosenheim', 59)
    Node('Rosenheim', 'Munchen')
    graph.connect('Rosenheim', 'Salzburg', 81)
    Node('Salzburg', 'Rosenheim')
    graph.connect('Passau', 'Linz', 102)
    Node('Linz', 'Passau')
    graph.connect('Salzburg', 'Linz', 126)

    # Make graph undirected, create symmetric connections
    # graph.make_undirected()

    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    heuristics['Basel'] = 204
    heuristics['Bern'] = 247
    heuristics['Frankfurt'] = 215
    heuristics['Karlsruhe'] = 137
    heuristics['Linz'] = 318
    heuristics['Mannheim'] = 164
    heuristics['Munchen'] = 120
    heuristics['Memmingen'] = 47
    heuristics['Nurnberg'] = 132
    heuristics['Passau'] = 257
    heuristics['Rosenheim'] = 168
    heuristics['Stuttgart'] = 75
    heuristics['Salzburg'] = 236
    heuristics['Wurzburg'] = 153
    heuristics['Zurich'] = 157
    heuristics['Ulm'] = 0
    # Run the search algorithm
    path = astar_search(graph, heuristics, 'Frankfurt', 'Ulm')
    print(path)
    print()
    return graph


'''======================= Global Variables ======================================='''
filename = 'graph_list.csv'

if __name__ == '__main__':

    graph = [['a', 'c', '8'], ['a', 'b', '7'], ['c', 'd', '8']]
    example_graph()
    #open_csv()
    #write_csv(graph)

    start(graph)


# https://www.annytab.com/a-star-search-algorithm-in-python/#:~:text=The%20goal%20of%20the%20A,the%20goal%20node%20(h).
# https://www-m9.ma.tum.de/graph-algorithms/directed-chinese-postman/index_en.html