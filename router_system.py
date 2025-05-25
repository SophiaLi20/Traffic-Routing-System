from graph import graph
from dijkstra import dijkstra

class TrafficRouterSystem:
    def __init__(self):
        self.graph = graph()

    def load_map_data(self):
        # Hardcoded or load from JSON
        self.graph.add_edge(1, 2, 2)
        self.graph.add_edge(1, 3, 4)
        self.graph.add_edge(2, 4, 7)
        self.graph.add_edge(3, 4, 1)
        self.graph.add_edge(4, 5, 3)

    def find_shortest_paths(self, source):
        return dijkstra.shortest_path(self.graph, source)
