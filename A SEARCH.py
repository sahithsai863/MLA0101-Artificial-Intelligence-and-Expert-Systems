import heapq
graph = {
    "Warehouse": [("Junction 1", 3), ("Junction 2", 5)],
    "Junction 1": [("Customer Area", 4)],
    "Junction 2": [("Traffic Signal", 2)],
    "Traffic Signal": [("Customer Area", 3)],
    "Customer Area": [("Delivery Destination", 2)],
    "Delivery Destination": []
}
heuristic = {
    "Warehouse": 8,
    "Junction 1": 5,
    "Junction 2": 4,
    "Traffic Signal": 2,
    "Customer Area": 1,
    "Delivery Destination": 0
}
def a_star(start, goal):
    priority_queue = [(heuristic[start], 0, start)]
    visited = set()
    print("Delivery Robot Path:")
    while priority_queue:
        f, g, location = heapq.heappop(priority_queue)
        if location in visited:
            continue
        print(location, end=" -> ")
        if location == goal:
            print("Delivered")
            print("Total Travel Cost =", g)
            return
        visited.add(location)
        for neighbor, cost in graph[location]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(priority_queue, (new_f, new_g, neighbor))
a_star("Warehouse", "Delivery Destination")
