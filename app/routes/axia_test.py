"""
AXIA Runtime Test Endpoint
Safe test endpoint — AXIA Real Code Fix Operator (P7).
AXIA UI Fix — /axia-status HTML status page added (P8).
This file does NOT modify existing routes or database schema.
"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import datetime

router = APIRouter()


@router.get("/axia-test")
async def axia_test():
    """AXIA Runtime Test — safe endpoint, no DB access"""
    return {
        "status": "ok",
        "message": "AXIA runtime verified",
        "version": "p7",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    }


@router.get("/axia-test/health")
async def axia_test_health():
    """AXIA lightweight health check — no DB access"""
    return {
        "alive": True,
        "version": "p7",
    }


@router.get("/axia-status", response_class=HTMLResponse)
async def axia_status():
    """AXIA Status Page — simple HTML UI (P8)"""
    now = datetime.datetime.utcnow().isoformat() + "Z"
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AXIA Status</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
    }}
    .card {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 40px 48px;
      max-width: 480px;
      width: 100%;
      box-shadow: 0 4px 24px rgba(0,0,0,0.4);
    }}
    .badge {{
      display: inline-block;
      background: #22c55e;
      color: #fff;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 20px;
      text-transform: uppercase;
    }}
    h1 {{
      font-size: 24px;
      font-weight: 700;
      margin: 0 0 8px;
      color: #f8fafc;
    }}
    .subtitle {{
      color: #94a3b8;
      font-size: 14px;
      margin-bottom: 32px;
    }}
    .row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 0;
      border-bottom: 1px solid #334155;
      font-size: 14px;
    }}
    .row:last-child {{ border-bottom: none; }}
    .label {{ color: #94a3b8; }}
    .value {{ color: #f1f5f9; font-weight: 500; font-family: monospace; }}
    .ok {{ color: #22c55e; font-weight: 700; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">&#x2713; Running</div>
    <h1>AXIA Runtime Verified</h1>
    <p class="subtitle">Kyotei MVP Backend — FastAPI</p>
    <div class="row">
      <span class="label">Status</span>
      <span class="value ok">OK</span>
    </div>
    <div class="row">
      <span class="label">FastAPI</span>
      <span class="value ok">Running</span>
    </div>
    <div class="row">
      <span class="label">Version</span>
      <span class="value">P8</span>
    </div>
    <div class="row">
      <span class="label">Timestamp</span>
      <span class="value">{now}</span>
    </div>
    <div class="row">
      <span class="label">Health</span>
      <span class="value"><a href="/api/health" style="color:#60a5fa;">/api/health</a></span>
    </div>
  </div>
</body>
</html>"""
    return HTMLResponse(content=html, status_code=200)
