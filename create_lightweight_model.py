import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load the original data
print("Loading data...")
df = pd.read_csv('diamonds.csv')

# Preprocess the data (same as original)
cut_map = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
color_map = {'D': 1, 'E': 2, 'F': 3, 'G': 4, 'H': 5, 'I': 6, 'J': 7}
clarity_map = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}

df['cut'] = df['cut'].map(cut_map)
df['color'] = df['color'].map(color_map)
df['clarity'] = df['clarity'].map(clarity_map)

# Select features
features = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']
X = df[features]
y = df['price']

# Train a lightweight Linear Regression model
print("Training lightweight model...")
model = LinearRegression()
model.fit(X, y)

# Save the lightweight model
joblib.dump(model, 'lightweight_model.pkl')
print("Lightweight model saved as 'lightweight_model.pkl'")

# Test the model
y_pred = model.predict(X)
mse = np.mean((y - y_pred) ** 2)
print(f"Model MSE: {mse:.2f}")
print(f"Model R²: {model.score(X, y):.4f}")

# Show model size
import os
size = os.path.getsize('lightweight_model.pkl')
print(f"Model size: {size / 1024:.2f} KB")
