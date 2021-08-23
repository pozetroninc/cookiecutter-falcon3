import uvicorn
from app import asgi_app

uvicorn.run(asgi_app, host="0.0.0.0", port=8000, log_level="info")
