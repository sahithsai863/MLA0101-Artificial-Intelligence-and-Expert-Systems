import heapq
graph = {
    "Robot Start": ["Rack A", "Rack B"],
    "Rack A": ["Rack C", "Rack D"],
    "Rack B": ["Rack E"],
    "Rack C": ["Target Rack"],
    "Rack D": [],
    "Rack E": ["Target Rack"],
    "Target Rack": []
}
heuristic = {
    "Robot Start": 8,
    "Rack A": 5,
    "Rack B": 6,
    "Rack C": 2,
    "Rack D": 4,
    "Rack E": 1,
    "Target Rack": 0
}
def greedy_best_first(start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    print("Robot Path:")
    while priority_queue:
        h, location = heapq.heappop(priority_queue)
        if location not in visited:
            print(location, end=" -> ")
            if location == goal:
                print("Reached")
                return
            visited.add(location)
            for neighbor in graph[location]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
greedy_best_first("Robot Start", "Target Rack")
