from fastapi import FastAPI
from app.routes.health import router as health_router

app = FastAPI(title="Kyotei MVP API", version="0.1")

@app.get("/")
def root():
    return {"ok": True, "service": "kyotei-mvp-backend"}

app.include_router(health_router, prefix="/api")
