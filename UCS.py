import heapq

def uniform_cost_search(graph, start, goal):

    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    visited = set()

    while priority_queue:

        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue,
                        (cost + edge_cost,
                         neighbor,
                         path + [neighbor])
                    )

    return None, float("inf")


graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 7), ('E', 3)],
    'C': [('A', 4), ('F', 5)],
    'D': [('B', 7)],
    'E': [('B', 3), ('F', 1)],
    'F': [('C', 5), ('E', 1)]
}

source = 'A'
destination = 'F'

path, cost = uniform_cost_search(graph, source, destination)

if path:
    print("Least Cost Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No Path Found")
