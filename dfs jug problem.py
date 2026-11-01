
# Water Jug Problem using DFS

jug1 = 4
jug2 = 3
target = 2

visited = set()

def dfs(x, y, path):

    # Check goal state
    if x == target or y == target:
        path.append((x, y))
        return True

    # Avoid repeated states
    if (x, y) in visited:
        return False

    visited.add((x, y))
    path.append((x, y))

    # Generate all possible operations
    next_states = [
        (jug1, y),  # Fill Jug 1
        (x, jug2),  # Fill Jug 2
        (0, y),     # Empty Jug 1
        (x, 0),     # Empty Jug 2
        (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour Jug 1 to Jug 2
        (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour Jug 2 to Jug 1
    ]

    # Explore states using DFS
    for state in next_states:
        if state not in visited:
            if dfs(state[0], state[1], path):
                return True

    path.pop()
    return False


# Execute DFS
path = []

if dfs(0, 0, path):
    print("Solution Found!")
    print("Steps:")

    for step, state in enumerate(path):
        print("Step", step, ":", state)

    print("Goal Achieved!")
else:
    print("No Solution Found!")
