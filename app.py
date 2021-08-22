import json
import pickle

from flask import Flask, render_template, request
from utils.input_processor import process_input

SAVED_MODEL_PATH = "model.pkl"

regressor = pickle.load(open(SAVED_MODEL_PATH, "rb"))

app = Flask(__name__)

@app.route('/')
def home() -> str:
    """
    Homepage for this API.
    :return: Basic info about the API
    """
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict() -> str:
    """
    Creates route for model prediction for given number of inputs.
    :return: predicted price
    """
    try:
        input_params = process_input(request.data)
        print(input_params)
        predictions = regressor.predict(input_params)

        return json.dumps({"predicted_price": predictions.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500
