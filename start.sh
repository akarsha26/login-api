#!/bin/bash
# Startup script for Railway
# This ensures PORT is properly set and the app starts correctly

# Set default PORT if not set
export PORT=${PORT:-8000}

# Print environment info for debugging
echo "Starting application..."
echo "PORT: $PORT"
echo "PYTHONPATH: $PYTHONPATH"
echo "MONGODB_URI set: $([ -n "$MONGODB_URI" ] && echo 'yes' || echo 'no')"
echo "JWT_SECRET_KEY set: $([ -n "$JWT_SECRET_KEY" ] && echo 'yes' || echo 'no')"

# Start uvicorn
exec uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
