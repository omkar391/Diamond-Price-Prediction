from flask import Flask, render_template, request
import numpy as np
import joblib
import pandas as pd
import os
import warnings

# Suppress scikit-learn warnings
warnings.filterwarnings('ignore', category=UserWarning)

app = Flask(__name__)

# Load trained model with memory optimization
try:
    model = joblib.load('model.pkl')
    features = list(model.feature_names_in_)
    print(f"Model loaded successfully with {len(features)} features")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    features = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if model is loaded
        if model is None:
            return render_template('result.html', prediction="Error: Model not loaded")
        
        # Get input data from form
        carat = float(request.form['carat'])
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])

        # Convert categorical to numerical (same mapping as training)
        cut_map = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
        color_map = {'D': 1, 'E': 2, 'F': 3, 'G': 4, 'H': 5, 'I': 6, 'J': 7}
        clarity_map = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}

        cut = cut_map.get(cut, 0)
        color = color_map.get(color, 0)
        clarity = clarity_map.get(clarity, 0)

        # Create input array directly (more memory efficient than DataFrame)
        input_data = np.array([[carat, cut, color, clarity, depth, table, x, y, z]])

        # Predict
        prediction = model.predict(input_data)

        # Extract float value from numpy array
        prediction_value = float(prediction[0])
        prediction_value = round(prediction_value, 2)

        return render_template('result.html', prediction=prediction_value)

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
