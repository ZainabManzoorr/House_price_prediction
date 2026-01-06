import pickle
from flask import Flask,request,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
#load the model
model = pickle.load(open('elasticnet_model.pkl','rb'))
# app.py
from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

# -----------------------------
# Initialize Flask app
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Load the trained ML model
# -----------------------------
with open("elasticnet_model.pkl", "rb") as f:
    model = pickle.load(f)

# -----------------------------
# Expected feature order
# -----------------------------
expected_features = [
    'CRIM','ZN','INDUS','CHAS','NOX','RM','AGE',
    'DIS','RAD','TAX','PTRATIO','B','LSTAT'
]

# -----------------------------
# Routes
# -----------------------------

# Home page (optional)
@app.route('/')
def home():
    return render_template('home.html')  # You can create a simple HTML form here

# API endpoint for predictions
@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        # Parse JSON input
        data = request.get_json()['data']
        
        # Validate input
        missing_features = [f for f in expected_features if f not in data]
        if missing_features:
            return jsonify({"error": f"Missing features: {missing_features}"}), 400
        
        # Ensure correct feature order and reshape for prediction
        feature_array = np.array([data[f] for f in expected_features]).reshape(1, -1)
        
        # Predict using the loaded model
        prediction = model.predict(feature_array)
        
        # Return prediction as a Python float (JSON-safe)
        return jsonify({"prediction": float(prediction[0])})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# Run the app
# -----------------------------
if __name__ == "__main__":
    # Debug=True is only for development. Turn off in production!
    app.run(debug=True)

    


