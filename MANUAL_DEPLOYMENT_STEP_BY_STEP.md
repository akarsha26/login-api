# Manual Deployment Guide - Step by Step

## Step 1: Push Code to GitHub

### 1.1 Initialize Git Repository (if not already done)
```bash
cd C:\Users\AKARSHA\Downloads\py-api
git init
```

### 1.2 Create .gitignore (already exists, but verify)
Make sure `.gitignore` includes:
- `.env` (so secrets aren't committed)
- `__pycache__/`
- `venv/`
- etc.

### 1.3 Add All Files
```bash
git add .
```

### 1.4 Commit Files
```bash
git commit -m "Initial commit - Login API with authentication"
```

### 1.5 Create GitHub Repository
1. Go to https://github.com
2. Click **"+"** → **"New repository"**
3. Repository name: `login-api` (or your choice)
4. Description: "User authentication API with FastAPI"
5. Choose: **Public** or **Private**
6. **DO NOT** initialize with README, .gitignore, or license (we already have files)
7. Click **"Create repository"**

### 1.6 Connect and Push to GitHub
GitHub will show you commands. Run these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/login-api.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

**If you get authentication error:**
- Use GitHub Personal Access Token instead of password
- Or use GitHub Desktop app

---

## Step 2: Connect to Vercel via GitHub

### 2.1 Go to Vercel
1. Visit: https://vercel.com
2. Click **"Sign Up"** or **"Log In"**
3. Choose **"Continue with GitHub"** (recommended)

### 2.2 Import Project
1. After login, click **"Add New..."** → **"Project"**
2. You'll see your GitHub repositories
3. Find `login-api` (or your repo name)
4. Click **"Import"**

### 2.3 Configure Project
Vercel will auto-detect settings:
- **Framework Preset**: Leave as is (or select "Other")
- **Root Directory**: `./` (current directory)
- **Build Command**: Leave empty (Vercel handles Python)
- **Output Directory**: Leave empty
- **Install Command**: Leave empty

Click **"Deploy"** (we'll set environment variables after)

---

## Step 3: Set Environment Variables

### 3.1 Go to Project Settings
1. After deployment starts, go to your project dashboard
2. Click **"Settings"** tab
3. Click **"Environment Variables"** in left sidebar

### 3.2 Add Each Variable
Click **"Add New"** for each variable below:

**Variable 1:**
- Key: `MONGODB_URI`
- Value: `mongodb+srv://philbug36_db_user:FaMDgnao9sw6eC8l@cluster0.96tz3me.mongodb.net/?appName=Cluster0`
- Environment: Select **Production**, **Preview**, and **Development**
- Click **"Save"**

**Variable 2:**
- Key: `MONGODB_DB_NAME`
- Value: `login_app`
- Environment: All
- Click **"Save"**

**Variable 3:**
- Key: `JWT_SECRET_KEY`
- Value: `ey0mvm-8a3rR4LL-Ypmz6CNOp9wLByi85T0g320ssbtJvos43Fn6_vdsVRvKIQmHx8z-qzJ9ohJg0jJ0vgGNsw`
- Environment: All
- Click **"Save"**

**Variable 4:**
- Key: `JWT_ALGORITHM`
- Value: `HS256`
- Environment: All
- Click **"Save"**

**Variable 5:**
- Key: `JWT_ACCESS_TOKEN_EXPIRE_MINUTES`
- Value: `30`
- Environment: All
- Click **"Save"**

**Variable 6:**
- Key: `JWT_REFRESH_TOKEN_EXPIRE_DAYS`
- Value: `7`
- Environment: All
- Click **"Save"**

**Variable 7:**
- Key: `SMTP_HOST`
- Value: `smtp.gmail.com`
- Environment: All
- Click **"Save"**

**Variable 8:**
- Key: `SMTP_PORT`
- Value: `587`
- Environment: All
- Click **"Save"**

**Variable 9:**
- Key: `SMTP_USER`
- Value: `zenvia07@gmail.com`
- Environment: All
- Click **"Save"**

**Variable 10:**
- Key: `SMTP_PASSWORD`
- Value: `ogntznelsmhkqdvi`
- Environment: All
- Click **"Save"**

**Variable 11:**
- Key: `EMAIL_FROM`
- Value: `zenvia07@gmail.com`
- Environment: All
- Click **"Save"**

**Variable 12:**
- Key: `FRONTEND_URL`
- Value: `https://your-project-name.vercel.app` 
  - **IMPORTANT**: Replace `your-project-name` with your actual Vercel project name
  - You'll see this URL after first deployment
  - You can update it later
- Environment: All
- Click **"Save"**

---

## Step 4: Redeploy with Environment Variables

### 4.1 Trigger Redeployment
1. Go to **"Deployments"** tab
2. Click the **"..."** (three dots) on the latest deployment
3. Click **"Redeploy"**
4. Select **"Use existing Build Cache"** (optional)
5. Click **"Redeploy"**

OR

1. Make a small change to any file (like README.md)
2. Commit and push to GitHub
3. Vercel will automatically redeploy

---

## Step 5: Get Your Production URL

### 5.1 Find Your URL
1. After deployment completes, go to **"Deployments"** tab
2. Click on the latest deployment
3. You'll see: **"Visit"** button
4. Your URL will be: `https://your-project-name.vercel.app`

### 5.2 Update FRONTEND_URL
1. Go back to **Settings** → **Environment Variables**
2. Find `FRONTEND_URL`
3. Click **"Edit"**
4. Update value to your actual URL: `https://your-project-name.vercel.app`
5. Click **"Save"**
6. Redeploy again

---

## Step 6: Test Your Deployment

### 6.1 Test the URL
1. Visit: `https://your-project-name.vercel.app`
2. You should see the login page

### 6.2 Test API
1. Visit: `https://your-project-name.vercel.app/api/health`
2. Should return: `{"status": "healthy", "message": "API is operational"}`

### 6.3 Test Registration
1. Fill out registration form
2. Submit
3. Check email for activation link
4. Click activation link
5. Should redirect to login

---

## Troubleshooting

### Deployment Fails?
- Check **"Deployments"** tab → Click failed deployment → Check logs
- Common issues:
  - Missing environment variables
  - Python version mismatch
  - Import errors

### Environment Variables Not Working?
- Make sure you selected **All** environments (Production, Preview, Development)
- Redeploy after adding variables
- Check variable names match exactly (case-sensitive)

### Email Links Not Working?
- Verify `FRONTEND_URL` is set to your production URL
- Should be: `https://your-project-name.vercel.app` (not localhost)
- Redeploy after updating

### API Calls Failing?
- Check browser console (F12) for errors
- Verify CORS settings
- Check network tab for failed requests

---

## Quick Reference: All Environment Variables

Copy-paste ready list:

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

**Remember**: Update `FRONTEND_URL` with your actual Vercel URL after first deployment!

---

## Success Checklist

- [ ] Code pushed to GitHub
- [ ] Project imported to Vercel
- [ ] All environment variables added
- [ ] First deployment successful
- [ ] FRONTEND_URL updated with actual URL
- [ ] Redeployed with updated FRONTEND_URL
- [ ] Tested production URL
- [ ] Tested registration flow
- [ ] Tested activation email
- [ ] Everything working! 🎉
