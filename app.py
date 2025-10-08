from flask import Flask, render_template, request
import numpy as np
import os
import warnings

# Suppress all warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Simple formula-based prediction (no ML model needed)
def predict_price(carat, cut, color, clarity, depth, table, x, y, z):
    """
    Simple formula-based diamond price prediction
    Based on common diamond pricing factors
    """
    # Base price per carat (simplified)
    base_price_per_carat = 5000
    
    # Carat weight factor (exponential growth)
    carat_factor = carat ** 1.5
    
    # Cut quality multiplier
    cut_multipliers = {1: 0.7, 2: 0.8, 3: 0.9, 4: 1.0, 5: 1.1}
    cut_factor = cut_multipliers.get(cut, 1.0)
    
    # Color quality multiplier (D=best, J=worst)
    color_multipliers = {1: 1.3, 2: 1.2, 3: 1.1, 4: 1.0, 5: 0.9, 6: 0.8, 7: 0.7}
    color_factor = color_multipliers.get(color, 1.0)
    
    # Clarity multiplier
    clarity_multipliers = {1: 0.6, 2: 0.7, 3: 0.8, 4: 0.9, 5: 1.0, 6: 1.1, 7: 1.2, 8: 1.3}
    clarity_factor = clarity_multipliers.get(clarity, 1.0)
    
    # Depth and table factors (optimal ranges)
    depth_factor = 1.0
    if 58 <= depth <= 62:  # Optimal depth range
        depth_factor = 1.1
    elif depth < 55 or depth > 65:
        depth_factor = 0.8
    
    table_factor = 1.0
    if 53 <= table <= 57:  # Optimal table range
        table_factor = 1.05
    elif table < 50 or table > 60:
        table_factor = 0.9
    
    # Calculate predicted price
    predicted_price = (base_price_per_carat * carat_factor * 
                      cut_factor * color_factor * clarity_factor * 
                      depth_factor * table_factor)
    
    return predicted_price

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
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

        # Convert categorical to numerical
        cut_map = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
        color_map = {'D': 1, 'E': 2, 'F': 3, 'G': 4, 'H': 5, 'I': 6, 'J': 7}
        clarity_map = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}

        cut = cut_map.get(cut, 0)
        color = color_map.get(color, 0)
        clarity = clarity_map.get(clarity, 0)

        # Use formula-based prediction (no ML model needed)
        prediction_value = predict_price(carat, cut, color, clarity, depth, table, x, y, z)
        prediction_value = round(prediction_value, 2)

        return render_template('result.html', prediction=prediction_value)

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
