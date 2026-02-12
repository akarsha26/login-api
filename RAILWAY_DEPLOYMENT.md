# Railway Deployment Guide

## Quick Steps

### 1. Sign Up & Connect GitHub
- Go to https://railway.app
- Sign up with GitHub
- Authorize Railway to access your repositories

### 2. Create New Project
- Click **"New Project"**
- Select **"Deploy from GitHub repo"**
- Find and select `akarsha26/login-api`
- Click **"Deploy Now"**

### 3. Add Environment Variables
Railway will start deploying. While it's building:

1. Go to your project → **"Variables"** tab
2. Click **"New Variable"**
3. Add each variable one by one:

```
MONGODB_URI=mongodb+srv://philbug36_db_user:FaMDgnao9sw6eC8l@cluster0.96tz3me.mongodb.net/?appName=Cluster0
MONGODB_DB_NAME=login_app
JWT_SECRET_KEY=ey0mvm-8a3rR4LL-Ypmz6CNOp9wLByi85T0g320ssbtJvos43Fn6_vdsVRvKIQmHx8z-qzJ9ohJg0jJ0vgGNsw
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
JWT_REFRESH_TOKEN_EXPIRE_DAYS=7
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=zenvia07@gmail.com
SMTP_PASSWORD=ogntznelsmhkqdvi
EMAIL_FROM=zenvia07@gmail.com
FRONTEND_URL=https://your-app-name.up.railway.app
```

**Important**: After deployment, Railway will give you a URL. Update `FRONTEND_URL` with that URL!

### 4. Configure Service Settings
1. Go to **"Settings"** tab
2. Under **"Deploy"**:
   - **Start Command**: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
   - Railway will auto-detect this, but you can verify

### 5. Get Your URL
1. After deployment succeeds, go to **"Settings"** → **"Networking"**
2. Click **"Generate Domain"** (or use the default one)
3. Your app will be available at: `https://your-app-name.up.railway.app`
4. **Update `FRONTEND_URL`** variable with this URL
5. Redeploy (Railway will auto-redeploy when you update variables)

## Troubleshooting

### Build Fails?
- Check build logs in Railway dashboard
- Make sure all files are committed to GitHub
- Verify `requirements.txt` is correct

### App Crashes?
- Check deploy logs
- Verify all environment variables are set
- Check MongoDB connection (make sure IP whitelist allows Railway IPs)

### Port Issues?
- Railway automatically sets `PORT` environment variable
- The Dockerfile uses `${PORT:-8000}` to handle this

## Railway vs Vercel

**Railway Advantages:**
- ✅ Simpler deployment (just Dockerfile)
- ✅ Better for full-stack apps
- ✅ More predictable behavior
- ✅ Better error messages

**What's Different:**
- Uses Dockerfile instead of `vercel.json`
- Environment variables set in Railway dashboard
- URL format: `your-app.up.railway.app`

## After Deployment

1. Test your app: `https://your-app.up.railway.app`
2. Test API: `https://your-app.up.railway.app/api/health`
3. Update `FRONTEND_URL` with your Railway URL
4. Test registration/login flow

Your app should work perfectly on Railway! 🚀
