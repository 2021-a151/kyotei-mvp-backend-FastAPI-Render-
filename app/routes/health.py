from fastapi import APIRouter
import os
from sqlalchemy import create_engine, text

router = APIRouter()

@router.get("/health")
def health():
    return {"ok": True}

@router.get("/health/db")
def health_db():
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        return {"ok": False, "error": "DATABASE_URL not set"}

    engine = create_engine(db_url, pool_pre_ping=True)
    with engine.connect() as conn:
        conn.execute(text("select 1"))
    return {"ok": True, "db": "connected"}
