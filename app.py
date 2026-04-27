from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Traffic Signal Model Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    features = np.array([[data['traffic_volume'], data['avg_speed'], data['hour']]])
    
    prediction = model.predict(features)
    
    return jsonify({"green_time": float(prediction[0])})

if __name__ == "__main__":
    app.run()