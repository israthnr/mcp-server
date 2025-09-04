from fastapi import FastAPI
from app.routes import cv, email

app = FastAPI(title="MCP Server")

# Register routes
app.include_router(cv.router)
app.include_router(email.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
