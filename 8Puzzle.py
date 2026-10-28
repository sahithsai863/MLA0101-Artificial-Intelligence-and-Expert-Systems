from collections import deque
initial = "123456780"
goal = "123708456"

def get_neighbors(state):
    neighbors = []

    zero_position = state.index("0")

    row = zero_position // 3
    col = zero_position % 3

    directions = [
        (-1, 0, "UP"),
        (1, 0, "DOWN"),
        (0, -1, "LEFT"),
        (0, 1, "RIGHT")
    ]

    for dr, dc, move in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_position = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero_position], new_state[new_position] = \
                new_state[new_position], new_state[zero_position]

            new_state = "".join(new_state)

            neighbors.append((new_state, move))

    return neighbors

def solve(initial, goal):

    queue = deque()

    queue.append((initial, [initial], []))

    visited = set()
    visited.add(initial)

    while queue:

        current, path, moves = queue.popleft()
        if current == goal:
            return path, moves
        for next_state, move in get_neighbors(current):

            if next_state not in visited:

                visited.add(next_state)

                queue.append(
                    (
                        next_state,
                        path + [next_state],
                        moves + [move]
                    )
                )

    return None, None
path, moves = solve(initial, goal)


if path:

    print("Initial State:")
    print()

    for i in range(3):
        print(path[0][i * 3:(i + 1) * 3])

    print("\nSolution:\n")

    for i in range(1, len(path)):

        print("Move:", moves[i - 1])

        state = path[i]

        for j in range(3):
            print(state[j * 3:(j + 1) * 3])

        print()

    print("Goal reached!")
    print("Total moves:", len(moves))

else:
    print("No solution exists.")
