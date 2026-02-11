#!/bin/bash
# Deployment script for Vercel

echo "🚀 Starting deployment to Vercel..."

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Login to Vercel (if not already logged in)
echo "📝 Checking Vercel login..."
vercel whoami || vercel login

# Deploy to production
echo "🌐 Deploying to Vercel..."
vercel --prod

echo "✅ Deployment complete!"
echo "📧 Don't forget to:"
echo "   1. Set environment variables in Vercel dashboard"
echo "   2. Update FRONTEND_URL to your production URL"
echo "   3. Update frontend/js/main.js API_BASE_URL"
