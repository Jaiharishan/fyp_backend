import random
import numpy as np

class ACO:
  def __init__(self, weight_matrix, num_ants, num_iterations, alpha, beta):
    self.weight_matrix = weight_matrix
    self.num_ants = num_ants
    self.num_iterations = num_iterations
    self.alpha = alpha
    self.beta = beta
    self.pheromone_matrix = np.ones((len(weight_matrix), len(weight_matrix)))
    self.best_tour = None
    self.best_distance = float('inf')

  def solve(self):
    for i in range(self.num_iterations):
      # Generate a list of tours
      tours = []
      for j in range(self.num_ants):
        tour = self.generate_tour()
        tours.append(tour)

      # Update the pheromone matrix
      self.update_pheromone_matrix(tours)

      # Find the best tour
      for tour in tours:
        distance = self.calculate_tour_distance(tour)
        if distance < self.best_distance:
          self.best_tour = tour
          self.best_distance = distance

    return self.best_tour, self.best_distance

  def generate_tour(self):
    tour = []
    visited = set()
    current_node = random.randint(0, len(self.weight_matrix) - 1)
    tour.append(current_node)
    visited.add(current_node)
    while len(visited) < len(self.weight_matrix):
      next_node = self.select_next_node(current_node, visited)
      tour.append(next_node)
      visited.add(next_node)
      current_node = next_node
    return tour

  def select_next_node(self, current_node, visited):
    unvisited_nodes = set(range(len(self.weight_matrix))) - visited
    probabilities = []
    for node in unvisited_nodes:
      pheromone = self.pheromone_matrix[current_node, node] ** self.alpha
      distance = self.weight_matrix[current_node, node] ** self.beta
      probability = pheromone * distance
      probabilities.append(probability)
    total_probability = sum(probabilities)
    probabilities = [p / total_probability for p in probabilities]
    return random.choices(list(unvisited_nodes), weights=probabilities)[0]

  def update_pheromone_matrix(self, tours):
    for tour in tours:
      for i in range(len(tour) - 1):
        current_node = tour[i]
        next_node = tour[i + 1]
        self.pheromone_matrix[current_node, next_node] += 1 / self.calculate_tour_distance(tour)

  def calculate_tour_distance(self, tour):
    distance = 0
    for i in range(len(tour) - 1):
      current_node = tour[i]
      next_node = tour[i + 1]
      distance += self.weight_matrix[current_node, next_node]
    return distance


# # Create an ACO object
# aco = ACO(weight_matrix, num_ants=10, num_iterations=100, alpha=1, beta=1)

# # Solve the problem
# best_tour, best_distance = aco.solve()