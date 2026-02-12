# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY backend/ ./backend/
COPY frontend/ ./frontend/
# Note: .env file is not copied - Railway uses environment variables instead

# Expose port
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Copy startup script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Run the application
# Railway provides PORT environment variable automatically
# Use shell form to ensure bash executes the script
CMD ["/bin/bash", "/app/start.sh"]
