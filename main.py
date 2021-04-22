import csv
import cv2

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


filename = 'graph_list.csv'

if __name__ == '__main__':

    graph = [['a', 'c', '8'], ['a', 'b', '7'], ['c', 'd', '8']]

    open_csv()
    write_csv(graph)
