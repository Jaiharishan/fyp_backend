import numpy as np

class HopfieldTSP:
    def __init__(self, num_cities, city_distances):
        self.num_cities = num_cities
        self.city_distances = city_distances
        self.weights = np.zeros((num_cities, num_cities))

    def train(self):
        for i in range(self.num_cities):
            for j in range(i+1, self.num_cities):
                self.weights[i, j] = -self.city_distances[i, j]
                self.weights[j, i] = -self.city_distances[i, j]

    def energy(self, tour):
        total_distance = 0
        for i in range(self.num_cities):
            total_distance += self.city_distances[tour[i], tour[(i+1)%self.num_cities]]
        return total_distance

    def find_optimal_tour(self, initial_tour=None, max_iter=100):
        if initial_tour is None:
            tour = np.random.permutation(self.num_cities)
        else:
            tour = initial_tour

        for _ in range(max_iter):
            new_tour = np.copy(tour)
            for i in range(self.num_cities):
                energy_change = np.dot(self.weights[i], tour)
                if energy_change < 0:
                    new_tour[i] = 1 - tour[i]  # Flip the state
            if np.array_equal(new_tour, tour):
                break
            tour = new_tour

        return tour

# Function to calculate total distance of TSP tour
def calculate_tsp_distance(city_coordinates, tour):
    total_distance = 0
    num_cities = len(tour)
    for i in range(num_cities):
        total_distance += np.linalg.norm(city_coordinates[tour[i]] - city_coordinates[tour[(i + 1) % num_cities]])
    return total_distance



# Create and train HopfieldTSP network (using city distances as given)
def hopfield_nn(num_cities, city_distances, city_coordinates):
    
    hopfield_tsp = HopfieldTSP(num_cities, city_distances)
    hopfield_tsp.train()

    # Find optimal tour
    optimal_tour = hopfield_tsp.find_optimal_tour()

    # Calculate the optimal distance
    optimal_distance = calculate_tsp_distance(city_coordinates, optimal_tour)

    return optimal_tour, optimal_distance

