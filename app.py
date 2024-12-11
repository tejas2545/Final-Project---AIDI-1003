from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load("random_forest_model.pkl")  # Ensure this file exists in the same directory

# Initialize Flask app
app = Flask(__name__)

# Root endpoint for basic connectivity check
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the ML Model Prediction API! Use POST on /predict to get predictions."

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Ensure the "features" key is present in the JSON
        if "features" not in data:
            return jsonify({"error": "Missing 'features' key in JSON data"}), 400

        # Extract features and reshape for model input
        features = np.array(data['features']).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Return prediction as JSON
        response = {
            "prediction": prediction.tolist()
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
