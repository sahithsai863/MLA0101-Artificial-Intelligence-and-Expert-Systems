import heapq
graph = {
    "Chennai": ["Vellore", "Pondicherry"],
    "Vellore": ["Bengaluru", "Salem"],
    "Pondicherry": ["Trichy"],
    "Salem": ["Madurai"],
    "Bengaluru": [],
    "Trichy": ["Madurai"],
    "Madurai": []
}
heuristic = {
    "Chennai": 460,
    "Vellore": 380,
    "Pondicherry": 300,
    "Salem": 210,
    "Bengaluru": 430,
    "Trichy": 130,
    "Madurai": 0
}
def best_first_search(start, goal):
    visited = set()
    priority_queue = []

    heapq.heappush(priority_queue, (heuristic[start], start))

    print("Path Traversed:")

    while priority_queue:
        h, city = heapq.heappop(priority_queue)

        if city not in visited:
            print(city, end=" ")

            if city == goal:
                print("\n\nDestination Reached!")
                return

            visited.add(city)

            for neighbour in graph[city]:
                if neighbour not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbour], neighbour))
best_first_search("Chennai", "Madurai")
