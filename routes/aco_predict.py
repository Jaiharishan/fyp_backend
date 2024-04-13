from flask import Flask, request, jsonify
import pandas as pd
import os, numpy as np, csv

#IMPORT MODELS
from models.ant_colony_optimization import ACO

# IMPORT HELPERS
from helpers.create_weight_matrix import create_weight_matrix


def aco_predict():
    # Check if a file is provided in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})

    file = request.files['file']

    # Check if the file has a CSV extension
    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'Invalid file format. Please provide a CSV file'})

    try:
        # Save the file temporarily
        file.save(os.path.join(os.getcwd() , 'dataset.csv')) # Then save the file
        file_path = 'dataset.csv'

        
        # Process the CSV file
        # Initialize an empty list to store coordinates
        coordinates = []

        # Open the CSV file in read mode
        with open('dataset.csv', mode='r') as file:
            reader = csv.reader(file)
            
            # Skip the header row
            next(reader)
            
            # Read each row and store coordinates in the list
            for row in reader:
                x, y = map(int, row)
                coordinates.append([x, y])

                
        coordinates = np.array(coordinates)

        weight_matrix = create_weight_matrix(coordinates)

        # print(weight_matrix)

        # Create an ACO object
        aco = ACO(weight_matrix, num_ants=10, num_iterations=100, alpha=1, beta=1)

        # Solve the problem
        best_tour, best_distance = aco.solve()

        # Return the predictions
        return jsonify({'Permutation': best_tour, 'Distance': best_distance})

    except Exception as e:
        return jsonify({'error': str(e)})