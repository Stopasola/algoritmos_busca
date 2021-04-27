cost = 0


def regular_DFS(graph, starting_point):
    path = regular_dfs_search(graph, starting_point)
    return path


def regular_dfs_search(graph, point, visited=[]):
    visited.append(point)
    adjacent_nodes = graph.get(point)
    for node, weight in adjacent_nodes.items():
        if node not in visited:
            regular_dfs_search(graph, node, visited)
    return visited
    


def targetet_DFS(graph, start_point, ending_point):
    path = targeted_dfs_search(graph, start_point, ending_point)
    return cost


def targeted_dfs_search(graph, point, ending_point, visited=[]):
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
