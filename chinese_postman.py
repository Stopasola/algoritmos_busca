from a_star import astar_search
from dfs import targetet_DFS


# carrega a estrutura do grafo em um dicionário, e busca todos os nós com um numero impar de arestas
def odd_nodes(graph):
    odd_list = []
    graph_structure = graph.structure()

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

    return odd_list


# calcula todas as opções de pares possiveis com os nós presentes no grafo
def possible_pairings(odd_list):
    pairs = []
    for i in range(len(odd_list)-1):
        pairs.append([])
        for j in range(i+1, len(odd_list)):
            pairs[i].append([odd_list[i], odd_list[j]])
    return pairs


# Faz as combinações com os pairs já calculados
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


# calcula as distancias entre os conjuntos de pairs usando o astar
def calculate_pairings_astar(pairings_sum, graph, coordinates):
    min_sums = []
    paths = []
    aux_i = 0
    for i in pairings_sum:
        s = 0
        paths.append([])
        for j in range(len(i)):
            cost = astar_search(graph, coordinates, i[j][0], i[j][1])
            print('Custo: ', i[j][0], 'de: ', i[j][1], 'para:', cost)
            paths[aux_i].append([i[j][0], i[j][1], cost])
            s += cost
        min_sums.append(s)
        aux_i += 1
    return paths, min_sums


# calcula as distancias entre os conjuntos de pairs usando o dfs
def calculate_pairings_dfs(pairings_sum, graph):
    min_sums = []
    paths = []
    aux_i = 0
    for i in pairings_sum:
        s = 0
        paths.append([])
        for j in range(len(i)):
            path, cost = targetet_DFS(graph, i[j][0], i[j][1])
            paths[aux_i].append([i[j][0], i[j][1], cost])
            print('Custo: ', i[j][0], 'de: ', i[j][1], 'para:', cost)
            s += cost
        min_sums.append(s)
        aux_i += 1

    return paths, min_sums


# calcula as distancias entre os conjuntos de pairs usando o AG
def calculate_pairings_genetic(pairings_sum, graph):
    min_sums = []
    paths = []
    aux_i = 0
    for i in pairings_sum:
        s = 0
        paths.append([])
        for j in range(len(i)):
            path, cost = targetet_genetic(graph, i[j][0], i[j][1])
            paths[aux_i].append([i[j][0], i[j][1], cost])
            #print('Custo: ', i[j][0], 'de: ', i[j][1], 'para:', cost)
            s += cost
        min_sums.append(s)
        aux_i += 1

    return paths, min_sums


# busca o menor valor dos pares encontrados
def add_edges(min_sums):
    min_value = min(min_sums)
    return min_value


# calcula distancia total com o valor miniomo encontrado no pairing
def calculate_total_distance(graph, min_value):
    total_cost = 0
    for edges in graph.structure().values():
        for j, value in edges.items():
            total_cost += int(value)

    print('Custo total:', total_cost + min_value)
    return total_cost + min_value


'''======================= Global Variables ======================================='''
l = 0
pairings_sum = []


def start(graph, coordinates):
    global l
    odd_list = odd_nodes(graph)
    pairs = possible_pairings(odd_list)
    # numero de pairs usados, foi declarado aqui, uma vez que usamos recurssão na função que calcular os conjuntos de pairings
    l = (len(pairs)+1)//2

    get_pairs(pairs)

    # Calculo A*
    print('Busca A*')
    paths, min_sums = calculate_pairings_astar(pairings_sum, graph, coordinates)
    min_value = add_edges(min_sums)
    calculate_total_distance(graph, min_value)

    # Calculo Bfs
    print('Busca em profundidade')
    paths, min_sums = calculate_pairings_dfs(pairings_sum, graph)
    min_value = add_edges(min_sums)
    calculate_total_distance(graph, min_value)
