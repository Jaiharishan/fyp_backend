import elkai

def lkh(weight_matrix):
    cities = elkai.DistanceMatrix(weight_matrix)
    permutation_LKH = cities.solve_tsp()
    return permutation_LKH