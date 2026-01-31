from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db import get_db

router = APIRouter()

@router.get("/dbtest")
def dbtest(db: Session = Depends(get_db)):
    v = db.execute(text("select 1")).scalar()
    return {"ok": True, "select1": v}
