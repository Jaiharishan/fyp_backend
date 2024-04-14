import numpy as np
import sys

def tsp_branch_and_bound(distances):
    num_nodes = len(distances)
    
    # Initialize variables
    tour = [0]
    min_cost = sys.maxsize
    visited = [False] * num_nodes
    visited[0] = True
    
    # Define recursive function for branch and bound
    def branch_and_bound(curr_node, curr_cost, depth, path):
        nonlocal min_cost, tour
        
        # If all nodes visited, check if it forms a better tour
        if depth == num_nodes - 1:
            if distances[curr_node][0] < min_cost:
                min_cost = distances[curr_node][0]
                tour = path + [0]
            return

        # Branching
        for next_node in range(num_nodes):
            if not visited[next_node]:
                # Prune if cost is already higher than the current min_cost
                if curr_cost + distances[curr_node][next_node] >= min_cost:
                    continue
                
                visited[next_node] = True
                branch_and_bound(next_node, curr_cost + distances[curr_node][next_node], depth + 1, path + [next_node])
                visited[next_node] = False
                
    # Start branch and bound from node 0
    branch_and_bound(0, 0, 0, [0])
    
    return tour, min_cost


# branch and bound function
def branch_and_bound(weight_matrix):
    tour, min_cost = tsp_branch_and_bound(weight_matrix)
    return tour, min_cost
