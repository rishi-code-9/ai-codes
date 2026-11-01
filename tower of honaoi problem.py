
from collections import deque

# Initial and Goal States
# Each tuple represents the position of disks 1, 2, 3
# 0 = Source, 1 = Auxiliary, 2 = Destination

start = (0, 0, 0)
goal = (2, 2, 2)

# Generate possible next states
def get_neighbors(state):
    neighbors = []

    pegs = [[], [], []]

    for disk, peg in enumerate(state):
        pegs[peg].append(disk)

    for i in range(3):
        if not pegs[i]:
            continue

        disk = min(pegs[i])

        for j in range(3):
            if i != j:
                if not pegs[j] or disk < min(pegs[j]):

                    new_state = list(state)
                    new_state[disk] = j

                    neighbors.append(tuple(new_state))

    return neighbors


# BFS State Space Search
def tower_of_hanoi():
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None


# Display Solution
solution = tower_of_hanoi()

if solution is not None:
    print("Tower of Hanoi Solution")
    print("Total Moves:", len(solution))

    for step, state in enumerate(solution, 1):
        print("\nStep", step)

        for disk, peg in enumerate(state):
            print("Disk", disk + 1, "-> Peg", peg)
else:
    print("No solution found")
