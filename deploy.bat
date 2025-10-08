@echo off
echo Deploying Diamond Price Prediction App to Heroku...
echo.

echo Step 1: Checking if Heroku CLI is installed...
heroku --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Heroku CLI not found. Please install it from: https://devcenter.heroku.com/articles/heroku-cli
    echo After installation, run this script again.
    pause
    exit /b 1
)

echo Step 2: Checking if logged in to Heroku...
heroku auth:whoami >nul 2>&1
if %errorlevel% neq 0 (
    echo Please login to Heroku first:
    heroku login
)

echo Step 3: Initializing git repository...
git init
git add .
git commit -m "Deploy diamond price prediction app"

echo Step 4: Creating Heroku app...
set /p appname="Enter your app name (or press Enter for auto-generated): "
if "%appname%"=="" (
    heroku create
) else (
    heroku create %appname%
)

echo Step 5: Deploying to Heroku...
git push heroku main

echo Step 6: Opening deployed app...
heroku open

echo.
echo Deployment complete! Your app should now be live.
pause
