from collections import deque

# Initial and goal states
initial = "123456780"
goal = "123708456"


# Find the possible moves for the empty space (0)
def get_neighbors(state):
    neighbors = []

    # Position of 0
    zero_position = state.index("0")

    # Board position
    row = zero_position // 3
    col = zero_position % 3

    # Possible directions: Up, Down, Left, Right
    directions = [
        (-1, 0, "UP"),
        (1, 0, "DOWN"),
        (0, -1, "LEFT"),
        (0, 1, "RIGHT")
    ]

    for dr, dc, move in directions:
        new_row = row + dr
        new_col = col + dc

        # Check whether the new position is inside the board
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_position = new_row * 3 + new_col

            # Convert string to list so we can swap
            new_state = list(state)

            # Swap 0 with the neighboring tile
            new_state[zero_position], new_state[new_position] = \
                new_state[new_position], new_state[zero_position]

            new_state = "".join(new_state)

            neighbors.append((new_state, move))

    return neighbors


# BFS algorithm
def solve(initial, goal):

    # Queue contains:
    # (current state, path of states, path of moves)
    queue = deque()

    queue.append((initial, [initial], []))

    # Keep track of already visited states
    visited = set()
    visited.add(initial)

    while queue:

        current, path, moves = queue.popleft()

        # Goal reached
        if current == goal:
            return path, moves

        # Generate next states
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


# Solve the puzzle
path, moves = solve(initial, goal)


# Display solution
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
