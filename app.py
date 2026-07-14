import os
import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 🚀 SENIOR PRACTICE: Load the model ONCE globally when the server starts, not on every request.
MODEL_PATH = "model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Critical Error: '{MODEL_PATH}' not found. Please ensure your trained model file is in the root directory.")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 🤝 MATCHING THE UI: Parse incoming modern JSON data payload
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request. Missing JSON payload.'}), 400

        # Extract features safely, parsing to float/int to prevent unexpected model type issues
        features_list = [
            float(data.get('fixed_acidity', 0)),
            float(data.get('volatile_acidity', 0)),
            float(data.get('citric_acid', 0)),
            float(data.get('residual_sugar', 0)),
            float(data.get('chlorides', 0)),
            int(data.get('freesulfurdioxide', 0)),
            int(data.get('totalsulfurdioxide', 0)),
            float(data.get('density', 0)),
            float(data.get('ph', 0)),
            float(data.get('sulphates', 0)),
            float(data.get('alcohol', 0))
        ]

        # Prepare payload format for the model array shape: [[x1, x2, ...]]
        features = np.array(features_list).reshape(1, -1)
        
        # Execute ML prediction execution
        prediction = model.predict(features)

        # Map prediction logic outcome
        # (Note: In your comments you mentioned a regression model, but your evaluation logic 
        # is looking for a binary classification 1 or 0. This logic handles classification cleanly.)
        if int(prediction[0]) == 1:
            result_text = 'Good Quality Wine'
        else:
            result_text = 'Bad Quality Wine'

        #  MATCHING THE UI: Return a clean JSON object back to the JavaScript fetch API
        return jsonify({'result': result_text})

    except KeyError as ke:
        return jsonify({'error': f'Missing required field parameter: {str(ke)}'}), 400
    except Exception as e:
        # Catch errors gracefully and return structured JSON log status
        return jsonify({'error': f'Internal Prediction engine error: {str(e)}'}), 500

if __name__ == '__main__':
    # Toggle debug=False in highly restricted live production environments
    app.run(debug=True)