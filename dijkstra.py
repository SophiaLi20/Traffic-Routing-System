import heapq

def dijkstra(graph, start_node):
    min_heap = [(0, start_node)]
    distances = {node: float('inf') for node in graph.get_nodes()}
    distances[start_node] = 0

    while min_heap:
        current_dist, current_node = heapq.heappop(min_heap)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph.get_neighbors(current_node):
            new_dist = current_dist + weight
            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return distances
