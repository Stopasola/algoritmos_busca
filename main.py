import csv
from graph import Graph
from chinese_postman import start


def open_graph_csv():
    reading_list = list()
    aux_list = list()
    with open(graph_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row:
                aux_list.append(row)
            else:
                reading_list.append(aux_list[:])
                aux_list.clear()

    return reading_list[0]


def open_coordinates_csv():
    reading_list = {}
    with open(coordinates_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row:
                reading_list[row[0]] = (int(row[1]), int(row[2]))
    return reading_list


def write_csv(graph):

    with open(graph_filename, mode='a') as graph_file:
        employee_writer = csv.writer(graph_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for g in graph:
            employee_writer.writerow(g)
        employee_writer.writerow([])


def load_graph(graph_list):
    graph = Graph()
    for connection in graph_list:
        graph.connect(connection[0], connection[1], connection[2])
    return graph


'''======================= Global Variables ======================================='''
graph_filename = 'graph_list.csv'
coordinates_filename = 'coordinates.csv'

if __name__ == '__main__':

    graph_list = open_graph_csv()  # Lê arquivo com todas as conexões do grafo em questão
    coordinates = open_coordinates_csv()  # Lẽ arquivo com as coordenadas de latitude e longitude reais e aproximadas de todos as cidaes (nós)
    graph = load_graph(graph_list)  # Carrega em memória uma instancia do objeto grafo
    start(graph, coordinates)  # Inicia o problema do carteiro chines

