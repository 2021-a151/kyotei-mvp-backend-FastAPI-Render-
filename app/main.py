from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.dbtest import router as dbtest_router
from app.routes.admin import router as admin_router
from app.routes.axia_test import router as axia_test_router

app = FastAPI(title="Kyotei MVP API", version="0.1")


@app.get("/")
def root():
    return {"ok": True, "service": "kyotei-mvp-backend"}


app.include_router(health_router, prefix="/api")
app.include_router(dbtest_router, prefix="/api")
app.include_router(admin_router, prefix="/api")
app.include_router(axia_test_router, prefix="/api")
