# 💎 Diamond Price Prediction Web App

A Flask-based Machine Learning web application that predicts the price of a diamond based on its physical and categorical attributes such as carat, cut, color, and clarity.  
The model was trained using a regression algorithm and integrated into a simple and elegant web interface.

---

## 🚀 Project Overview

This project demonstrates the complete Machine Learning workflow:
1. Data Preprocessing and Feature Engineering  
2. Model Training and Serialization (`model.pkl`)  
3. Web Application Development with Flask  
4. Model Deployment and Real-time Prediction

Users can input diamond features via a web form and instantly get the **predicted price**.

---

## 🧠 Features

- Interactive web interface built using **Flask**
- Real-time diamond price prediction
- Encoded categorical variables (Cut, Color, Clarity)
- Handles all form validations gracefully
- Model and feature names loaded via `joblib`
- Organized folder structure for easy extension

---

## 🧰 Tech Stack

| Layer | Technology |
|--------|-------------|
| **Frontend** | HTML, CSS (Bootstrap) |
| **Backend** | Python (Flask) |
| **Machine Learning** | Scikit-learn, Pandas, NumPy |
| **Model Serialization** | Joblib |
| **IDE / Tools** | VS Code, Flask Extension |

---

## 🏗️ Project Structure
DiamondPricePrediction/
│
├── app.py # Main Flask application
├── model.pkl # Trained ML model
├── model_features.pkl # Saved feature names
│
├── templates/
│ ├── index.html # Input form page
│ └── result.html # Prediction result page
│
├── static/
│ ├── style.css # Optional CSS styles
│
├── README.md # Project documentation
└── requirements.txt # Python dependencies



---

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/DiamondPricePrediction.git
cd DiamondPricePrediction
```

### 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For macOS/Linux

### 3. Install dependencies
pip install -r requirements.txt


### 4. Run the Flask app
python app.py

Then open your browser and visit:
👉 http://127.0.0.1:5000/



| Feature   | Description                 | Example |
| --------- | --------------------------- | ------- |
| `carat`   | Weight of the diamond       | 0.7     |
| `cut`     | Cut quality (Fair → Ideal)  | Ideal   |
| `color`   | Diamond color grade (D → J) | G       |
| `clarity` | Diamond clarity grade       | VS2     |
| `depth`   | Total depth percentage      | 61.5    |
| `table`   | Width of top of diamond     | 57      |
| `x`       | Length in mm                | 5.8     |
| `y`       | Width in mm                 | 5.9     |
| `z`       | Depth in mm                 | 3.6     |




🧮 Model Details

Algorithm: Linear Regression / Random Forest Regressor (based on your training)

Libraries Used:

scikit-learn

pandas

numpy

Saved using joblib for production use.




🖼️ Screenshots

Add screenshots of your web pages here

<img width="1920" height="869" alt="image" src="https://github.com/user-attachments/assets/9d599faf-e51e-423a-9727-e398928118b2" /> 
templates/index.html — Input Page
<img width="1920" height="869" alt="image" src="https://github.com/user-attachments/assets/00553149-849e-44f0-a629-df04f2a4f789" />
 templates/result.html — Prediction Output



🛡️ Error Handling

Gracefully handles missing or invalid inputs

Displays human-readable error messages on result page

Prevents app crash with try/except block during prediction


🔮 Future Improvements

Improve model accuracy using XGBoost or CatBoost

Add visualizations for data insights

Deploy on Render / AWS / Heroku / Azure

Add user authentication and history tracking


👨‍💻 Author

Omkar Khandagale
📧 omkarkhandagale12@gmail.com


🪪 License

This project is licensed under the MIT License — feel free to modify and use it.
