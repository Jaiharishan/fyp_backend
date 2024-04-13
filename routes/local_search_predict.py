from flask import Flask, request, jsonify
import pandas as pd
import os, numpy as np, csv

#IMPORT MODELS
from models.local_search import local_search

# IMPORT HELPERS

def local_search_predict():
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

        
        permutation, distance = local_search(coordinates)
        
        # Return the predictions
        return jsonify({'Permutation': permutation, 'Distance': distance})


    except Exception as e:
        return jsonify({'error': str(e)})