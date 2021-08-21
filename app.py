import json
import pickle

import numpy as np
from flask import Flask, request, render_template


SAVED_MODEL_PATH = "model.pkl"

regressor = pickle.load(open(SAVED_MODEL_PATH, "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

def __process_input(request_data: str) -> np.array:
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    assert len(parsed_body.shape) == 2, "'inputs' must be a 2-d array"
    return parsed_body

@app.route("/predict", methods=["POST"])
def predict() -> str:
    try:
        input_params = __process_input(request.data)
        print(input_params)
        predictions = regressor.predict(input_params)

        return json.dumps({"predicted_price": predictions.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500
