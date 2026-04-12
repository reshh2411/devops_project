from fastapi import FastAPI
from datetime import datetime
import socket

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello DevOps 🚀",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow()
    }

@app.get("/info")
def info():
    return {
        "app": "DevOps Demo",
        "version": "1.0.0",
        "hostname": socket.gethostname()
    }
