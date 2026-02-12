#!/bin/bash
# Startup script for Railway
# This ensures PORT is properly set and the app starts correctly

# Set default PORT if not set (Railway sets PORT automatically)
if [ -z "$PORT" ]; then
    export PORT=8000
fi

# Print environment info for debugging
echo "=========================================="
echo "Starting application..."
echo "PORT: $PORT"
echo "PYTHONPATH: $PYTHONPATH"
echo "MONGODB_URI set: $([ -n "$MONGODB_URI" ] && echo 'yes' || echo 'no')"
echo "JWT_SECRET_KEY set: $([ -n "$JWT_SECRET_KEY" ] && echo 'yes' || echo 'no')"
echo "=========================================="

# Start uvicorn with explicit port number
exec uvicorn backend.app.main:app --host 0.0.0.0 --port "$PORT"
