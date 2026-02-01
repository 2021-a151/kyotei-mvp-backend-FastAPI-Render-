from fastapi import FastAPI
from app.routes.health import router as health_router

app = FastAPI(title="Kyotei MVP API", version="0.1")

@app.get("/")
def root():
    return {"ok": True, "service": "kyotei-mvp-backend"}

app.include_router(health_router, prefix="/api")
from app.routes.dbtest import router as dbtest_router
app.include_router(dbtest_router, prefix="/api")
from app.routes.dbtest import router as dbtest_router
app.include_router(dbtest_router, prefix="/api")
from app.routes.admin import router as admin_router
...
app.include_router(admin_router, prefix="/api")
