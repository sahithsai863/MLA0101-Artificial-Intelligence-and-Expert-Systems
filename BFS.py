from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set([start])
    
    queue = deque([(start, [start])])
    
    while queue:
        current_room, path = queue.popleft()
        
        if current_room == goal:
            return path
        
        for neighbor in graph.get(current_room, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None

if __name__ == "__main__":
    building_graph = {
        'Room_A': ['Room_B', 'Room_C'],
        'Room_B': ['Room_A', 'Room_D', 'Room_E'],
        'Room_C': ['Room_A', 'Room_F'],
        'Room_D': ['Room_B'],
        'Room_E': ['Room_B', 'Room_F'],
        'Room_F': ['Room_C', 'Room_E']
    }
    
    start_room = 'Room_A'
    end_room = 'Room_F'
    
    print(f"--- Robot BFS Shortest Route Finder ---")
    shortest_route = bfs_shortest_path(building_graph, start_room, end_room);
    
    if shortest_route:
        print(f"Shortest route from {start_room} to {end_room}: {' -> '.join(shortest_route)}")
        print(f"Total steps (edges): {len(shortest_route) - 1}")
    else:
        print(f"No path found between {start_room} and {end_room}")
        
