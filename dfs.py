cost = 0


# Função para chamar algoritmo de busca em profundidade padrão (não foi usado)
def regular_DFS(graph, starting_point):
    path = regular_dfs_search(graph, starting_point)
    return path


# Algoritmo padrão de busca em profundidade
# Inicializa um vetor visited vazio, adiciona o nó do grafo que está sendo processado,
# e chama a função recursivamente para cada vizinho do nó que ainda não foi visitado.
def regular_dfs_search(graph, point, visited=[]):
    visited.append(point)
    adjacent_nodes = graph.get(point)
    for node, weight in adjacent_nodes.items():
        if node not in visited:
            regular_dfs_search(graph, node, visited)
    return visited
    

# Função para chamar algoritmo de busca em profundidade com o nó destino
def targetet_DFS(graph, start_point, ending_point):
    global cost
    cost = 0
    path = targeted_dfs_search(graph, start_point, ending_point, visited = [])
    return path, cost


# Função parecida com o dfs normal com uma comparação adicional, para verificar se o nó que está sendo processado
# é o nó destino, e também calcula o custo do caminho do nó inicial até o nó final.
def targeted_dfs_search(graph, point, ending_point, visited):
    global cost
    visited.append(point)
    if (point == ending_point):
        return visited

    adjacent_nodes = graph.get(point)

    for node, weight in adjacent_nodes.items():
        if node not in visited:
            cost += int(weight)
            path = targeted_dfs_search(graph, node, ending_point, visited)
            if path:
                return path

    return None
