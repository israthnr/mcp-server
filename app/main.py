from fastapi import FastAPI
from app.routes import cv, email

app = FastAPI(title="MCP Server")

# Register routes
app.include_router(cv.router)
app.include_router(email.router)
