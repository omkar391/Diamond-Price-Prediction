# Deployment Instructions for Diamond Price Prediction App

## Option 1: Deploy to Heroku

### Prerequisites:
1. Install Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli
2. Create a free Heroku account at https://heroku.com
3. Login to Heroku: `heroku login`

### Deployment Steps:
```bash
# Initialize git repository (if not already done)
git init
git add .
git commit -m "Initial commit"

# Create Heroku app
heroku create your-diamond-price-app

# Deploy to Heroku
git push heroku main

# Open the deployed app
heroku open
```

## Option 2: Deploy to Railway

### Prerequisites:
1. Create account at https://railway.app
2. Connect your GitHub repository

### Deployment Steps:
1. Go to Railway.app
2. Click "New Project"
3. Connect your GitHub repository
4. Railway will automatically detect it's a Python app and deploy

## Option 3: Deploy to Render

### Prerequisites:
1. Create account at https://render.com
2. Connect your GitHub repository

### Deployment Steps:
1. Go to Render.com
2. Click "New Web Service"
3. Connect your GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`

## Option 4: Deploy to PythonAnywhere

### Prerequisites:
1. Create account at https://pythonanywhere.com

### Deployment Steps:
1. Upload your files via the web interface
2. Create a new web app
3. Configure the WSGI file to point to your Flask app
4. Set up the virtual environment and install requirements

## Files Created for Deployment:
- `Procfile`: Tells Heroku how to run your app
- `runtime.txt`: Specifies Python version
- `requirements.txt`: Lists all dependencies
- Updated `app.py`: Configured for production deployment

## Important Notes:
- Your app is now configured to run on any cloud platform
- The model files (model.pkl, model_features.pkl) will be included in deployment
- The app will be accessible via a public URL once deployed
- Make sure to test the deployed app thoroughly
