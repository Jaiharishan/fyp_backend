import random

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def total_distance(tour, cities):
    """Calculate the total distance of a tour."""
    distance = 0
    num_cities = len(tour)
    for i in range(num_cities):
        distance += euclidean_distance(cities[tour[i]], cities[tour[(i + 1) % num_cities]])
    return distance

def generate_initial_solution(num_cities):
    """Generate an initial solution randomly."""
    return random.sample(range(num_cities), num_cities)

def two_opt(tour, cities):
    """Apply 2-opt heuristic to improve the tour."""
    improved = True
    while improved:
        improved = False
        for i in range(len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) + euclidean_distance(
                        cities[tour[j]], cities[tour[(j + 1) % len(tour)]]) > \
                        euclidean_distance(cities[tour[i]], cities[tour[j]]) + euclidean_distance(
                    cities[tour[i + 1]], cities[tour[(j + 1) % len(tour)]]):
                    tour[i + 1:j + 1] = tour[j:i:-1]
                    improved = True
    return tour

def tsp_local_search(cities):
    """Solve the TSP using local search."""
    num_cities = len(cities)
    # Generate initial solution
    current_tour = generate_initial_solution(num_cities)
    current_distance = total_distance(current_tour, cities)
    # Apply 2-opt heuristic to improve the initial solution
    improved_tour = two_opt(current_tour, cities)
    improved_distance = total_distance(improved_tour, cities)
    while improved_distance < current_distance:
        current_tour = improved_tour
        current_distance = improved_distance
        improved_tour = two_opt(current_tour, cities)
        improved_distance = total_distance(improved_tour, cities)
    return improved_tour, improved_distance



def local_search(cities):
    optimal_tour, optimal_distance = tsp_local_search(cities)

    return optimal_tour, optimal_distance
