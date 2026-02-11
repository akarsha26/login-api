"""
Vercel serverless function handler for FastAPI
"""
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, project_root)

# Import the FastAPI app
from backend.app.main import app

# Vercel Python runtime expects 'handler' to be the ASGI app
handler = app
