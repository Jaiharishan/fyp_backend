import numpy as np

def calculate_tsp_distance(city_coordinates, tour):
        total_distance = 0
        num_cities = len(tour)
        for i in range(num_cities):
            total_distance += np.linalg.norm(city_coordinates[tour[i]] - city_coordinates[tour[(i + 1) % num_cities]])

        return total_distance