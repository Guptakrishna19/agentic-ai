# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install python dependencies
RUN pip install --no-cache-dir fastapi uvicorn pydantic python-dotenv

# Copy application files
COPY . .

# Expose the application port
EXPOSE 8000

# Start uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
