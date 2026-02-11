"""
Vercel serverless function handler for FastAPI
"""
import sys
import os
import traceback

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    # Import the FastAPI app
    from backend.app.main import app
    
    # Vercel Python runtime expects 'handler' to be the ASGI app
    handler = app
except Exception as e:
    # Log the error for debugging
    error_msg = f"Failed to import FastAPI app: {str(e)}\n{traceback.format_exc()}"
    print(error_msg)
    
    # Create a minimal error handler
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    error_app = FastAPI()
    
    @error_app.exception_handler(Exception)
    async def global_exception_handler(request, exc):
        return JSONResponse(
            status_code=500,
            content={
                "error": "Server configuration error",
                "message": str(e),
                "traceback": traceback.format_exc() if os.getenv("DEBUG") else None
            }
        )
    
    handler = error_app
