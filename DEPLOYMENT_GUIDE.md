# Deployment Guide - Deploy to Production

## Option 1: Deploy to Vercel (Recommended)

Vercel supports FastAPI and static frontend files.

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Deploy
```bash
vercel
```

Follow the prompts:
- Set up and deploy? **Yes**
- Which scope? **Your account**
- Link to existing project? **No**
- Project name? **login-api** (or your choice)
- Directory? **./** (current directory)
- Override settings? **No**

### Step 4: Set Environment Variables in Vercel Dashboard

Go to your project on Vercel → Settings → Environment Variables

Add these variables:
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
FRONTEND_URL=https://your-project.vercel.app
```

### Step 5: Update Frontend API URL

After deployment, update `frontend/js/main.js`:
```javascript
const API_BASE_URL = 'https://your-project.vercel.app/api';
```

Or use environment-based configuration.

---

## Option 2: Deploy with Docker to Cloud Platform

### Deploy to Railway, Render, or DigitalOcean

1. Push code to GitHub
2. Connect repository to platform
3. Set environment variables
4. Deploy

---

## Option 3: Deploy Backend and Frontend Separately

### Backend: Deploy to Railway/Render/Fly.io
- Deploy FastAPI backend
- Get backend URL: `https://api.yourdomain.com`

### Frontend: Deploy to Vercel/Netlify
- Deploy static files
- Update API_BASE_URL to backend URL
- Get frontend URL: `https://yourdomain.com`

---

## Important: Update Email URLs

After deployment, update activation email URLs to use production domain instead of localhost.
