# Production Deployment Guide

## Quick Start: Deploy to Vercel

### Prerequisites
- Node.js installed (for Vercel CLI)
- GitHub account (optional, for automatic deployments)
- Vercel account (free tier available)

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
# First deployment (will ask questions)
vercel

# Production deployment
vercel --prod
```

Or use the provided scripts:
- **Windows**: `deploy.bat`
- **Linux/Mac**: `deploy.sh`

---

## Step 4: Configure Environment Variables

After deployment, go to **Vercel Dashboard** → Your Project → **Settings** → **Environment Variables**

Add all these variables:

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
FRONTEND_URL=https://your-project-name.vercel.app
```

**Important**: Replace `your-project-name.vercel.app` with your actual Vercel URL!

---

## Step 5: Update Frontend API URL

After deployment, you'll get a URL like: `https://your-project.vercel.app`

Update `frontend/js/main.js`:

```javascript
// Change from:
const API_BASE_URL = 'http://localhost:3000/api';

// To:
const API_BASE_URL = 'https://your-project.vercel.app/api';
```

Or better yet, make it environment-aware:

```javascript
// Auto-detect API URL
const API_BASE_URL = window.location.origin + '/api';
```

This will automatically use the correct URL whether localhost or production.

---

## Step 6: Redeploy

After updating the frontend code:
```bash
vercel --prod
```

---

## Alternative: Deploy Backend and Frontend Separately

### Option A: Backend on Railway/Render, Frontend on Vercel

1. **Backend (Railway/Render)**:
   - Deploy FastAPI backend
   - Get URL: `https://api.yourdomain.com`
   - Set CORS to allow frontend domain

2. **Frontend (Vercel)**:
   - Deploy static files
   - Update `API_BASE_URL` to backend URL
   - Get URL: `https://yourdomain.com`

### Option B: Full Stack on Vercel (Current Setup)
- Both backend and frontend on same domain
- Simpler setup
- Already configured in `vercel.json`

---

## Post-Deployment Checklist

- [ ] Environment variables set in Vercel
- [ ] FRONTEND_URL updated to production URL
- [ ] Frontend API_BASE_URL updated
- [ ] Test registration flow
- [ ] Test activation email (check email links)
- [ ] Test login flow
- [ ] Verify database connection
- [ ] Check CORS settings (if using separate domains)

---

## Troubleshooting

### Email links not working?
- Check `FRONTEND_URL` environment variable
- Ensure it's set to your production URL (https://...)

### API calls failing?
- Check `API_BASE_URL` in frontend
- Verify CORS settings
- Check browser console for errors

### Database connection issues?
- Verify `MONGODB_URI` is correct
- Check MongoDB Atlas IP whitelist (allow all IPs: 0.0.0.0/0)

---

## Your Production URL

After deployment, Vercel will give you a URL like:
- `https://your-project-name.vercel.app`

This is your global URL! Share it with users.
