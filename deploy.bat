@echo off
REM Deployment script for Vercel (Windows)

echo Starting deployment to Vercel...

REM Check if Vercel CLI is installed
where vercel >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Vercel CLI not found. Installing...
    npm install -g vercel
)

REM Login to Vercel (if not already logged in)
echo Checking Vercel login...
vercel whoami
if %ERRORLEVEL% NEQ 0 (
    vercel login
)

REM Deploy to production
echo Deploying to Vercel...
vercel --prod

echo Deployment complete!
echo Don't forget to:
echo   1. Set environment variables in Vercel dashboard
echo   2. Update FRONTEND_URL to your production URL
echo   3. Update frontend/js/main.js API_BASE_URL

pause
