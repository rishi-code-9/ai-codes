
from collections import deque

# Grid: 0 = Free cell, 1 = Obstacle
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

# Possible movements: Up, Down, Left, Right
directions = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1)
]

# BFS Algorithm
def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        x, y = path[-1]

        # Check goal
        if (x, y) == goal:
            return path

        # Explore neighboring cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < 4 and
                0 <= ny < 4 and
                grid[nx][ny] == 0 and
                (nx, ny) not in visited):

                visited.add((nx, ny))
                queue.append(path + [(nx, ny)])

    return None


# Execute BFS
path = bfs(start, goal)

if path:
    print("Path Found!")
    print("Robot Path:")

    for position in path:
        print(position)

    print("Total Steps:", len(path) - 1)

else:
    print("No Path Found!")
