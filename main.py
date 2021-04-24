import csv
from a_star import astar_search
from graph import Graph


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
    graph.connect('Frankfurt', 'Mannheim', 85)
    graph.connect('Wurzburg', 'Nurnberg', 104)
    graph.connect('Wurzburg', 'Stuttgart', 140)
    graph.connect('Wurzburg', 'Ulm', 183)
    graph.connect('Mannheim', 'Nurnberg', 230)
    graph.connect('Mannheim', 'Karlsruhe', 67)
    graph.connect('Karlsruhe', 'Basel', 191)
    graph.connect('Karlsruhe', 'Stuttgart', 64)
    graph.connect('Nurnberg', 'Ulm', 171)
    graph.connect('Nurnberg', 'Munchen', 170)
    graph.connect('Nurnberg', 'Passau', 220)
    graph.connect('Stuttgart', 'Ulm', 107)
    graph.connect('Basel', 'Bern', 91)
    graph.connect('Basel', 'Zurich', 85)
    graph.connect('Bern', 'Zurich', 120)
    graph.connect('Zurich', 'Memmingen', 184)
    graph.connect('Memmingen', 'Ulm', 55)
    graph.connect('Memmingen', 'Munchen', 115)
    graph.connect('Munchen', 'Ulm', 123)
    graph.connect('Munchen', 'Passau', 189)
    graph.connect('Munchen', 'Rosenheim', 59)
    graph.connect('Rosenheim', 'Salzburg', 81)
    graph.connect('Passau', 'Linz', 102)
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
'''======================= Global Variables ======================================='''
filename = 'graph_list.csv'

if __name__ == '__main__':

    graph = [['a', 'c', '8'], ['a', 'b', '7'], ['c', 'd', '8']]
    example_graph()
    #open_csv()
    #write_csv(graph)


# https://www.annytab.com/a-star-search-algorithm-in-python/#:~:text=The%20goal%20of%20the%20A,the%20goal%20node%20(h).
# https://www-m9.ma.tum.de/graph-algorithms/directed-chinese-postman/index_en.html