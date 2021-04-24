class Node:
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        print('meu cu1')
        return self.name == other.name
    # Sort nodes
    def __lt__(self, other):
         print('meu cu2')
         return self.f < other.f
    # Print node
    def __repr__(self):
        print('meu cu3')
        return ('({0},{1})'.format(self.name, self.f))