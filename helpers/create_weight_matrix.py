import numpy as np

def create_weight_matrix(node_coords):
    def euclidean_distance(point1, point2):
        """
        Calculates the Euclidean distance between two points.

        Args:
            point1: A numpy array representing the first point.
            point2: A numpy array representing the second point.

        Returns:
            The Euclidean distance between the two points.
        """
        return np.linalg.norm(point1 - point2)

    # Initialize the weight matrix
    weight_matrix = np.zeros((len(node_coords), len(node_coords)))

    # Calculate the Euclidean distance between each pair of points
    for i in range(len(node_coords)):
        for j in range(len(node_coords)):
            weight_matrix[i, j] = euclidean_distance(node_coords[i], node_coords[j])

    weight_matrix = np.array(weight_matrix)

    return weight_matrix