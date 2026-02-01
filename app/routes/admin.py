from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
import os
from datetime import datetime, timezone

from app.db import get_db

router = APIRouter()


def _require_admin(api_key: str | None):
    expected = os.environ.get("ADMIN_API_KEY")
    if not expected:
        raise HTTPException(status_code=500, detail="ADMIN_API_KEY is not set")
    if not api_key or api_key != expected:
        raise HTTPException(status_code=403, detail="Forbidden")


@router.get("/admin/ingest")
def ingest(date: str, api_key: str | None = None, db: Session = Depends(get_db)):
    """
    ダミー版 ingest（ブラウザGETで動く版）
    - races / entries / previews / decisions / picks に1件ずつUPSERT
    - dateはYYYYMMDD文字列（例：20260201）
    """
    _require_admin(api_key)

    race_id = f"{date}-11-01"
    now = datetime.now(timezone.utc)

    # races UPSERT
    db.execute(
        text(
            """
            insert into public.races (race_id, race_date, jcd, rno, close_at, created_at, updated_at)
            values (:race_id, :race_date, '11', 1, :close_at, :now, :now)
            on conflict (race_id) do update set
              updated_at = excluded.updated_at,
              close_at = excluded.close_at
            """
        ),
        {"race_id": race_id, "race_date": date, "close_at": now, "now": now},
    )

    # entries UPSERT（6艇ダミー）
    for lane in range(1, 7):
        db.execute(
            text(
                """
                insert into public.entries (race_id, lane, racer_id, racer_name, created_at)
                values (:race_id, :lane, :racer_id, :racer_name, :now)
                on conflict (race_id, lane) do update set
                  racer_id = excluded.racer_id,
                  racer_name = excluded.racer_name
                """
            ),
            {
                "race_id": race_id,
                "lane": lane,
                "racer_id": f"R{lane:02d}",
                "racer_name": f"ダミー選手{lane}",
                "now": now,
            },
        )

    # previews UPSERT（JSONBはPythonのlistをそのまま渡す）
    db.execute(
        text(
            """
            insert into public.previews (race_id, show_time, show_st, motor2, fetched_at)
            values (:race_id, :show_time, :show_st, :motor2, :now)
            on conflict (race_id) do update set
              show_time = excluded.show_time,
              show_st   = excluded.show_st,
              motor2    = excluded.motor2,
              fetched_at = excluded.fetched_at
            """
        ),
        {
            "race_id": race_id,
            "show_time": [6.72, 6.75, 6.78, 6.80, 6.77, 6.74],
            "show_st": [0.12, 0.14, 0.16, 0.13, 0.15, 0.11],
            "motor2": [38.1, 42.3, 27.5, 31.0, 33.2, 29.9],
            "now": now,
        },
    )

    # decisions UPSERT（JSONBは文字列でなくPythonのlist/dictを渡す）
    db.execute(
        text(
            """
            insert into public.decisions (race_id, status, weak_flags, good_flags, reason_summary, reason_details, computed_at)
            values (:race_id, :status, :weak_flags, :good_flags, :summary, :details, :now)
            on conflict (race_id) do update set
              status = excluded.status,
              weak_flags = excluded.weak_flags,
              good_flags = excluded.good_flags,
              reason_summary = excluded.reason_summary,
              reason_details = excluded.reason_details,
              computed_at = excluded.computed_at
            """
        ),
        {
            "race_id": race_id,
            "status": "GO",
            "weak_flags": [],
            "good_flags": ["TIME_TOP3", "ST_TOP3"],
            "summary": "条件が揃っているため、今回はGOです。",
            "details": [
                {"key": "showTimeRank", "label": "展示タイム", "value": "2位"},
                {"key": "showStRank", "label": "展示ST", "value": "3位"},
            ],
            "now": now,
        },
    )

    # picks UPSERT（ticketsもPython listで渡す）
    tickets = [
        {"ticket": "1-2-6", "rank": 1, "tag": "RECOMMENDED"},
        {"ticket": "1-6-2", "rank": 2, "tag": "RECOMMENDED"},
        {"ticket": "1-2-3", "rank": 3, "tag": "RECOMMENDED"},
        {"ticket": "1-3-2", "rank": 4, "tag": "RECOMMENDED"},
        {"ticket": "1-2-4", "rank": 5, "tag": "RECOMMENDED"},
        {"ticket": "1-4-2", "rank": 6, "tag": "RECOMMENDED"},
        {"ticket": "1-2-5", "rank": 7, "tag": "RECOMMENDED"},
    ]

    db.execute(
        text(
            """
            insert into public.picks (race_id, max_points, tickets, computed_at)
            values (:race_id, :max_points, :tickets, :now)
            on conflict (race_id) do update set
              tickets = excluded.tickets,
              computed_at = excluded.computed_at
            """
        ),
        {"race_id": race_id, "max_points": 7, "tickets": tickets, "now": now},
    )

    db.commit()
    return {"ok": True, "raceId": race_id, "inserted": True}
