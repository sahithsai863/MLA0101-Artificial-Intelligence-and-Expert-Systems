from collections import deque

def water_jug_bfs(capacity1, capacity2, goal):

    visited = set()
    queue = deque()

    queue.append(((0, 0), []))

    while queue:

        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == goal or b == goal:
            return path

        next_states = []
        # Fill Jug A
        next_states.append((capacity1, b))
        # Fill Jug B
        next_states.append((a, capacity2))
        # Empty Jug A
        next_states.append((0, b))
        # Empty Jug B
        next_states.append((a, 0))
        # Pour A -> B
        transfer = min(a, capacity2 - b)
        next_states.append((a - transfer, b + transfer))
        # Pour B -> A
        transfer = min(b, capacity1 - a)
        next_states.append((a + transfer, b - transfer))
        for state in next_states:
            if state not in visited:
                queue.append((state, path))
    return None
capacity1 = 4
capacity2 = 3
goal = 2

solution = water_jug_bfs(capacity1, capacity2, goal)

if solution:
    print("Sequence of Operations:")
    for state in solution:
        print(state)
else:
    print("No Solution Exists")
