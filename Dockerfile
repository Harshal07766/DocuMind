# Use Python 3.11 slim image for better compatibility
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install only FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Create the app inline to avoid file copy issues
RUN echo 'from fastapi import FastAPI\napp = FastAPI()\n@app.get("/")\ndef root(): return {"status": "ok"}\n@app.get("/health")\ndef health(): return {"status": "healthy"}' > app.py

# Expose port
EXPOSE 8000

# Run the test application
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
