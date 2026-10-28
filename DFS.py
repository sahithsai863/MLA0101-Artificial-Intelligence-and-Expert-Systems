def dfs_cave_exploration(cave_map, current_junction, visited=None):
    if visited is None:
        visited = []

    visited.append(current_junction)
    print(f"Drone enters: {current_junction}")

    for next_junction in cave_map.get(current_junction, []):
        if next_junction not in visited:
            print(f" -> Moving deeper from {current_junction} to {next_junction}")
            dfs_cave_exploration(cave_map, next_junction, visited)
            print(f" <- Dead end / Explored. Backtracking to: {current_junction}")

    return visited

if __name__ == "__main__":
    cave_map = {
        'Entrance': ['Chamber_A', 'Chamber_B'],
        'Chamber_A': ['Deep_Cave_1', 'Deep_Cave_2'],
        'Deep_Cave_1': [],
        'Deep_Cave_2': [],
        'Chamber_B': ['Deep_Cave_3'],
        'Deep_Cave_3': []
    }

    print("--- Rescue Drone DFS Cave Exploration ---")
    exploration_order = dfs_cave_exploration(cave_map, 'Entrance')

    print("\n--- Final Summary ---")
    print(f"Complete path explored by the drone: {' -> '.join(exploration_order)}")
