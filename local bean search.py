
import random

# Distance matrix between cities
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = len(distance)
K = 3
MAX_ITERATIONS = 100

# Calculate total tour distance
def calculate_cost(path):
    cost = 0

    for i in range(len(path)):
        cost += distance[path[i]][path[(i + 1) % cities]]

    return cost


# Generate neighboring routes by swapping cities
def get_neighbors(path):
    neighbors = []

    for i in range(cities):
        for j in range(i + 1, cities):
            new_path = path.copy()

            new_path[i], new_path[j] = (
                new_path[j], new_path[i]
            )

            neighbors.append(new_path)

    return neighbors


# Local Beam Search Algorithm
def local_beam_search():
    beam = []

    # Generate K random initial routes
    for _ in range(K):
        path = list(range(cities))
        random.shuffle(path)
        beam.append(path)

    for iteration in range(MAX_ITERATIONS):

        candidates = []

        # Generate successors of all current routes
        for path in beam:
            candidates.extend(get_neighbors(path))

        # Sort routes according to their cost
        candidates.sort(key=calculate_cost)

        # Keep the best K routes
        beam = candidates[:K]

    best_path = min(beam, key=calculate_cost)

    return best_path, calculate_cost(best_path)


# Execute algorithm
best_path, best_cost = local_beam_search()

print("Traveling Salesman Problem")
print("Best Route:")

for city in best_path:
    print(chr(65 + city), end=" -> ")

print(chr(65 + best_path[0]))

print("Minimum Distance:", best_cost)
