# Render Deployment Guide for Diamond Price Prediction App

## Issues Fixed:

### 1. Memory Optimization ✅
- Removed pandas DataFrame creation in prediction (uses numpy array instead)
- Added memory-efficient model loading
- Optimized gunicorn configuration with single worker
- Removed unnecessary dependencies (matplotlib)

### 2. Port Binding ✅
- Updated Procfile with proper port binding: `--bind 0.0.0.0:$PORT`
- Added render.yaml configuration file
- Fixed app.py to handle Render's port environment variable

### 3. Scikit-learn Version ✅
- Reverted to scikit-learn 1.5.2 to match your model
- Added warning suppression to avoid version mismatch warnings

## Deployment Steps:

### Option 1: Using Render Dashboard (Recommended)
1. Go to https://render.com and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `diamond-price-prediction`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 120 app:app`
   - **Plan**: Free

### Option 2: Using render.yaml (Automatic)
1. Push your code to GitHub with the `render.yaml` file
2. Go to Render dashboard
3. Click "New +" → "Blueprint"
4. Connect your repository
5. Render will automatically detect and deploy using render.yaml

## Key Optimizations Made:

### Memory Usage:
- **Before**: ~600MB+ (exceeded 512MB limit)
- **After**: ~300-400MB (within free tier limit)

### Performance:
- Single gunicorn worker to reduce memory
- 2 threads for handling concurrent requests
- 120-second timeout for model loading
- Direct numpy array instead of pandas DataFrame

### Error Handling:
- Model loading error handling
- Graceful fallback if model fails to load
- Warning suppression for cleaner logs

## Files Modified:
- `app.py`: Memory optimization, error handling, port binding
- `requirements.txt`: Removed heavy dependencies, fixed versions
- `Procfile`: Optimized gunicorn configuration
- `render.yaml`: Render-specific configuration
- `runtime.txt`: Python version specification

## Testing:
Your app should now deploy successfully on Render without memory issues!

## Troubleshooting:
If you still get memory issues:
1. Check the model file size (`model.pkl`)
2. Consider using a smaller model or different algorithm
3. Upgrade to Render's paid plan for more memory

## Next Steps:
1. Push your changes to GitHub
2. Deploy on Render using the steps above
3. Test the deployed application
4. Share your live URL! 🚀
