# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only backend-related files
COPY backend.py .
COPY ai_agent.py .
COPY requirements.txt .

# Load environment variables at runtime
ENV DOTENV_PATH="/app/.env"


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose backend port
EXPOSE 9999

# Run FastAPI backend
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "9999"]
