class Node:
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0  # distancia g(n)
        self.h = 0  # heuristica h(n)
        self.f = 0  # Custo total f(n) = g(n) + h(n)
        self.coordinates = 0  # tupla de coordenadas

    # Compara nós, usando uma função built-in do python
    def __eq__(self, other):
        return self.name == other.name

    # Compara maior nó, usando uma função built-in do python
    def __lt__(self, other):
         return self.f < other.f
