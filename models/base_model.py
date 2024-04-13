from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import os


def process_csv(file_path):
    # Read the CSV file into a Pandas DataFrame
    data = pd.read_csv(file_path)

    # Assume the CSV file has features in columns 1 to n-1 and target variable in the last column
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Preprocess the data (if necessary)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train a machine learning model
    model = LinearRegression()
    model.fit(X_scaled, y)

    # Make predictions
    predictions = model.predict(X_scaled)

    return predictions