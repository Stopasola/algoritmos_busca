from node import Node


def astar_search(graph, coordinates, start, end):
    open = []
    closed = []

    # Cria os nodes, e atribui as coordenadas consultando um dict específico
    start_node = Node(start, None)
    start_node.coordinates = coordinates[start]
    goal_node = Node(end, None)
    goal_node.coordinates = coordinates[end]
    # Adiciona a lista o node inicial
    open.append(start_node)

    # Percorre até a lista ficar vazia, com todos os nós em closed
    while len(open) > 0:
        open.sort()
        current_node = open.pop(0)  # Pega o nó com menor custo
        closed.append(current_node)  # Adiciona a lista percorrida
        # Verifica se chegou no nó final
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(int(current_node.g))
                current_node = current_node.parent
            path.append(int(start_node.g))
            # retorna o custo final
            return path[0]
        # Busca os vizinhos com a função get implementada no file graph
        neighbors = graph.get(current_node.name)
        for key, value in neighbors.items():
            neighbor = Node(key, current_node)
            neighbor.coordinates = coordinates[key]
            # Se o nó vizinho atual está na lista closed, não calcula o peso
            if neighbor in closed:
                continue
            # Calcula o peso, para encontrar a heuristica h(h), usamos o calculo de manhattan
            neighbor.g = current_node.g + int(graph.get(current_node.name, neighbor.name))
            neighbor.h = manhattan_distance(neighbor, goal_node)
            neighbor.f = neighbor.g + neighbor.h

            # Verifico se o vizinho ainda está na lista open, caso esteja ele é adicionado, por meio da função chamada
            if add_to_open(open, neighbor):
                open.append(neighbor)
    return None


# calculo da distância de manhattan
def manhattan_distance(neighbor, goal_node):
    return abs(neighbor.coordinates[0] - goal_node.coordinates[0]) + abs(neighbor.coordinates[1] - goal_node.coordinates[1])


def add_to_open(open, neighbor):
    for node in open:
        if neighbor == node and neighbor.f > node.f:
            return False
    return True