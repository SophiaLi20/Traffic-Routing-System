class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest, weight):
        if src not in self.adj_list:
            self.adj_list[src] = []
        self.adj_list[src].append((dest, weight))

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])

    def get_nodes(self):
        return self.adj_list.keys()
