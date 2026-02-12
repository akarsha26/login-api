#!/usr/bin/env python3
"""
Startup script for Railway
Reads PORT from environment and starts uvicorn
"""
import os
import sys

# Get PORT from environment, default to 8000
port = int(os.getenv("PORT", "8000"))

print("=" * 50)
print("Starting FastAPI application...")
print(f"PORT: {port}")
print(f"PYTHONPATH: {os.getenv('PYTHONPATH', 'not set')}")
print(f"MONGODB_URI set: {'yes' if os.getenv('MONGODB_URI') else 'no'}")
print(f"JWT_SECRET_KEY set: {'yes' if os.getenv('JWT_SECRET_KEY') else 'no'}")
print("=" * 50)

# Start uvicorn
import uvicorn
uvicorn.run(
    "backend.app.main:app",
    host="0.0.0.0",
    port=port,
    log_level="info"
)
