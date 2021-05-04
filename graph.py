class Graph:
    # Construtor
    def __init__(self, graph_dict=None):
        self.graph_dict = graph_dict or {}

    # Cria a conexão entre dois nós, com o valor de distância
    def connect(self, A, B, distance):
        self.graph_dict.setdefault(A, {})[B] = distance

    # Função recursiva para buscar nós vizinhos
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Retorna um dicionário com a estrutura do grafo
    def structure(self):
        return self.graph_dict
