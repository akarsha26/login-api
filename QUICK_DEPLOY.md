# Quick Deployment Checklist

## ✅ Pre-Deployment Checklist

- [ ] Code is working locally
- [ ] All files committed to Git
- [ ] `.env` file is in `.gitignore` (secrets not committed)
- [ ] GitHub account ready
- [ ] Vercel account ready

---

## 🚀 Deployment Steps (5 Minutes)

### 1. Push to GitHub (2 min)
```bash
git init
git add .
git commit -m "Ready for deployment"
git remote add origin https://github.com/YOUR_USERNAME/login-api.git
git push -u origin main
```

### 2. Connect to Vercel (1 min)
- Go to https://vercel.com
- Click "Add New" → "Project"
- Import your GitHub repo
- Click "Deploy"

### 3. Add Environment Variables (2 min)
Go to: **Settings** → **Environment Variables**

Add these 12 variables (copy from QUICK_DEPLOY.md below):

---

## 📋 Environment Variables (Copy-Paste Ready)

Add each one in Vercel Dashboard:

1. **MONGODB_URI**
   ```
   mongodb+srv://philbug36_db_user:FaMDgnao9sw6eC8l@cluster0.96tz3me.mongodb.net/?appName=Cluster0
   ```

2. **MONGODB_DB_NAME**
   ```
   login_app
   ```

3. **JWT_SECRET_KEY**
   ```
   ey0mvm-8a3rR4LL-Ypmz6CNOp9wLByi85T0g320ssbtJvos43Fn6_vdsVRvKIQmHx8z-qzJ9ohJg0jJ0vgGNsw
   ```

4. **JWT_ALGORITHM**
   ```
   HS256
   ```

5. **JWT_ACCESS_TOKEN_EXPIRE_MINUTES**
   ```
   30
   ```

6. **JWT_REFRESH_TOKEN_EXPIRE_DAYS**
   ```
   7
   ```

7. **SMTP_HOST**
   ```
   smtp.gmail.com
   ```

8. **SMTP_PORT**
   ```
   587
   ```

9. **SMTP_USER**
   ```
   zenvia07@gmail.com
   ```

10. **SMTP_PASSWORD**
    ```
    ogntznelsmhkqdvi
    ```

11. **EMAIL_FROM**
    ```
    zenvia07@gmail.com
    ```

12. **FRONTEND_URL**
    ```
    https://your-project-name.vercel.app
    ```
    ⚠️ **Update this after first deployment with your actual URL!**

---

## 🔄 After First Deployment

1. Get your URL: `https://your-project-name.vercel.app`
2. Update `FRONTEND_URL` environment variable with this URL
3. Redeploy (or push a new commit)
4. Test your site!

---

## 🎯 Your Production URL

After deployment, you'll get:
```
https://your-project-name.vercel.app
```

This is your **global URL** - share it with anyone!

---

## ❓ Need Help?

- Check deployment logs in Vercel Dashboard
- Verify all environment variables are set
- Make sure MongoDB Atlas allows all IPs (0.0.0.0/0)
- Test API: `https://your-url.vercel.app/api/health`
