from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import os

# IMPORT ROUTES
from routes.base_predict import base_predict
from routes.aco_predict import aco_predict
from routes.lkh_predict import lkh_predict
from routes.local_search_predict import local_search_predict
from routes.hopfield_nn_predict import hopfield_nn_predict

# APP CONFIG
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static'

# TSP INPUT: CSV FILE (X, Y)
# TSP OUTPUT: BEST PATH (LIST), DISTANCE (INT)

# DEFINE ROUTES FOR THE API
app.add_url_rule('/predict', 'predict', base_predict, methods=["POST"])
app.add_url_rule('/aco_predict', 'aco_predict', aco_predict, methods=["POST"])
app.add_url_rule('/lkh_predict', 'lkh_predict', lkh_predict, methods=["POST"])
app.add_url_rule('/local_search_predict', 'local_search_predict',  local_search_predict, methods=["POST"])
app.add_url_rule('/hopfield_nn_predict', 'hopfield_nn_predict', hopfield_nn_predict, methods=["POST"])


if __name__ == '__main__':
    app.run(debug=True)
