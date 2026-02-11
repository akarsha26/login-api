"""
Vercel serverless function handler for FastAPI
"""
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from backend.app.main import app

# Export the app for Vercel
handler = app
