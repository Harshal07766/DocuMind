"""
Minimal test app for Docker healthcheck
"""
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Test App")

@app.get("/")
async def root():
    print("🔍 Root endpoint called")
    return {"message": "Test app is running", "status": "ok"}

@app.get("/health")
async def health():
    print("❤️ Health endpoint called")
    return {"status": "healthy", "message": "Service is running"}

if __name__ == "__main__":
    print("🚀 Starting test app...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
