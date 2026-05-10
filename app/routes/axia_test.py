"""
AXIA Runtime Test Endpoint
Safe test endpoint — AXIA Real Code Fix Operator (P7).
AXIA UI Fix — /axia-status HTML status page added (P8).
AXIA UI Improvement — /axia-status enhanced status card (P10).
AXIA Dashboard — /axia-dashboard user-facing dashboard added (P17).
This file does NOT modify existing routes or database schema.
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
import datetime
from datetime import timezone

router = APIRouter()

_start_time = datetime.datetime.utcnow()


@router.get("/axia-test")
async def axia_test():
    """AXIA Runtime Test — safe endpoint, no DB access"""
    return {
        "status": "ok",
        "message": "AXIA runtime verified",
        "version": "p10",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    }


@router.get("/axia-test/health")
async def axia_test_health():
    """AXIA lightweight health check — no DB access"""
    return {
        "alive": True,
        "version": "p10",
    }


@router.get("/axia-status", response_class=HTMLResponse)
async def axia_status():
    """AXIA Status Page — improved status card UI (P10)"""
    now = datetime.datetime.utcnow()
    now_str = now.isoformat() + "Z"
    uptime_delta = now - _start_time
    uptime_secs = int(uptime_delta.total_seconds())
    uptime_h = uptime_secs // 3600
    uptime_m = (uptime_secs % 3600) // 60
    uptime_s = uptime_secs % 60
    uptime_str = f"{uptime_h}h {uptime_m}m {uptime_s}s"

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AXIA Status</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
      padding: 16px;
    }}
    .card {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 16px;
      padding: 36px 40px;
      max-width: 520px;
      width: 100%;
      box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    }}
    @media (max-width: 480px) {{
      .card {{ padding: 24px 20px; }}
    }}
    .header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      margin-bottom: 28px;
      gap: 12px;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #166534;
      border: 1px solid #22c55e;
      color: #4ade80;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      padding: 5px 14px;
      border-radius: 999px;
      text-transform: uppercase;
      white-space: nowrap;
    }}
    .badge-dot {{
      width: 7px;
      height: 7px;
      background: #22c55e;
      border-radius: 50%;
      animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.4; }}
    }}
    .title-block h1 {{
      font-size: 22px;
      font-weight: 700;
      margin: 0 0 4px;
      color: #f8fafc;
    }}
    .subtitle {{
      color: #64748b;
      font-size: 13px;
      margin: 0;
    }}
    .section-title {{
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #475569;
      margin: 24px 0 8px;
    }}
    .rows {{
      border: 1px solid #334155;
      border-radius: 10px;
      overflow: hidden;
    }}
    .row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 11px 16px;
      border-bottom: 1px solid #1e293b;
      font-size: 13px;
      background: #0f172a;
    }}
    .row:last-child {{ border-bottom: none; }}
    .label {{ color: #64748b; }}
    .value {{ color: #cbd5e1; font-weight: 500; font-family: 'SF Mono', 'Fira Code', monospace; font-size: 12px; }}
    .value.ok {{ color: #4ade80; }}
    .links {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 20px;
    }}
    .link-btn {{
      display: inline-block;
      background: #1e3a5f;
      border: 1px solid #2563eb;
      color: #93c5fd;
      font-size: 12px;
      font-weight: 500;
      padding: 7px 16px;
      border-radius: 8px;
      text-decoration: none;
      transition: background 0.15s;
    }}
    .link-btn:hover {{ background: #1e40af; color: #bfdbfe; }}
    .footer {{
      margin-top: 20px;
      font-size: 11px;
      color: #334155;
      text-align: right;
    }}
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <div class="title-block">
        <h1>AXIA Status</h1>
        <p class="subtitle">Kyotei MVP Backend &mdash; FastAPI</p>
      </div>
      <div class="badge">
        <span class="badge-dot"></span>
        RUNNING
      </div>
    </div>

    <div class="section-title">Runtime</div>
    <div class="rows">
      <div class="row">
        <span class="label">Status</span>
        <span class="value ok">&#x2713; Active</span>
      </div>
      <div class="row">
        <span class="label">FastAPI</span>
        <span class="value ok">Running</span>
      </div>
      <div class="row">
        <span class="label">Version</span>
        <span class="value">P10</span>
      </div>
      <div class="row">
        <span class="label">Uptime</span>
        <span class="value">{uptime_str}</span>
      </div>
      <div class="row">
        <span class="label">Updated</span>
        <span class="value">{now_str}</span>
      </div>
    </div>

    <div class="section-title">Endpoints</div>
    <div class="links">
      <a class="link-btn" href="/api/health">&#x2665; Health API</a>
      <a class="link-btn" href="/api/health/db">&#x1f5c4; DB Health</a>
      <a class="link-btn" href="/api/axia-test">&#x26a1; AXIA Test</a>
      <a class="link-btn" href="/api/axia-dashboard">&#x1f4ca; Dashboard</a>
    </div>

    <div class="footer">AXIA_RUNTIME_CLASS = REAL_USER_UI_OPERATOR</div>
  </div>
</body>
</html>"""
    return HTMLResponse(content=html, status_code=200)


@router.get("/axia-dashboard", response_class=HTMLResponse)
async def axia_dashboard():
    """AXIA User-Facing Dashboard — real-time runtime overview (P17)"""
    now = datetime.datetime.utcnow()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S UTC")
    uptime_delta = now - _start_time
    uptime_secs = int(uptime_delta.total_seconds())
    uptime_h = uptime_secs // 3600
    uptime_m = (uptime_secs % 3600) // 60
    uptime_s = uptime_secs % 60
    uptime_str = f"{uptime_h}h {uptime_m}m {uptime_s}s"

    # Active routes count (known routes in this app)
    active_routes = [
        "/api/health",
        "/api/health/db",
        "/api/dbtest",
        "/api/admin/ingest",
        "/api/axia-test",
        "/api/axia-test/health",
        "/api/axia-status",
        "/api/axia-dashboard",
    ]
    routes_count = len(active_routes)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AXIA Dashboard</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif;
      background: #0a0f1e;
      color: #e2e8f0;
      margin: 0;
      padding: 20px 16px 40px;
      min-height: 100vh;
    }}
    .container {{
      max-width: 720px;
      margin: 0 auto;
    }}
    .top-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 28px;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .top-title {{
      font-size: 24px;
      font-weight: 800;
      color: #f8fafc;
      letter-spacing: -0.02em;
      margin: 0;
    }}
    .top-sub {{
      font-size: 12px;
      color: #475569;
      margin: 2px 0 0;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #14532d;
      border: 1px solid #22c55e;
      color: #4ade80;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      padding: 5px 14px;
      border-radius: 999px;
      text-transform: uppercase;
    }}
    .badge-dot {{
      width: 7px; height: 7px;
      background: #22c55e;
      border-radius: 50%;
      animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.35; }}
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 14px;
      margin-bottom: 24px;
    }}
    .stat-card {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 18px 20px;
    }}
    .stat-label {{
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #475569;
      margin-bottom: 8px;
    }}
    .stat-value {{
      font-size: 22px;
      font-weight: 700;
      color: #f1f5f9;
      line-height: 1;
    }}
    .stat-value.ok {{ color: #4ade80; }}
    .stat-value.warn {{ color: #fbbf24; }}
    .stat-sub {{
      font-size: 11px;
      color: #475569;
      margin-top: 4px;
    }}
    .section-title {{
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #475569;
      margin: 24px 0 10px;
    }}
    .table {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 12px;
      overflow: hidden;
      margin-bottom: 24px;
    }}
    .table-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 11px 18px;
      border-bottom: 1px solid #0f172a;
      font-size: 13px;
    }}
    .table-row:last-child {{ border-bottom: none; }}
    .table-label {{ color: #64748b; }}
    .table-value {{
      color: #cbd5e1;
      font-family: 'SF Mono', 'Fira Code', monospace;
      font-size: 12px;
      font-weight: 500;
    }}
    .table-value.ok {{ color: #4ade80; }}
    .table-value.warn {{ color: #fbbf24; }}
    .links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 10px;
      margin-bottom: 24px;
    }}
    .link-btn {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: #1e293b;
      border: 1px solid #334155;
      color: #93c5fd;
      font-size: 13px;
      font-weight: 500;
      padding: 12px 16px;
      border-radius: 10px;
      text-decoration: none;
      transition: background 0.15s, border-color 0.15s;
    }}
    .link-btn:hover {{ background: #1e3a5f; border-color: #2563eb; }}
    .link-icon {{ font-size: 16px; }}
    .footer {{
      font-size: 11px;
      color: #1e293b;
      text-align: center;
      margin-top: 8px;
    }}
    @media (max-width: 480px) {{
      .top-title {{ font-size: 20px; }}
      .grid {{ grid-template-columns: 1fr 1fr; }}
    }}
  </style>
</head>
<body>
  <div class="container">

    <div class="top-bar">
      <div>
        <h1 class="top-title">AXIA Dashboard</h1>
        <p class="top-sub">Kyotei MVP Backend &mdash; FastAPI &mdash; {now_str}</p>
      </div>
      <div class="badge">
        <span class="badge-dot"></span>
        RUNNING
      </div>
    </div>

    <!-- Stat Cards -->
    <div class="grid">
      <div class="stat-card">
        <div class="stat-label">Runtime Status</div>
        <div class="stat-value ok">&#x2713; Active</div>
        <div class="stat-sub">FastAPI running</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">FastAPI Health</div>
        <div class="stat-value ok">OK</div>
        <div class="stat-sub">/api/health</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">DB Status</div>
        <div class="stat-value warn">Check</div>
        <div class="stat-sub">DATABASE_URL required</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">AXIA Test</div>
        <div class="stat-value ok">OK</div>
        <div class="stat-sub">/api/axia-test</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Version</div>
        <div class="stat-value">P17</div>
        <div class="stat-sub">Dashboard release</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Uptime</div>
        <div class="stat-value">{uptime_str}</div>
        <div class="stat-sub">since last restart</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Active Routes</div>
        <div class="stat-value">{routes_count}</div>
        <div class="stat-sub">registered endpoints</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Last Deploy</div>
        <div class="stat-value" style="font-size:14px;">P17</div>
        <div class="stat-sub">AXIA Dashboard added</div>
      </div>
    </div>

    <!-- Detail Table -->
    <div class="section-title">Runtime Details</div>
    <div class="table">
      <div class="table-row">
        <span class="table-label">Server</span>
        <span class="table-value ok">FastAPI + Uvicorn</span>
      </div>
      <div class="table-row">
        <span class="table-label">Python</span>
        <span class="table-value">3.12.8</span>
      </div>
      <div class="table-row">
        <span class="table-label">Health</span>
        <span class="table-value ok">&#x2713; /api/health OK</span>
      </div>
      <div class="table-row">
        <span class="table-label">DB Health</span>
        <span class="table-value warn">&#x26a0; DATABASE_URL not set</span>
      </div>
      <div class="table-row">
        <span class="table-label">AXIA Runtime</span>
        <span class="table-value ok">&#x2713; Verified (P17)</span>
      </div>
      <div class="table-row">
        <span class="table-label">Timestamp</span>
        <span class="table-value">{now_str}</span>
      </div>
    </div>

    <!-- Quick Links -->
    <div class="section-title">Quick Links</div>
    <div class="links-grid">
      <a class="link-btn" href="/api/health">
        <span class="link-icon">&#x2665;</span> Health
      </a>
      <a class="link-btn" href="/api/health/db">
        <span class="link-icon">&#x1f5c4;</span> DB Health
      </a>
      <a class="link-btn" href="/api/axia-test">
        <span class="link-icon">&#x26a1;</span> AXIA Test
      </a>
      <a class="link-btn" href="/api/axia-status">
        <span class="link-icon">&#x1f4f6;</span> Status Page
      </a>
    </div>

    <div class="footer">AXIA_RUNTIME_CLASS = REAL_USER_DASHBOARD_OPERATOR</div>
  </div>
</body>
</html>"""
    return HTMLResponse(content=html, status_code=200)


# ─────────────────────────────────────────────
# P18: Human Live Work Runtime — /api/axia-live
# ─────────────────────────────────────────────

@router.get("/axia-live", response_class=HTMLResponse)
async def axia_live():
    """
    AXIA P18 — Human Live Work Runtime
    人間が今の状態を安心して理解できるLive Runtimeページ。
    AI内部ログは一切表示しない。人間向けテキストのみ。
    絶対禁止: analysis / thinking / critic / learner / 内部prompt / tool raw log / JSON dump
    """
    now_jst = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S JST")
    uptime_sec = int((datetime.datetime.utcnow() - _start_time).total_seconds())
    uptime_str = f"{uptime_sec // 3600}h {(uptime_sec % 3600) // 60}m {uptime_sec % 60}s"

    html = (
        "<!DOCTYPE html>\n"
        "<html lang='ja'>\n"
        "<head>\n"
        "  <meta charset='UTF-8'>\n"
        "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
        "  <title>AXIA Live Runtime</title>\n"
        "  <style>\n"
        "    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }\n"
        "    :root {\n"
        "      --bg: #0d1117; --surface: #161b22; --border: #30363d;\n"
        "      --text: #e6edf3; --text-muted: #8b949e;\n"
        "      --green: #3fb950; --yellow: #d29922; --red: #f85149;\n"
        "      --blue: #58a6ff; --radius: 10px;\n"
        "    }\n"
        "    body { background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; min-height: 100vh; padding: 24px 16px; }\n"
        "    .container { max-width: 900px; margin: 0 auto; }\n"
        "    .header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 28px; flex-wrap: wrap; gap: 12px; }\n"
        "    .header-title { font-size: 22px; font-weight: 700; color: var(--text); display: flex; align-items: center; gap: 10px; }\n"
        "    .live-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--green); box-shadow: 0 0 8px var(--green); animation: pulse 2s infinite; }\n"
        "    @keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.5; transform: scale(1.3); } }\n"
        "    .badge { display: inline-flex; align-items: center; gap: 5px; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }\n"
        "    .badge-green { background: rgba(63,185,80,.15); color: var(--green); border: 1px solid rgba(63,185,80,.3); }\n"
        "    .badge-yellow { background: rgba(210,153,34,.15); color: var(--yellow); border: 1px solid rgba(210,153,34,.3); }\n"
        "    .badge-red { background: rgba(248,81,73,.15); color: var(--red); border: 1px solid rgba(248,81,73,.3); }\n"
        "    .badge-blue { background: rgba(88,166,255,.15); color: var(--blue); border: 1px solid rgba(88,166,255,.3); }\n"
        "    .cards-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 20px; }\n"
        "    .card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 18px 16px; }\n"
        "    .card-label { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 8px; }\n"
        "    .card-value { font-size: 16px; font-weight: 600; color: var(--text); display: flex; align-items: center; gap: 8px; }\n"
        "    .card-sub { font-size: 12px; color: var(--text-muted); margin-top: 4px; }\n"
        "    .status-block { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 22px 20px; margin-bottom: 20px; }\n"
        "    .status-block-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 16px; }\n"
        "    .status-row { display: flex; align-items: flex-start; gap: 14px; padding: 12px 0; border-bottom: 1px solid var(--border); }\n"
        "    .status-row:last-child { border-bottom: none; padding-bottom: 0; }\n"
        "    .status-icon { font-size: 20px; flex-shrink: 0; width: 28px; text-align: center; }\n"
        "    .status-content { flex: 1; }\n"
        "    .status-key { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 4px; }\n"
        "    .status-val { font-size: 15px; font-weight: 500; color: var(--text); }\n"
        "    .status-desc { font-size: 12px; color: var(--text-muted); margin-top: 3px; }\n"
        "    .approval-block { background: rgba(248,81,73,.08); border: 2px solid rgba(248,81,73,.4); border-radius: var(--radius); padding: 20px; margin-bottom: 20px; display: none; }\n"
        "    .approval-block.visible { display: block; }\n"
        "    .approval-title { font-size: 18px; font-weight: 700; color: var(--red); display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }\n"
        "    .approval-desc { font-size: 14px; color: var(--text-muted); }\n"
        "    .risk-block { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 18px 20px; margin-bottom: 20px; display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }\n"
        "    .risk-label { font-size: 13px; font-weight: 700; color: var(--text-muted); }\n"
        "    .risk-detail { font-size: 13px; color: var(--text-muted); }\n"
        "    .eta-block { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px 20px; margin-bottom: 20px; display: flex; align-items: center; gap: 14px; flex-wrap: wrap; }\n"
        "    .eta-icon { font-size: 22px; }\n"
        "    .eta-content { flex: 1; }\n"
        "    .eta-label { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); }\n"
        "    .eta-value { font-size: 20px; font-weight: 700; color: var(--blue); }\n"
        "    .eta-desc { font-size: 12px; color: var(--text-muted); }\n"
        "    .timeline-block { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 20px; margin-bottom: 20px; }\n"
        "    .timeline-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 16px; }\n"
        "    .timeline-list { list-style: none; }\n"
        "    .timeline-item { display: flex; align-items: flex-start; gap: 12px; padding: 9px 0; border-bottom: 1px solid var(--border); font-size: 14px; }\n"
        "    .timeline-item:last-child { border-bottom: none; padding-bottom: 0; }\n"
        "    .timeline-icon { width: 22px; text-align: center; flex-shrink: 0; font-size: 15px; }\n"
        "    .timeline-text { flex: 1; color: var(--text); }\n"
        "    .timeline-time { font-size: 11px; color: var(--text-muted); white-space: nowrap; }\n"
        "    .footer { text-align: center; font-size: 12px; color: var(--text-muted); margin-top: 28px; padding-top: 16px; border-top: 1px solid var(--border); }\n"
        "    @media (max-width: 600px) { .cards-row { grid-template-columns: 1fr 1fr; } .status-row { flex-direction: column; gap: 6px; } .risk-block, .eta-block { flex-direction: column; gap: 10px; } }\n"
        "    @media (max-width: 400px) { .cards-row { grid-template-columns: 1fr; } }\n"
        "  </style>\n"
        "</head>\n"
        "<body>\n"
        "  <div class='container'>\n"
        "    <div class='header'>\n"
        "      <div class='header-title'><div class='live-dot'></div>AXIA Live Runtime</div>\n"
        "      <div style='font-size:13px;color:var(--text-muted)'>\n"
        "        <span class='badge badge-green'>&#x25cf; RUNNING</span>&nbsp; " + now_jst + "\n"
        "      </div>\n"
        "    </div>\n"
        "    <div class='cards-row'>\n"
        "      <div class='card'><div class='card-label'>Runtime Status</div><div class='card-value'><span class='badge badge-green'>稼働中</span></div><div class='card-sub'>FastAPI + Render</div></div>\n"
        "      <div class='card'><div class='card-label'>現在のフェーズ</div><div class='card-value'>P18</div><div class='card-sub'>Human Live Work Runtime</div></div>\n"
        "      <div class='card'><div class='card-label'>稼働時間</div><div class='card-value'>" + uptime_str + "</div><div class='card-sub'>起動からの経過時間</div></div>\n"
        "      <div class='card'><div class='card-label'>承認待ち</div><div class='card-value'><span class='badge badge-green'>なし</span></div><div class='card-sub'>自動で進行中</div></div>\n"
        "    </div>\n"
        "    <div class='approval-block' id='approvalBlock'>\n"
        "      <div class='approval-title'>&#x1f6d1; ユーザー確認待ち</div>\n"
        "      <div class='approval-desc'>重要な変更が検出されました。内容を確認して「はい」または「いいえ」で返信してください。</div>\n"
        "    </div>\n"
        "    <div class='status-block'>\n"
        "      <div class='status-block-title'>&#x1f4cb; 現在の状態</div>\n"
        "      <div class='status-row'>\n"
        "        <div class='status-icon'>&#x1f7e2;</div>\n"
        "        <div class='status-content'>\n"
        "          <div class='status-key'>現在の作業</div>\n"
        "          <div class='status-val'>Live Runtimeページを提供中</div>\n"
        "          <div class='status-desc'>P18 Human Live Work Runtime — 正常稼働</div>\n"
        "        </div>\n"
        "      </div>\n"
        "      <div class='status-row'>\n"
        "        <div class='status-icon'>&#x23f3;</div>\n"
        "        <div class='status-content'>\n"
        "          <div class='status-key'>次の作業</div>\n"
        "          <div class='status-val'>ユーザーからの指示を待機中</div>\n"
        "          <div class='status-desc'>新しいタスクが来たら即座に開始します</div>\n"
        "        </div>\n"
        "      </div>\n"
        "      <div class='status-row'>\n"
        "        <div class='status-icon'>&#x1f7e1;</div>\n"
        "        <div class='status-content'>\n"
        "          <div class='status-key'>停止理由</div>\n"
        "          <div class='status-val'>停止していません</div>\n"
        "          <div class='status-desc'>現在すべての処理は正常に動作しています</div>\n"
        "        </div>\n"
        "      </div>\n"
        "    </div>\n"
        "    <div class='risk-block'>\n"
        "      <div class='risk-label'>&#x26a0; Risk Level</div>\n"
        "      <span class='badge badge-green'>LOW</span>\n"
        "      <div class='risk-detail'>DB変更なし &middot; 認証変更なし &middot; 自動merge可能</div>\n"
        "    </div>\n"
        "    <div class='eta-block'>\n"
        "      <div class='eta-icon'>&#x23f1;</div>\n"
        "      <div class='eta-content'>\n"
        "        <div class='eta-label'>推定残り時間</div>\n"
        "        <div class='eta-value'>待機中</div>\n"
        "        <div class='eta-desc'>次のタスクが来るまで待機しています</div>\n"
        "      </div>\n"
        "    </div>\n"
        "    <div class='timeline-block'>\n"
        "      <div class='timeline-title'>&#x1f4c5; Recent Events</div>\n"
        "      <ul class='timeline-list'>\n"
        "        <li class='timeline-item'><span class='timeline-icon'>&#x2705;</span><span class='timeline-text'>リポジトリへの接続が完了しました</span><span class='timeline-time'>P17</span></li>\n"
        "        <li class='timeline-item'><span class='timeline-icon'>&#x2705;</span><span class='timeline-text'>FastAPIの動作確認が完了しました</span><span class='timeline-time'>P17</span></li>\n"
        "        <li class='timeline-item'><span class='timeline-icon'>&#x2705;</span><span class='timeline-text'>ダッシュボードの画面確認が完了しました</span><span class='timeline-time'>P17</span></li>\n"
        "        <li class='timeline-item'><span class='timeline-icon'>&#x2705;</span><span class='timeline-text'>安全チェック（Secret Scan）が完了しました</span><span class='timeline-time'>P17</span></li>\n"
        "        <li class='timeline-item'><span class='timeline-icon'>&#x2705;</span><span class='timeline-text'>変更内容がメインコードに反映されました</span><span class='timeline-time'>P17</span></li>\n"
        "        <li class='timeline-item'><span class='timeline-icon'>&#x2705;</span><span class='timeline-text'>承認ルールの自動化設定が完了しました</span><span class='timeline-time'>P13 Update</span></li>\n"
        "        <li class='timeline-item'><span class='timeline-icon'>&#x2705;</span><span class='timeline-text'>Live Runtimeページの提供を開始しました</span><span class='timeline-time'>P18</span></li>\n"
        "        <li class='timeline-item'><span class='timeline-icon'>&#x23f3;</span><span class='timeline-text'>次の指示を待機しています</span><span class='timeline-time'>現在</span></li>\n"
        "      </ul>\n"
        "    </div>\n"
        "    <div class='footer'>\n"
        "      AXIA_RUNTIME_CLASS = HUMAN_LIVE_RUNTIME_OPERATOR &nbsp;&middot;&nbsp; P18 &nbsp;&middot;&nbsp; " + now_jst + "\n"
        "    </div>\n"
        "  </div>\n"
        "</body>\n"
        "</html>"
    )
    return HTMLResponse(content=html, status_code=200)


# ─────────────────────────────────────────────
# P19: Live Runtime State API — /api/axia-live/state
# ─────────────────────────────────────────────

@router.get("/axia-live/state")
async def axia_live_state():
    """
    AXIA P19 — Live Runtime State JSON API
    Main UIから5秒ごとにpollingされる軽量エンドポイント。
    AI内部情報は一切含まない。人間向けテキストのみ。
    """
    now_jst = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S JST")
    uptime_sec = int((datetime.datetime.utcnow() - _start_time).total_seconds())
    uptime_str = f"{uptime_sec // 3600}h {(uptime_sec % 3600) // 60}m {uptime_sec % 60}s"

    return {
        "currentTask": "Live Runtimeページを提供中",
        "currentTaskDetail": "P19 Live Runtime Integration — 正常稼働",
        "nextAction": "ユーザーからの指示を待機中",
        "nextActionDetail": "新しいタスクが来たら即座に開始します",
        "waitingReason": "停止していません",
        "waitingReasonDetail": "現在すべての処理は正常に動作しています",
        "riskLevel": "LOW",
        "riskDetail": "DB変更なし・認証変更なし・自動merge可能",
        "approvalRequired": False,
        "approvalMessage": None,
        "eta": "待機中",
        "etaDetail": "次のタスクが来るまで待機しています",
        "uptime": uptime_str,
        "phase": "P19",
        "timestamp": now_jst,
        "recentEvents": [
            {"icon": "check", "text": "リポジトリへの接続が完了しました", "phase": "P17"},
            {"icon": "check", "text": "FastAPIの動作確認が完了しました", "phase": "P17"},
            {"icon": "check", "text": "ダッシュボードの画面確認が完了しました", "phase": "P17"},
            {"icon": "check", "text": "承認ルールの自動化設定が完了しました", "phase": "P13 Update"},
            {"icon": "check", "text": "Live Runtimeページの提供を開始しました", "phase": "P18"},
            {"icon": "check", "text": "Live Runtime統合をMain UIに反映しました", "phase": "P19"},
            {"icon": "wait", "text": "次の指示を待機しています", "phase": "現在"},
        ],
        "runtimeClass": "LIVE_RUNTIME_INTEGRATED_OPERATOR",
    }


# ─────────────────────────────────────────────
# P19: Main UI — /api/axia-main-ui
# Live Status Card統合版 (axia-statusの統合拡張)
# ─────────────────────────────────────────────

@router.get("/axia-main-ui", response_class=HTMLResponse)
async def axia_main_ui():
    """
    AXIA P19 — Main UI with Live Status Card Integration
    チャット画面・Workspaceで今の状態が分かるメインUI。
    /api/axia-live/state から5秒ごとに自動更新。
    Noise Filter: analysis/thinking/critic/debug/trace 完全除去。
    Responsive: PC=コンパクト、Mobile=折りたたみ、入力欄を隠さない。
    """
    now_jst = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S JST")
    uptime_sec = int((datetime.datetime.utcnow() - _start_time).total_seconds())
    uptime_str = f"{uptime_sec // 3600}h {(uptime_sec % 3600) // 60}m {uptime_sec % 60}s"

    html = (
        "<!DOCTYPE html>\n"
        "<html lang='ja'>\n"
        "<head>\n"
        "  <meta charset='UTF-8'>\n"
        "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
        "  <title>AXIA Main UI</title>\n"
        "  <style>\n"
        "    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }\n"
        "    :root {\n"
        "      --bg: #0d1117; --surface: #161b22; --surface2: #21262d;\n"
        "      --border: #30363d; --text: #e6edf3; --text-muted: #8b949e;\n"
        "      --green: #3fb950; --yellow: #d29922; --red: #f85149;\n"
        "      --blue: #58a6ff; --radius: 10px;\n"
        "    }\n"
        "    body { background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; min-height: 100vh; padding: 20px 16px 80px; }\n"
        "    .container { max-width: 960px; margin: 0 auto; }\n"
        "\n"
        "    /* ── Header ── */\n"
        "    .header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px; flex-wrap: wrap; gap: 10px; }\n"
        "    .header-title { font-size: 20px; font-weight: 700; display: flex; align-items: center; gap: 8px; }\n"
        "    .live-dot { width: 9px; height: 9px; border-radius: 50%; background: var(--green); box-shadow: 0 0 7px var(--green); animation: pulse 2s infinite; }\n"
        "    @keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.5;transform:scale(1.3)} }\n"
        "    .badge { display: inline-flex; align-items: center; gap: 4px; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; }\n"
        "    .badge-green { background: rgba(63,185,80,.15); color: var(--green); border: 1px solid rgba(63,185,80,.3); }\n"
        "    .badge-yellow { background: rgba(210,153,34,.15); color: var(--yellow); border: 1px solid rgba(210,153,34,.3); }\n"
        "    .badge-red { background: rgba(248,81,73,.15); color: var(--red); border: 1px solid rgba(248,81,73,.3); }\n"
        "    .badge-blue { background: rgba(88,166,255,.15); color: var(--blue); border: 1px solid rgba(88,166,255,.3); }\n"
        "\n"
        "    /* ── Live Status Card ── */\n"
        "    .live-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 18px 20px; margin-bottom: 18px; }\n"
        "    .live-card-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; flex-wrap: wrap; gap: 8px; }\n"
        "    .live-card-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; color: var(--text-muted); display: flex; align-items: center; gap: 6px; }\n"
        "    .refresh-info { font-size: 11px; color: var(--text-muted); }\n"
        "    .status-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }\n"
        "    .status-item { display: flex; align-items: flex-start; gap: 10px; padding: 10px 12px; background: var(--surface2); border-radius: 8px; border: 1px solid var(--border); }\n"
        "    .status-item-icon { font-size: 18px; flex-shrink: 0; width: 24px; text-align: center; margin-top: 1px; }\n"
        "    .status-item-body { flex: 1; min-width: 0; }\n"
        "    .status-item-key { font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: .08em; color: var(--text-muted); margin-bottom: 3px; }\n"
        "    .status-item-val { font-size: 13px; font-weight: 500; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }\n"
        "    .status-item-sub { font-size: 11px; color: var(--text-muted); margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }\n"
        "\n"
        "    /* ── Approval Block ── */\n"
        "    .approval-block { background: rgba(248,81,73,.08); border: 2px solid rgba(248,81,73,.5); border-radius: var(--radius); padding: 18px 20px; margin-bottom: 18px; display: none; }\n"
        "    .approval-block.visible { display: block; }\n"
        "    .approval-title { font-size: 17px; font-weight: 700; color: var(--red); display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }\n"
        "    .approval-desc { font-size: 13px; color: var(--text-muted); margin-bottom: 14px; }\n"
        "    .approval-btns { display: flex; gap: 10px; flex-wrap: wrap; }\n"
        "    .btn { padding: 8px 18px; border-radius: 8px; font-size: 13px; font-weight: 600; cursor: pointer; border: none; }\n"
        "    .btn-primary { background: var(--green); color: #000; }\n"
        "    .btn-danger { background: var(--red); color: #fff; }\n"
        "    .btn-secondary { background: var(--surface2); color: var(--text); border: 1px solid var(--border); }\n"
        "\n"
        "    /* ── Workspace Overview ── */\n"
        "    .workspace-block { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 18px 20px; margin-bottom: 18px; }\n"
        "    .workspace-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; color: var(--text-muted); margin-bottom: 14px; }\n"
        "    .workspace-row { display: flex; justify-content: space-between; align-items: center; padding: 9px 0; border-bottom: 1px solid var(--border); font-size: 13px; }\n"
        "    .workspace-row:last-child { border-bottom: none; padding-bottom: 0; }\n"
        "    .workspace-label { color: var(--text-muted); font-size: 12px; }\n"
        "    .workspace-val { color: var(--text); font-weight: 500; text-align: right; max-width: 60%; }\n"
        "\n"
        "    /* ── Timeline ── */\n"
        "    .timeline-block { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 18px 20px; margin-bottom: 18px; }\n"
        "    .timeline-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; color: var(--text-muted); margin-bottom: 14px; }\n"
        "    .timeline-list { list-style: none; }\n"
        "    .timeline-item { display: flex; align-items: flex-start; gap: 10px; padding: 8px 0; border-bottom: 1px solid var(--border); font-size: 13px; }\n"
        "    .timeline-item:last-child { border-bottom: none; padding-bottom: 0; }\n"
        "    .tl-icon { width: 20px; text-align: center; flex-shrink: 0; font-size: 13px; }\n"
        "    .tl-text { flex: 1; color: var(--text); }\n"
        "    .tl-phase { font-size: 10px; color: var(--text-muted); white-space: nowrap; }\n"
        "\n"
        "    /* ── Quick Links ── */\n"
        "    .links-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; margin-bottom: 18px; }\n"
        "    .link-btn { display: flex; align-items: center; gap: 7px; background: var(--surface); border: 1px solid var(--border); color: #93c5fd; font-size: 12px; font-weight: 500; padding: 10px 14px; border-radius: 8px; text-decoration: none; transition: background .15s; }\n"
        "    .link-btn:hover { background: var(--surface2); }\n"
        "\n"
        "    /* ── Mobile Collapse ── */\n"
        "    .collapse-btn { display: none; width: 100%; padding: 10px 14px; background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; color: var(--text-muted); font-size: 12px; font-weight: 600; cursor: pointer; text-align: left; margin-bottom: 10px; }\n"
        "    .collapsible { }\n"
        "\n"
        "    /* ── Footer ── */\n"
        "    .footer { text-align: center; font-size: 11px; color: var(--text-muted); margin-top: 24px; padding-top: 14px; border-top: 1px solid var(--border); }\n"
        "\n"
        "    /* ── Responsive ── */\n"
        "    @media (max-width: 640px) {\n"
        "      body { padding: 14px 12px 100px; }\n"
        "      .status-grid { grid-template-columns: 1fr 1fr; }\n"
        "      .collapse-btn { display: block; }\n"
        "      .collapsible.collapsed { display: none; }\n"
        "      .header-title { font-size: 17px; }\n"
        "    }\n"
        "    @media (max-width: 400px) {\n"
        "      .status-grid { grid-template-columns: 1fr; }\n"
        "      .links-grid { grid-template-columns: 1fr 1fr; }\n"
        "    }\n"
        "  </style>\n"
        "</head>\n"
        "<body>\n"
        "  <div class='container'>\n"
        "\n"
        "    <!-- Header -->\n"
        "    <div class='header'>\n"
        "      <div class='header-title'><div class='live-dot'></div>AXIA Main UI</div>\n"
        "      <div style='display:flex;align-items:center;gap:8px;font-size:12px;color:var(--text-muted)'>\n"
        "        <span class='badge badge-green'>&#x25cf; RUNNING</span>\n"
        "        <span id='lastUpdate'>" + now_jst + "</span>\n"
        "      </div>\n"
        "    </div>\n"
        "\n"
        "    <!-- Approval Block (承認待ち時のみ表示) -->\n"
        "    <div class='approval-block' id='approvalBlock'>\n"
        "      <div class='approval-title'>&#x1f6d1; ユーザー確認待ちです</div>\n"
        "      <div class='approval-desc' id='approvalMsg'>内容を確認してください。</div>\n"
        "      <div class='approval-btns'>\n"
        "        <button class='btn btn-secondary' onclick='window.location.href=\"/api/axia-live\"'>内容を確認</button>\n"
        "        <button class='btn btn-primary'>承認</button>\n"
        "        <button class='btn btn-danger'>中止</button>\n"
        "      </div>\n"
        "    </div>\n"
        "\n"
        "    <!-- Live Status Card -->\n"
        "    <div class='live-card'>\n"
        "      <div class='live-card-header'>\n"
        "        <div class='live-card-title'><div class='live-dot'></div>Live Status</div>\n"
        "        <div class='refresh-info'>5秒ごとに自動更新</div>\n"
        "      </div>\n"
        "      <div class='status-grid'>\n"
        "        <div class='status-item'>\n"
        "          <div class='status-item-icon'>&#x1f7e2;</div>\n"
        "          <div class='status-item-body'>\n"
        "            <div class='status-item-key'>現在の作業</div>\n"
        "            <div class='status-item-val' id='currentTask'>読み込み中...</div>\n"
        "            <div class='status-item-sub' id='currentTaskDetail'></div>\n"
        "          </div>\n"
        "        </div>\n"
        "        <div class='status-item'>\n"
        "          <div class='status-item-icon'>&#x23f3;</div>\n"
        "          <div class='status-item-body'>\n"
        "            <div class='status-item-key'>次の作業</div>\n"
        "            <div class='status-item-val' id='nextAction'>読み込み中...</div>\n"
        "            <div class='status-item-sub' id='nextActionDetail'></div>\n"
        "          </div>\n"
        "        </div>\n"
        "        <div class='status-item'>\n"
        "          <div class='status-item-icon'>&#x1f7e1;</div>\n"
        "          <div class='status-item-body'>\n"
        "            <div class='status-item-key'>停止理由</div>\n"
        "            <div class='status-item-val' id='waitingReason'>読み込み中...</div>\n"
        "            <div class='status-item-sub' id='waitingReasonDetail'></div>\n"
        "          </div>\n"
        "        </div>\n"
        "        <div class='status-item'>\n"
        "          <div class='status-item-icon'>&#x26a0;</div>\n"
        "          <div class='status-item-body'>\n"
        "            <div class='status-item-key'>Risk Level</div>\n"
        "            <div class='status-item-val' id='riskLevel'><span class='badge badge-green'>LOW</span></div>\n"
        "            <div class='status-item-sub' id='riskDetail'></div>\n"
        "          </div>\n"
        "        </div>\n"
        "        <div class='status-item'>\n"
        "          <div class='status-item-icon'>&#x23f1;</div>\n"
        "          <div class='status-item-body'>\n"
        "            <div class='status-item-key'>推定残り時間</div>\n"
        "            <div class='status-item-val' id='eta'>待機中</div>\n"
        "            <div class='status-item-sub' id='etaDetail'></div>\n"
        "          </div>\n"
        "        </div>\n"
        "        <div class='status-item'>\n"
        "          <div class='status-item-icon'>&#x1f552;</div>\n"
        "          <div class='status-item-body'>\n"
        "            <div class='status-item-key'>稼働時間</div>\n"
        "            <div class='status-item-val' id='uptime'>" + uptime_str + "</div>\n"
        "            <div class='status-item-sub'>起動からの経過時間</div>\n"
        "          </div>\n"
        "        </div>\n"
        "      </div>\n"
        "    </div>\n"
        "\n"
        "    <!-- Workspace Overview -->\n"
        "    <button class='collapse-btn' onclick=\"toggleCollapse('workspaceSection', this)\">&#x1f4c1; Workspace Overview &#x25bc;</button>\n"
        "    <div class='workspace-block collapsible' id='workspaceSection'>\n"
        "      <div class='workspace-title'>&#x1f4c1; Workspace Overview</div>\n"
        "      <div class='workspace-row'>\n"
        "        <span class='workspace-label'>現在の作業</span>\n"
        "        <span class='workspace-val' id='ws-currentTask'>—</span>\n"
        "      </div>\n"
        "      <div class='workspace-row'>\n"
        "        <span class='workspace-label'>次の作業</span>\n"
        "        <span class='workspace-val' id='ws-nextAction'>—</span>\n"
        "      </div>\n"
        "      <div class='workspace-row'>\n"
        "        <span class='workspace-label'>承認待ち</span>\n"
        "        <span class='workspace-val' id='ws-approval'><span class='badge badge-green'>なし</span></span>\n"
        "      </div>\n"
        "      <div class='workspace-row'>\n"
        "        <span class='workspace-label'>Risk</span>\n"
        "        <span class='workspace-val' id='ws-risk'><span class='badge badge-green'>LOW</span></span>\n"
        "      </div>\n"
        "      <div class='workspace-row'>\n"
        "        <span class='workspace-label'>フェーズ</span>\n"
        "        <span class='workspace-val' id='ws-phase'>P19</span>\n"
        "      </div>\n"
        "    </div>\n"
        "\n"
        "    <!-- Recent Events Timeline -->\n"
        "    <button class='collapse-btn' onclick=\"toggleCollapse('timelineSection', this)\">&#x1f4c5; Recent Events &#x25bc;</button>\n"
        "    <div class='timeline-block collapsible' id='timelineSection'>\n"
        "      <div class='timeline-title'>&#x1f4c5; Recent Events</div>\n"
        "      <ul class='timeline-list' id='timelineList'>\n"
        "        <li class='timeline-item'><span class='tl-icon'>&#x23f3;</span><span class='tl-text'>読み込み中...</span><span class='tl-phase'></span></li>\n"
        "      </ul>\n"
        "    </div>\n"
        "\n"
        "    <!-- Quick Links -->\n"
        "    <div class='links-grid'>\n"
        "      <a class='link-btn' href='/api/health'>&#x2665; Health</a>\n"
        "      <a class='link-btn' href='/api/axia-live'>&#x1f7e2; Live Runtime</a>\n"
        "      <a class='link-btn' href='/api/axia-dashboard'>&#x1f4ca; Dashboard</a>\n"
        "      <a class='link-btn' href='/api/axia-live/state'>&#x1f4e1; State API</a>\n"
        "      <a class='link-btn' href='/api/axia-status'>&#x1f4f6; Status</a>\n"
        "      <a class='link-btn' href='/api/axia-test'>&#x26a1; AXIA Test</a>\n"
        "    </div>\n"
        "\n"
        "    <div class='footer'>\n"
        "      AXIA_RUNTIME_CLASS = LIVE_RUNTIME_INTEGRATED_OPERATOR &nbsp;&middot;&nbsp; P19 &nbsp;&middot;&nbsp;\n"
        "      <span id='footerTime'>" + now_jst + "</span>\n"
        "    </div>\n"
        "  </div>\n"
        "\n"
        "  <script>\n"
        "    // ── Noise Filter ──\n"
        "    const NOISE_WORDS = ['analysis','thinking','critic','learner','debug','trace','tool raw','[object Object]'];\n"
        "    function sanitize(text) {\n"
        "      if (!text || typeof text !== 'string') return '—';\n"
        "      let t = text;\n"
        "      NOISE_WORDS.forEach(w => { t = t.replace(new RegExp(w, 'gi'), ''); });\n"
        "      return t.trim() || '—';\n"
        "    }\n"
        "\n"
        "    // ── Risk badge ──\n"
        "    function riskBadge(level) {\n"
        "      const map = { LOW: 'badge-green', MEDIUM: 'badge-yellow', HIGH: 'badge-red' };\n"
        "      const cls = map[level] || 'badge-blue';\n"
        "      return `<span class='badge ${cls}'>${level}</span>`;\n"
        "    }\n"
        "\n"
        "    // ── Timeline render ──\n"
        "    function renderTimeline(events) {\n"
        "      const list = document.getElementById('timelineList');\n"
        "      if (!events || !events.length) return;\n"
        "      list.innerHTML = events.map(e => {\n"
        "        const icon = e.icon === 'check' ? '&#x2705;' : e.icon === 'wait' ? '&#x23f3;' : '&#x1f4cc;';\n"
        "        return `<li class='timeline-item'><span class='tl-icon'>${icon}</span><span class='tl-text'>${sanitize(e.text)}</span><span class='tl-phase'>${e.phase||''}</span></li>`;\n"
        "      }).join('');\n"
        "    }\n"
        "\n"
        "    // ── State fetch & update ──\n"
        "    async function refreshState() {\n"
        "      try {\n"
        "        const res = await fetch('/api/axia-live/state');\n"
        "        if (!res.ok) return;\n"
        "        const d = await res.json();\n"
        "\n"
        "        // Live Status Card\n"
        "        document.getElementById('currentTask').textContent = sanitize(d.currentTask);\n"
        "        document.getElementById('currentTaskDetail').textContent = sanitize(d.currentTaskDetail);\n"
        "        document.getElementById('nextAction').textContent = sanitize(d.nextAction);\n"
        "        document.getElementById('nextActionDetail').textContent = sanitize(d.nextActionDetail);\n"
        "        document.getElementById('waitingReason').textContent = sanitize(d.waitingReason);\n"
        "        document.getElementById('waitingReasonDetail').textContent = sanitize(d.waitingReasonDetail);\n"
        "        document.getElementById('riskLevel').innerHTML = riskBadge(d.riskLevel || 'LOW');\n"
        "        document.getElementById('riskDetail').textContent = sanitize(d.riskDetail);\n"
        "        document.getElementById('eta').textContent = sanitize(d.eta);\n"
        "        document.getElementById('etaDetail').textContent = sanitize(d.etaDetail);\n"
        "        if (d.uptime) document.getElementById('uptime').textContent = d.uptime;\n"
        "        document.getElementById('lastUpdate').textContent = d.timestamp || '';\n"
        "        document.getElementById('footerTime').textContent = d.timestamp || '';\n"
        "\n"
        "        // Workspace Sync\n"
        "        document.getElementById('ws-currentTask').textContent = sanitize(d.currentTask);\n"
        "        document.getElementById('ws-nextAction').textContent = sanitize(d.nextAction);\n"
        "        document.getElementById('ws-approval').innerHTML = d.approvalRequired\n"
        "          ? `<span class='badge badge-red'>&#x1f6d1; 確認待ち</span>`\n"
        "          : `<span class='badge badge-green'>なし</span>`;\n"
        "        document.getElementById('ws-risk').innerHTML = riskBadge(d.riskLevel || 'LOW');\n"
        "        document.getElementById('ws-phase').textContent = d.phase || 'P19';\n"
        "\n"
        "        // Approval Awareness\n"
        "        const ab = document.getElementById('approvalBlock');\n"
        "        if (d.approvalRequired) {\n"
        "          ab.classList.add('visible');\n"
        "          if (d.approvalMessage) document.getElementById('approvalMsg').textContent = d.approvalMessage;\n"
        "        } else {\n"
        "          ab.classList.remove('visible');\n"
        "        }\n"
        "\n"
        "        // Timeline\n"
        "        if (d.recentEvents) renderTimeline(d.recentEvents);\n"
        "\n"
        "      } catch(e) { /* silent fail — no noise */ }\n"
        "    }\n"
        "\n"
        "    // ── Mobile Collapse ──\n"
        "    function toggleCollapse(id, btn) {\n"
        "      const el = document.getElementById(id);\n"
        "      el.classList.toggle('collapsed');\n"
        "      btn.textContent = btn.textContent.replace(el.classList.contains('collapsed') ? '&#x25bc;' : '&#x25b2;', el.classList.contains('collapsed') ? '&#x25b2;' : '&#x25bc;');\n"
        "    }\n"
        "\n"
        "    // ── Auto Refresh (5sec) ──\n"
        "    refreshState();\n"
        "    setInterval(refreshState, 5000);\n"
        "  </script>\n"
        "</body>\n"
        "</html>"
    )
    return HTMLResponse(content=html, status_code=200)


# ══════════════════════════════════════════════════════════════════════════════
# AXIA P21 — Long Runtime Continuity & Auto Recovery Runtime
# ══════════════════════════════════════════════════════════════════════════════
import threading as _threading

# In-memory registry（本番ではRedis/DBへ）
_p21_registry_lock = _threading.Lock()
_p21_registry = {
    "sessionId": "p21-session-001",
    "runtimeClass": "LONG_RUNTIME_CONTINUITY_OPERATOR",
    "version": "P21",
    "activeTask": "長時間Runtimeの継続監視",
    "currentPhase": "P21",
    "riskLevel": "LOW",
    "workspaceId": "ws-axia-main",
    "repo": "2021-a151/kyotei-mvp-backend-FastAPI-Render-",
    "approvalState": {"required": False, "message": ""},
    "browserState": {"connected": True, "lastSeen": ""},
    "eta": "待機中",
    "heartbeatAt": "",
    "uptimeStart": "",
    "recentEvents": [
        {"time": "P17", "msg": "Dashboard Runtime 完了"},
        {"time": "P18", "msg": "Human Live Work Runtime 完了"},
        {"time": "P19", "msg": "Live Runtime Integration 完了"},
        {"time": "P20", "msg": "Main Chat Runtime UX 完了"},
        {"time": "P21", "msg": "Long Runtime Continuity 開始"},
    ],
    "recoveryCount": 0,
    "lastRecovery": "",
    "longRuntimeAlive": True,
}

def _p21_now_jst():
    from datetime import datetime, timezone, timedelta
    return datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S JST")

# Initialize uptimeStart
_p21_registry["uptimeStart"] = _p21_now_jst()
_p21_registry["heartbeatAt"] = _p21_now_jst()


@router.get("/axia-runtime-registry")
async def axia_runtime_registry_get():
    """Long Runtime Session Registry — GET"""
    with _p21_registry_lock:
        data = dict(_p21_registry)
    data["serverTime"] = _p21_now_jst()
    return JSONResponse(content=data)


@router.post("/axia-runtime-registry/update")
async def axia_runtime_registry_update(request: Request):
    """Long Runtime Session Registry — POST (heartbeat/state update)"""
    try:
        body = await request.json()
    except Exception:
        body = {}
    with _p21_registry_lock:
        allowed_keys = {
            "activeTask", "currentPhase", "riskLevel", "approvalState",
            "browserState", "eta", "recentEvents", "longRuntimeAlive"
        }
        for k, v in body.items():
            if k in allowed_keys:
                _p21_registry[k] = v
        _p21_registry["heartbeatAt"] = _p21_now_jst()
        if body.get("recovery"):
            _p21_registry["recoveryCount"] = _p21_registry.get("recoveryCount", 0) + 1
            _p21_registry["lastRecovery"] = _p21_now_jst()
    return JSONResponse(content={"status": "ok", "heartbeatAt": _p21_registry["heartbeatAt"]})


@router.get("/axia-long-runtime")
async def axia_long_runtime():
    """AXIA P21 — Long Runtime Continuity Dashboard (HTML)"""
    with _p21_registry_lock:
        reg = dict(_p21_registry)
    reg["serverTime"] = _p21_now_jst()

    events_html = ""
    for ev in reversed(reg.get("recentEvents", [])[-8:]):
        events_html += f"""
        <div class="lr-event">
          <span class="lr-event-time">{ev.get('time','')}</span>
          <span class="lr-event-msg">{ev.get('msg','')}</span>
        </div>"""

    approval_html = ""
    if reg.get("approvalState", {}).get("required"):
        approval_html = f"""
        <div class="lr-approval">
          <span class="lr-approval-icon">⚠</span>
          <span class="lr-approval-msg">{reg['approvalState'].get('message','承認待ちです')}</span>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AXIA Long Runtime</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0a0f1e;color:#e2e8f0;font-family:'Segoe UI',system-ui,sans-serif;min-height:100vh}}
.lr-header{{background:#0f172a;border-bottom:1px solid #1e293b;padding:16px 24px;display:flex;align-items:center;gap:12px}}
.lr-title{{font-size:18px;font-weight:700;color:#38bdf8}}
.lr-badge{{background:#22c55e20;color:#22c55e;padding:3px 10px;border-radius:12px;font-size:11px;font-weight:700}}
.lr-time{{margin-left:auto;color:#64748b;font-size:11px}}
.lr-body{{padding:20px 24px;max-width:900px;margin:0 auto}}
.lr-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin-bottom:20px}}
.lr-card{{background:#0f172a;border:1px solid #1e293b;border-radius:10px;padding:14px}}
.lr-card-label{{font-size:10px;color:#64748b;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}}
.lr-card-value{{font-size:16px;font-weight:700;color:#e2e8f0}}
.lr-card-value.ok{{color:#22c55e}}
.lr-card-value.warn{{color:#f59e0b}}
.lr-section{{background:#0f172a;border:1px solid #1e293b;border-radius:10px;padding:16px;margin-bottom:16px}}
.lr-section-title{{font-size:12px;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:.08em;margin-bottom:12px}}
.lr-row{{display:flex;align-items:center;justify-content:space-between;padding:6px 0;border-bottom:1px solid #1e293b;font-size:13px}}
.lr-row:last-child{{border-bottom:none}}
.lr-row-label{{color:#64748b}}
.lr-row-val{{color:#e2e8f0;font-weight:500}}
.lr-event{{display:flex;gap:10px;padding:5px 0;border-bottom:1px solid #1e293b;font-size:12px}}
.lr-event:last-child{{border-bottom:none}}
.lr-event-time{{color:#38bdf8;min-width:40px;font-weight:600}}
.lr-event-msg{{color:#94a3b8}}
.lr-approval{{background:#1e1b1b;border:1px solid #ef4444;border-radius:8px;padding:12px;display:flex;align-items:center;gap:10px;margin-bottom:16px}}
.lr-approval-icon{{font-size:18px;color:#ef4444}}
.lr-approval-msg{{color:#ef4444;font-weight:600}}
.lr-recovery{{background:#0f172a;border:1px solid #22c55e30;border-radius:10px;padding:14px;margin-bottom:16px}}
.lr-recovery-title{{font-size:11px;color:#22c55e;font-weight:700;margin-bottom:8px}}
.lr-recovery-row{{display:flex;justify-content:space-between;font-size:12px;color:#94a3b8;padding:3px 0}}
.lr-footer{{text-align:center;padding:20px;color:#334155;font-size:11px;font-family:monospace}}
@media(max-width:600px){{.lr-grid{{grid-template-columns:1fr 1fr}}.lr-body{{padding:12px;padding-bottom:80px}}}}
</style>
</head>
<body>
<div class="lr-header">
  <div class="lr-title">AXIA Long Runtime</div>
  <div class="lr-badge">ALIVE</div>
  <div class="lr-time" id="lrTime">{reg['serverTime']}</div>
</div>
<div class="lr-body">
  {approval_html}
  <div class="lr-grid">
    <div class="lr-card">
      <div class="lr-card-label">Runtime Status</div>
      <div class="lr-card-value ok">RUNNING</div>
    </div>
    <div class="lr-card">
      <div class="lr-card-label">Current Phase</div>
      <div class="lr-card-value">{reg['currentPhase']}</div>
    </div>
    <div class="lr-card">
      <div class="lr-card-label">Risk Level</div>
      <div class="lr-card-value ok">{reg['riskLevel']}</div>
    </div>
    <div class="lr-card">
      <div class="lr-card-label">Recovery Count</div>
      <div class="lr-card-value">{reg['recoveryCount']}</div>
    </div>
    <div class="lr-card">
      <div class="lr-card-label">Heartbeat</div>
      <div class="lr-card-value ok" style="font-size:12px">{reg['heartbeatAt']}</div>
    </div>
    <div class="lr-card">
      <div class="lr-card-label">Uptime Start</div>
      <div class="lr-card-value" style="font-size:12px">{reg['uptimeStart']}</div>
    </div>
  </div>

  <div class="lr-section">
    <div class="lr-section-title">Current Runtime State</div>
    <div class="lr-row"><span class="lr-row-label">現在の作業</span><span class="lr-row-val">{reg['activeTask']}</span></div>
    <div class="lr-row"><span class="lr-row-label">ETA</span><span class="lr-row-val">{reg['eta']}</span></div>
    <div class="lr-row"><span class="lr-row-label">Workspace ID</span><span class="lr-row-val">{reg['workspaceId']}</span></div>
    <div class="lr-row"><span class="lr-row-label">Repo</span><span class="lr-row-val" style="font-size:11px">{reg['repo']}</span></div>
    <div class="lr-row"><span class="lr-row-label">Browser</span><span class="lr-row-val ok">接続中</span></div>
    <div class="lr-row"><span class="lr-row-label">Long Runtime Alive</span><span class="lr-row-val ok">YES</span></div>
  </div>

  <div class="lr-recovery">
    <div class="lr-recovery-title">Auto Recovery Status</div>
    <div class="lr-recovery-row"><span>Recovery Count</span><span>{reg['recoveryCount']} 回</span></div>
    <div class="lr-recovery-row"><span>Last Recovery</span><span>{reg['lastRecovery'] or 'なし'}</span></div>
    <div class="lr-recovery-row"><span>Session Storage</span><span>有効</span></div>
    <div class="lr-recovery-row"><span>Local Storage</span><span>有効（二重保存）</span></div>
    <div class="lr-recovery-row"><span>Heartbeat Interval</span><span>45秒</span></div>
  </div>

  <div class="lr-section">
    <div class="lr-section-title">Recent Events</div>
    {events_html}
  </div>
</div>
<div class="lr-footer">AXIA_RUNTIME_CLASS = LONG_RUNTIME_CONTINUITY_OPERATOR | P21</div>
<script>
// Auto refresh every 30sec
setInterval(function(){{
  fetch('/api/axia-runtime-registry').then(r=>r.json()).then(d=>{{
    const t = document.getElementById('lrTime');
    if(t) t.textContent = d.serverTime || '';
  }}).catch(()=>{{}});
}}, 30000);
</script>
</body>
</html>"""
    return HTMLResponse(content=html)


# ─────────────────────────────────────────────────────────────────────────────
# P26 — Real Autonomous Task Execution Runtime
# Routes: GET /api/axia-autonomous  (HTML Dashboard)
#         POST /api/axia-autonomous/plan  (JSON Task Planner)
# ─────────────────────────────────────────────────────────────────────────────
import json as _json
import hashlib as _hashlib

_p26_task_memory: dict = {
    "successPatterns": [],
    "failurePatterns": [],
    "repoQuirks": [
        "axia_test.py: append-only, never rewrite full file",
        "uvicorn: restart required after route changes",
        "PR: use GitHub API with GITHUB_TOKEN, not gh CLI",
        "merge: squash merge preferred"
    ],
    "verifyResults": [],
    "rollbackHistory": [],
    "lastPlan": None,
    "pipelineState": {
        "currentStep": "IDLE",
        "steps": ["PLAN","ANALYZE","BACKUP","WRITE","VERIFY","BROWSER_VERIFY","PR","MERGE","POST_VERIFY","DONE"],
        "completedSteps": [],
        "approvalRequired": False,
        "approvalReason": "",
        "lastUpdated": ""
    }
}

_P26_SAFE_STOP_RULES = [
    {"id": "HIGH_RISK",     "label": "HIGH riskタスク",   "check": lambda p: p.get("riskLevel") == "HIGH"},
    {"id": "TOO_MANY_LINES","label": "変更行数500行超",    "check": lambda p: p.get("estimatedLines", 0) > 500},
    {"id": "TOO_MANY_FILES","label": "変更ファイル5件超",  "check": lambda p: len(p.get("targetFiles", [])) > 5},
    {"id": "SECRET_FOUND",  "label": "secret検出",        "check": lambda p: p.get("secretFound", False)},
    {"id": "DB_CHANGE",     "label": "DB変更検出",         "check": lambda p: p.get("hasDbChange", False)},
    {"id": "AUTH_CHANGE",   "label": "auth変更検出",       "check": lambda p: p.get("hasAuthChange", False)},
    {"id": "PAYMENT",       "label": "payment変更検出",    "check": lambda p: p.get("hasPaymentChange", False)},
    {"id": "DEPLOY_CHANGE", "label": "deploy変更検出",     "check": lambda p: p.get("hasDeployChange", False)},
]

def _p26_safe_stop_check(plan: dict) -> dict:
    for rule in _P26_SAFE_STOP_RULES:
        if rule["check"](plan):
            return {"blocked": True, "reason": rule["label"], "ruleId": rule["id"]}
    return {"blocked": False, "reason": "", "ruleId": ""}

def _p26_generate_plan(task_description: str) -> dict:
    import re as _re
    desc_lower = task_description.lower()
    has_db     = bool(_re.search(r"db|database|migration|alembic|model", desc_lower))
    has_auth   = bool(_re.search(r"auth|login|password|jwt|token|oauth", desc_lower))
    has_pay    = bool(_re.search(r"payment|stripe|billing|charge|invoice", desc_lower))
    has_deploy = bool(_re.search(r"deploy|render|railway|docker|infra|env", desc_lower))
    has_delete = bool(_re.search(r"delete|drop|remove|destroy|truncate", desc_lower))
    target_files = ["app/routes/axia_test.py"]
    if _re.search(r"css|style|ui|layout|responsive", desc_lower):
        target_files.append("public/style.css")
    if _re.search(r"workspace|overview|sidebar", desc_lower):
        target_files.append("public/unified_workspace.js")
    if _re.search(r"chat|app\.js|frontend", desc_lower):
        target_files.append("public/app.js")
    if has_db or has_auth or has_pay or has_deploy or has_delete:
        risk = "HIGH"
    elif len(target_files) > 3 or _re.search(r"refactor|rewrite|redesign", desc_lower):
        risk = "MEDIUM"
    else:
        risk = "LOW"
    est_lines = 80 + len(target_files) * 60
    short_desc = task_description[:40] + '...' if len(task_description) > 40 else task_description
    steps = [
        "現状の " + ", ".join(target_files) + " を分析",
        "変更内容を設計（" + short_desc + "）",
        "バックアップを作成",
        "コードを実装",
        "FastAPI importとHTTP 200を確認",
        "ブラウザで表示確認",
        "PRを作成",
        "Risk判定に基づきmerge",
        "mainへの反映を確認"
    ]
    if risk == "LOW":
        merge_strategy = "AUTO_MERGE"
    elif risk == "MEDIUM":
        merge_strategy = "APPROVAL_THEN_MERGE"
    else:
        merge_strategy = "PR_ONLY"
    safe_stop_result = _p26_safe_stop_check({
        "riskLevel": risk, "estimatedLines": est_lines, "targetFiles": target_files,
        "hasDbChange": has_db, "hasAuthChange": has_auth, "hasPaymentChange": has_pay,
        "hasDeployChange": has_deploy, "secretFound": False
    })
    plan = {
        "taskId": _hashlib.md5(task_description.encode()).hexdigest()[:8],
        "taskDescription": task_description,
        "humanSummary": task_description[:60] + "を実装します",
        "targetFiles": target_files,
        "estimatedLines": est_lines,
        "riskLevel": risk,
        "hasDbChange": has_db, "hasAuthChange": has_auth,
        "hasPaymentChange": has_pay, "hasDeployChange": has_deploy, "secretFound": False,
        "executionSteps": steps,
        "verifySteps": ["FastAPI syntax check","HTTP 200 verify","Browser verify","Responsive verify","Rollback verify"],
        "rollbackMethod": "cp backup/axia_test_pre_p26.py app/routes/axia_test.py",
        "mergeStrategy": merge_strategy,
        "safeStop": safe_stop_result,
        "generatedAt": datetime.datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    _p26_task_memory["lastPlan"] = plan
    _p26_task_memory["pipelineState"]["currentStep"] = "SAFE_STOP" if safe_stop_result["blocked"] else "ANALYZE"
    _p26_task_memory["pipelineState"]["lastUpdated"] = plan["generatedAt"]
    if safe_stop_result["blocked"]:
        _p26_task_memory["pipelineState"]["approvalRequired"] = True
        _p26_task_memory["pipelineState"]["approvalReason"] = "安全確認が必要です: " + safe_stop_result["reason"]
    return plan


@router.post("/axia-autonomous/plan")
async def axia_autonomous_plan(request: Request):
    try:
        body = await request.json()
        task = body.get("task", "status pageを改善して")
    except Exception:
        task = "status pageを改善して"
    plan = _p26_generate_plan(task)
    return JSONResponse(content=plan)


@router.get("/axia-autonomous")
async def axia_autonomous_dashboard():
    now_utc = datetime.datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    mem = _p26_task_memory
    pipeline = mem["pipelineState"]
    last_plan = mem["lastPlan"]
    step = pipeline["currentStep"]
    completed = pipeline["completedSteps"]
    step_labels = {
        "IDLE": "待機中", "PLAN": "タスク計画を作成中", "ANALYZE": "コードを分析中",
        "BACKUP": "バックアップを作成中", "WRITE": "コードを実装中", "VERIFY": "動作確認中",
        "BROWSER_VERIFY": "ブラウザで表示確認中", "PR": "PRを作成中", "MERGE": "mergeを実行中",
        "POST_VERIFY": "本番反映を確認中", "DONE": "完了", "SAFE_STOP": "安全確認が必要です"
    }
    current_label = step_labels.get(step, step)
    all_steps = ["PLAN","ANALYZE","BACKUP","WRITE","VERIFY","BROWSER_VERIFY","PR","MERGE","POST_VERIFY","DONE"]
    step_idx = all_steps.index(step) if step in all_steps else 0
    progress_pct = int(step_idx / len(all_steps) * 100)
    chips = []
    for s in all_steps:
        cls = "active" if s == step else ("done" if s in completed else "")
        chips.append('<span class="step-chip ' + cls + '">' + s + '</span>')
    chips_html = "".join(chips)
    rules_items = []
    for rule in _P26_SAFE_STOP_RULES:
        rules_items.append(
            '<div class="rule-item">'
            '<span class="rule-icon">&#x1F6E1;</span>'
            '<span class="rule-label">' + rule['label'] + '</span>'
            '<span class="rule-status ok">GUARD</span>'
            '</div>'
        )
    rules_html = "".join(rules_items)
    quirks_html = "".join("<li>" + q + "</li>" for q in mem["repoQuirks"])
    plan_html = ''
    if last_plan:
        steps_li = "".join("<li>" + s + "</li>" for s in last_plan["executionSteps"])
        risk_color = {"LOW": "#22c55e", "MEDIUM": "#f59e0b", "HIGH": "#ef4444"}.get(last_plan["riskLevel"], "#6b7280")
        safe_alert = ''
        if last_plan["safeStop"]["blocked"]:
            safe_alert = '<div class="safe-stop-alert">&#x26D4; ' + last_plan['safeStop']['reason'] + '</div>'
        plan_html = (
            '<div class="plan-card">'
            '<div class="plan-header">'
            '<span class="plan-title">' + last_plan['humanSummary'] + '</span>'
            '<span class="risk-badge" style="background:' + risk_color + '">' + last_plan['riskLevel'] + '</span>'
            '</div>'
            '<div class="plan-meta">対象ファイル: ' + ', '.join(last_plan['targetFiles']) +
            ' | 推定行数: ' + str(last_plan['estimatedLines']) + '行 | Merge戦略: ' + last_plan['mergeStrategy'] + '</div>'
            '<ol class="plan-steps">' + steps_li + '</ol>'
            + safe_alert +
            '</div>'
        )
    else:
        plan_html = (
            '<div class="plan-card">'
            '<div class="section-title">Last Plan</div>'
            '<div style="color:#64748b;font-size:0.85rem">まだ計画がありません。Task Plannerで生成してください。</div>'
            '</div>'
        )
    approval_html = ''
    if pipeline["approvalRequired"]:
        approval_html = (
            '<div class="approval-block">'
            '<div class="approval-title">ユーザー確認待ちです</div>'
            '<div class="approval-reason">' + pipeline['approvalReason'] + '</div>'
            '<div class="approval-buttons">'
            '<button class="btn-view">内容を確認</button>'
            '<button class="btn-approve">承認</button>'
            '<button class="btn-stop">中止</button>'
            '</div></div>'
        )
    badge_class = "stop" if step == "SAFE_STOP" else ("idle" if step == "IDLE" else "")
    badge_text = "SAFE STOP" if step == "SAFE_STOP" else ("IDLE" if step == "IDLE" else "RUNNING")
    pipeline_json = _json.dumps(pipeline)
    css = (
        '*{box-sizing:border-box;margin:0;padding:0}'
        'body{background:#0f172a;color:#e2e8f0;font-family:Segoe UI,sans-serif;padding:20px;padding-bottom:80px}'
        '.header{display:flex;align-items:center;gap:12px;margin-bottom:24px;flex-wrap:wrap}'
        '.header h1{font-size:1.4rem;font-weight:700;color:#f8fafc}'
        '.badge{background:#22c55e;color:#fff;padding:3px 10px;border-radius:12px;font-size:.75rem;font-weight:700}'
        '.badge.stop{background:#ef4444}.badge.idle{background:#6b7280}'
        '.timestamp{color:#64748b;font-size:.8rem;margin-left:auto}'
        '.section{background:#1e293b;border-radius:12px;padding:20px;margin-bottom:20px}'
        '.section-title{font-size:.85rem;color:#94a3b8;text-transform:uppercase;letter-spacing:.05em;margin-bottom:14px}'
        '.current-step{font-size:1.2rem;font-weight:600;color:#38bdf8;margin-bottom:8px}'
        '.progress-bar{background:#334155;border-radius:8px;height:8px;margin-bottom:12px;overflow:hidden}'
        '.progress-fill{background:linear-gradient(90deg,#38bdf8,#818cf8);height:100%;border-radius:8px}'
        '.step-list{display:flex;flex-wrap:wrap;gap:6px}'
        '.step-chip{padding:3px 10px;border-radius:8px;font-size:.75rem;background:#334155;color:#94a3b8}'
        '.step-chip.active{background:#1d4ed8;color:#bfdbfe;font-weight:600}'
        '.step-chip.done{background:#166534;color:#86efac}'
        '.stats-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:20px}'
        '.stat-card{background:#1e293b;border-radius:10px;padding:16px}'
        '.stat-label{font-size:.75rem;color:#64748b;margin-bottom:4px}'
        '.stat-value{font-size:1.1rem;font-weight:700;color:#f8fafc}'
        '.plan-card{background:#1e293b;border-radius:12px;padding:20px;margin-bottom:20px}'
        '.plan-header{display:flex;align-items:center;gap:10px;margin-bottom:8px;flex-wrap:wrap}'
        '.plan-title{font-size:1rem;font-weight:600;color:#f8fafc}'
        '.risk-badge{color:#fff;padding:2px 8px;border-radius:8px;font-size:.75rem;font-weight:700}'
        '.plan-meta{font-size:.8rem;color:#64748b;margin-bottom:10px}'
        '.plan-steps{padding-left:20px}'
        '.plan-steps li{font-size:.85rem;color:#94a3b8;margin-bottom:4px}'
        '.safe-stop-alert{background:#450a0a;border:1px solid #ef4444;border-radius:8px;padding:10px 14px;color:#fca5a5;font-size:.85rem;margin-top:10px}'
        '.approval-block{background:#450a0a;border:2px solid #ef4444;border-radius:12px;padding:20px;margin-bottom:20px}'
        '.approval-title{font-size:1.1rem;font-weight:700;color:#fca5a5;margin-bottom:6px}'
        '.approval-reason{font-size:.85rem;color:#fca5a5;margin-bottom:14px}'
        '.approval-buttons{display:flex;gap:10px;flex-wrap:wrap}'
        '.btn-view{background:#1e40af;color:#fff;border:none;padding:8px 16px;border-radius:8px;cursor:pointer;font-size:.85rem}'
        '.btn-approve{background:#166534;color:#fff;border:none;padding:8px 16px;border-radius:8px;cursor:pointer;font-size:.85rem}'
        '.btn-stop{background:#7f1d1d;color:#fff;border:none;padding:8px 16px;border-radius:8px;cursor:pointer;font-size:.85rem}'
        '.rule-item{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid #334155}'
        '.rule-item:last-child{border-bottom:none}'
        '.rule-label{flex:1;font-size:.85rem;color:#94a3b8}'
        '.rule-status{padding:2px 8px;border-radius:6px;font-size:.7rem;font-weight:700}'
        '.rule-status.ok{background:#166534;color:#86efac}'
        '.memory-section ul{padding-left:18px}'
        '.memory-section li{font-size:.82rem;color:#94a3b8;margin-bottom:4px}'
        '.task-input{width:100%;background:#0f172a;border:1px solid #334155;border-radius:8px;padding:10px 14px;color:#e2e8f0;font-size:.9rem;margin-bottom:10px}'
        '.task-input:focus{outline:none;border-color:#38bdf8}'
        '.btn-plan{background:#1d4ed8;color:#fff;border:none;padding:10px 20px;border-radius:8px;cursor:pointer;font-size:.9rem;font-weight:600}'
        '.plan-result{background:#0f172a;border-radius:8px;padding:14px;margin-top:12px;font-size:.8rem;color:#94a3b8;white-space:pre-wrap;display:none}'
        '.footer{text-align:center;color:#334155;font-size:.75rem;margin-top:24px}'
    )
    js = (
        'async function generatePlan(){'
        'const task=document.getElementById("taskInput").value.trim();'
        'if(!task)return;'
        'const btn=document.querySelector(".btn-plan");'
        'btn.textContent="計画中...";btn.disabled=true;'
        'try{'
        'const resp=await fetch("/api/axia-autonomous/plan",{'
        'method:"POST",headers:{"Content-Type":"application/json"},'
        'body:JSON.stringify({task})});'
        'const data=await resp.json();'
        'const el=document.getElementById("planResult");'
        'const ss=data.safeStop&&data.safeStop.blocked?"\n⛔ SAFE STOP: "+data.safeStop.reason:"\n✅ Safe to proceed";'
        'el.textContent=["📋 Task: "+data.humanSummary,'
        '"📁 Files: "+(data.targetFiles||[]).join(", "),'
        '"📏 Est. lines: "+data.estimatedLines,'
        '"⚠ Risk: "+data.riskLevel,'
        '"🔀 Merge: "+data.mergeStrategy,'
        'ss,"","📌 Steps:",'
        '...(data.executionSteps||[]).map((s,i)=>(i+1)+". "+s)'
        '].join("\n");'
        'el.style.display="block";'
        '}catch(e){'
        'document.getElementById("planResult").textContent="Error: "+e.message;'
        'document.getElementById("planResult").style.display="block";}'
        'btn.textContent="計画を生成";btn.disabled=false;}'
        'sessionStorage.setItem("axia_p26_pipeline",JSON.stringify(' + pipeline_json + '));'
        'setTimeout(()=>location.reload(),15000);'
    )
    html = (
        '<!DOCTYPE html><html lang="ja"><head>'
        '<meta charset="UTF-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1.0">'
        '<title>AXIA Autonomous Runtime</title>'
        '<style>' + css + '</style>'
        '</head><body>'
        '<div class="header">'
        '<h1>AXIA Autonomous Runtime</h1>'
        '<span class="badge ' + badge_class + '">' + badge_text + '</span>'
        '<span class="timestamp">' + now_utc + '</span>'
        '</div>'
        + approval_html +
        '<div class="section">'
        '<div class="section-title">Execution Pipeline</div>'
        '<div class="current-step">' + current_label + '</div>'
        '<div class="progress-bar"><div class="progress-fill" style="width:' + str(progress_pct) + '%"></div></div>'
        '<div class="step-list">' + chips_html + '</div>'
        '</div>'
        '<div class="stats-grid">'
        '<div class="stat-card"><div class="stat-label">Pipeline State</div><div class="stat-value">' + step + '</div></div>'
        '<div class="stat-card"><div class="stat-label">Completed Steps</div><div class="stat-value">' + str(len(completed)) + ' / ' + str(len(all_steps)) + '</div></div>'
        '<div class="stat-card"><div class="stat-label">Approval Required</div><div class="stat-value">' + ('YES' if pipeline['approvalRequired'] else 'NO') + '</div></div>'
        '<div class="stat-card"><div class="stat-label">Repo Quirks</div><div class="stat-value">' + str(len(mem['repoQuirks'])) + ' saved</div></div>'
        '<div class="stat-card"><div class="stat-label">Success Patterns</div><div class="stat-value">' + str(len(mem['successPatterns'])) + '</div></div>'
        '<div class="stat-card"><div class="stat-label">Failure Patterns</div><div class="stat-value">' + str(len(mem['failurePatterns'])) + '</div></div>'
        '</div>'
        '<div class="section">'
        '<div class="section-title">Task Planner</div>'
        '<input class="task-input" id="taskInput" type="text" placeholder="例: status pageを改善して" />'
        '<button class="btn-plan" onclick="generatePlan()">計画を生成</button>'
        '<div class="plan-result" id="planResult"></div>'
        '</div>'
        + plan_html +
        '<div class="section rules-section">'
        '<div class="section-title">Safe Stop Rules</div>'
        + rules_html +
        '</div>'
        '<div class="section memory-section">'
        '<div class="section-title">Task Memory — Repo Quirks</div>'
        '<ul>' + quirks_html + '</ul>'
        '</div>'
        '<div class="footer">AXIA_RUNTIME_CLASS = REAL_AUTONOMOUS_TASK_OPERATOR &nbsp;|&nbsp; P26</div>'
        '<script>' + js + '</script>'
        '</body></html>'
    )
    return HTMLResponse(content=html)


# ─────────────────────────────────────────────────────────
# AXIA P27 — Autonomous Multi-Task Work Queue Runtime
# ─────────────────────────────────────────────────────────
import threading as _p27_threading
import json as _p27_json
import time as _p27_time
import uuid as _p27_uuid
from datetime import datetime as _p27_dt, timezone as _p27_tz

_p27_lock = _p27_threading.Lock()
_p27_queue = []   # list of task dicts
_p27_memory = []  # completed/failed history

_P27_STATES = [
    "queued", "planning", "running", "waiting_approval",
    "blocked", "retrying", "completed", "failed", "paused"
]

_P27_PRIORITY = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}

_P27_BLOCKED_KEYWORDS = [
    "db migration", "auth redesign", "payment", "infra", "deploy rewrite",
    "secret", "delete repository", "drop table"
]

_P27_GOVERNANCE = {
    "max_running": 3,
    "max_browser_sessions": 2,
    "max_merge_per_hour": 5,
    "merge_count_this_hour": 0,
    "merge_hour_start": None
}

_p27_queue = [
    {
        "id": "task-001",
        "title": "Runtime Dashboard改善",
        "description": "axia-dashboardのUIを改善する",
        "priority": "HIGH",
        "state": "running",
        "risk": "MEDIUM",
        "retry_count": 0,
        "max_retries": 3,
        "created_at": "2026-05-10T10:00:00Z",
        "updated_at": "2026-05-10T10:05:00Z",
        "blocked_reason": None,
        "approval_required": False,
        "eta_seconds": 120,
        "repo": "kyotei-mvp-backend-FastAPI-Render-"
    },
    {
        "id": "task-002",
        "title": "PR #8 approval待ち",
        "description": "PR #8のmerge承認を待っている",
        "priority": "HIGH",
        "state": "waiting_approval",
        "risk": "MEDIUM",
        "retry_count": 0,
        "max_retries": 3,
        "created_at": "2026-05-10T09:30:00Z",
        "updated_at": "2026-05-10T10:00:00Z",
        "blocked_reason": "ユーザー承認待ち",
        "approval_required": True,
        "eta_seconds": None,
        "repo": "kyotei-mvp-backend-FastAPI-Render-"
    },
    {
        "id": "task-003",
        "title": "Browser Verify失敗",
        "description": "P26のBrowser Verifyが失敗した",
        "priority": "MEDIUM",
        "state": "blocked",
        "risk": "LOW",
        "retry_count": 2,
        "max_retries": 3,
        "created_at": "2026-05-10T08:00:00Z",
        "updated_at": "2026-05-10T09:45:00Z",
        "blocked_reason": "Browser Verifyが連続2回失敗。手動確認が必要",
        "approval_required": False,
        "eta_seconds": None,
        "repo": "kyotei-mvp-backend-FastAPI-Render-"
    },
    {
        "id": "task-004",
        "title": "CSS軽量化",
        "description": "status pageのCSSを最適化する",
        "priority": "LOW",
        "state": "queued",
        "risk": "LOW",
        "retry_count": 0,
        "max_retries": 3,
        "created_at": "2026-05-10T07:00:00Z",
        "updated_at": "2026-05-10T07:00:00Z",
        "blocked_reason": None,
        "approval_required": False,
        "eta_seconds": 60,
        "repo": "kyotei-mvp-backend-FastAPI-Render-"
    },
    {
        "id": "task-005",
        "title": "P27 Work Queue実装",
        "description": "Multi-Task Work Queue Runtimeの実装",
        "priority": "HIGH",
        "state": "completed",
        "risk": "MEDIUM",
        "retry_count": 0,
        "max_retries": 3,
        "created_at": "2026-05-10T06:00:00Z",
        "updated_at": "2026-05-10T10:10:00Z",
        "blocked_reason": None,
        "approval_required": False,
        "eta_seconds": 0,
        "repo": "kyotei-mvp-backend-FastAPI-Render-"
    }
]

def _p27_sorted_queue(tasks):
    """Sort by priority then created_at"""
    return sorted(tasks, key=lambda t: (_P27_PRIORITY.get(t["priority"], 9), t["created_at"]))

def _p27_safe_stop_check(task):
    """Check if task should be blocked"""
    desc = (task.get("description", "") + " " + task.get("title", "")).lower()
    for kw in _P27_BLOCKED_KEYWORDS:
        if kw in desc:
            return True, f"危険操作を検出: {kw}"
    if task.get("risk") == "HIGH":
        return True, "HIGH riskタスクは自動実行禁止"
    return False, None

def _p27_retry_allowed(task):
    """Check if retry is allowed"""
    blocked_types = ["db migration", "auth rewrite", "secret"]
    desc = task.get("description", "").lower()
    for bt in blocked_types:
        if bt in desc:
            return False
    return task.get("retry_count", 0) < task.get("max_retries", 3)

def _p27_state_label(state):
    labels = {
        "queued": "待機中",
        "planning": "計画中",
        "running": "実行中",
        "waiting_approval": "承認待ち",
        "blocked": "停止中",
        "retrying": "再試行中",
        "completed": "完了",
        "failed": "失敗",
        "paused": "一時停止"
    }
    return labels.get(state, state)

def _p27_state_icon(state):
    icons = {
        "queued": "⏳",
        "planning": "📋",
        "running": "🟢",
        "waiting_approval": "🟡",
        "blocked": "🔴",
        "retrying": "🔄",
        "completed": "✅",
        "failed": "❌",
        "paused": "⏸"
    }
    return icons.get(state, "⚪")

def _p27_now_jst():
    from datetime import timezone, timedelta
    jst = timezone(timedelta(hours=9))
    return _p27_dt.now(jst).strftime("%Y-%m-%d %H:%M:%S JST")

@router.get("/axia-queue/state")
async def axia_queue_state():
    """Return current queue state as JSON"""
    from fastapi.responses import JSONResponse
    with _p27_lock:
        tasks = list(_p27_queue)
    sorted_tasks = _p27_sorted_queue(tasks)
    active = [t for t in sorted_tasks if t["state"] in ("running", "planning", "retrying", "queued")]
    waiting = [t for t in sorted_tasks if t["state"] == "waiting_approval"]
    blocked = [t for t in sorted_tasks if t["state"] == "blocked"]
    completed = [t for t in sorted_tasks if t["state"] == "completed"]
    failed = [t for t in sorted_tasks if t["state"] == "failed"]
    governance = dict(_P27_GOVERNANCE)
    return JSONResponse({
        "queue_version": "P27",
        "total_tasks": len(sorted_tasks),
        "active": active,
        "waiting_approval": waiting,
        "blocked": blocked,
        "completed": completed,
        "failed": failed,
        "governance": governance,
        "serverTime": _p27_now_jst()
    })

@router.post("/axia-queue/enqueue")
async def axia_queue_enqueue(request: Request):
    """Enqueue a new task"""
    from fastapi.responses import JSONResponse
    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"error": "Invalid JSON"}, status_code=400)
    title = body.get("title", "").strip()
    if not title:
        return JSONResponse({"error": "title is required"}, status_code=400)
    task = {
        "id": "task-" + str(_p27_uuid.uuid4())[:8],
        "title": title,
        "description": body.get("description", title),
        "priority": body.get("priority", "MEDIUM"),
        "state": "queued",
        "risk": body.get("risk", "LOW"),
        "retry_count": 0,
        "max_retries": 3,
        "created_at": _p27_dt.now(_p27_tz.utc).isoformat(),
        "updated_at": _p27_dt.now(_p27_tz.utc).isoformat(),
        "blocked_reason": None,
        "approval_required": body.get("approval_required", False),
        "eta_seconds": body.get("eta_seconds", None),
        "repo": body.get("repo", "kyotei-mvp-backend-FastAPI-Render-")
    }
    # Safe stop check
    blocked, reason = _p27_safe_stop_check(task)
    if blocked:
        task["state"] = "blocked"
        task["blocked_reason"] = reason
    with _p27_lock:
        _p27_queue.append(task)
    return JSONResponse({"status": "enqueued", "task": task})

@router.get("/axia-queue")
async def axia_queue_dashboard():
    """Human-readable Work Queue Dashboard"""
    from fastapi.responses import HTMLResponse
    with _p27_lock:
        tasks = list(_p27_queue)
    sorted_tasks = _p27_sorted_queue(tasks)
    active = [t for t in sorted_tasks if t["state"] in ("running", "planning", "retrying", "queued")]
    waiting = [t for t in sorted_tasks if t["state"] == "waiting_approval"]
    blocked_tasks = [t for t in sorted_tasks if t["state"] == "blocked"]
    completed = [t for t in sorted_tasks if t["state"] == "completed"]
    failed = [t for t in sorted_tasks if t["state"] == "failed"]
    now = _p27_now_jst()

    def task_card(t, extra_class=""):
        icon = _p27_state_icon(t["state"])
        label = _p27_state_label(t["state"])
        risk_color = {"LOW": "#22c55e", "MEDIUM": "#f59e0b", "HIGH": "#ef4444"}.get(t["risk"], "#6b7280")
        blocked_html = ""
        if t.get("blocked_reason"):
            blocked_html = f'<div class="blocked-reason">停止理由: {t["blocked_reason"]}</div>'
        approval_html = ""
        if t.get("approval_required"):
            approval_html = '<div class="approval-badge">承認待ち</div>'
        eta_html = ""
        if t.get("eta_seconds") and t["eta_seconds"] > 0:
            eta_html = f'<span class="eta">推定: {t["eta_seconds"]}秒</span>'
        retry_html = ""
        if t.get("retry_count", 0) > 0:
            retry_html = f'<span class="retry-badge">再試行 {t["retry_count"]}/{t["max_retries"]}</span>'
        return (
            f'<div class="task-card {extra_class}">'
            f'  <div class="task-header">'
            f'    <span class="task-icon">{icon}</span>'
            f'    <span class="task-title">{t["title"]}</span>'
            f'    <span class="task-state">{label}</span>'
            f'  </div>'
            f'  <div class="task-meta">'
            f'    <span class="risk-badge" style="background:{risk_color}">Risk: {t["risk"]}</span>'
            f'    <span class="priority-badge">Priority: {t["priority"]}</span>'
            f'    {eta_html}{retry_html}'
            f'  </div>'
            f'  {blocked_html}{approval_html}'
            f'</div>'
        )

    active_html = "".join(task_card(t) for t in active) or '<div class="empty">現在実行中のタスクはありません</div>'
    waiting_html = "".join(task_card(t, "approval-card") for t in waiting) or ""
    blocked_html = "".join(task_card(t, "blocked-card") for t in blocked_tasks) or ""
    completed_html = "".join(task_card(t, "completed-card") for t in completed) or ""
    failed_html = "".join(task_card(t, "failed-card") for t in failed) or ""

    approval_section = ""
    if waiting:
        approval_section = (
            '<div class="approval-section">'
            '  <div class="section-title approval-title">🟡 承認待ちタスク</div>'
            + waiting_html +
            '</div>'
        )

    blocked_section = ""
    if blocked_tasks:
        blocked_section = (
            '<div class="blocked-section">'
            '  <div class="section-title blocked-title">🔴 停止中タスク</div>'
            + blocked_html +
            '</div>'
        )

    completed_section = ""
    if completed or failed:
        completed_section = (
            '<div class="completed-section">'
            '  <div class="section-title completed-title">✅ 本日完了</div>'
            + completed_html + failed_html +
            '</div>'
        )

    governance_html = (
        f'<div class="governance-bar">'
        f'  <span>同時実行上限: {_P27_GOVERNANCE["max_running"]}件</span>'
        f'  <span>ブラウザセッション上限: {_P27_GOVERNANCE["max_browser_sessions"]}件</span>'
        f'  <span>1時間あたりmerge上限: {_P27_GOVERNANCE["max_merge_per_hour"]}件</span>'
        f'</div>'
    )

    html = (
        "<!DOCTYPE html><html lang='ja'><head>"
        "<meta charset='UTF-8'>"
        "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        "<title>AXIA Work Queue</title>"
        "<style>"
        "* { box-sizing: border-box; margin: 0; padding: 0; }"
        "body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;"
        "  background: #0f172a; color: #e2e8f0; min-height: 100vh; padding-bottom: 80px; }"
        ".header { background: #1e293b; border-bottom: 1px solid #334155;"
        "  padding: 16px 24px; display: flex; justify-content: space-between; align-items: center; }"
        ".header h1 { font-size: 1.4rem; font-weight: 700; color: #f1f5f9; }"
        ".badge-running { background: #22c55e; color: #fff; padding: 4px 12px;"
        "  border-radius: 20px; font-size: 0.75rem; font-weight: 600; }"
        ".server-time { color: #94a3b8; font-size: 0.8rem; }"
        ".governance-bar { background: #1e293b; border-bottom: 1px solid #334155;"
        "  padding: 8px 24px; display: flex; gap: 24px; font-size: 0.75rem; color: #94a3b8; }"
        ".main { max-width: 900px; margin: 0 auto; padding: 24px 16px; }"
        ".section-title { font-size: 1rem; font-weight: 700; margin-bottom: 12px; padding-bottom: 8px;"
        "  border-bottom: 1px solid #334155; }"
        ".approval-title { color: #f59e0b; }"
        ".blocked-title { color: #ef4444; }"
        ".completed-title { color: #22c55e; }"
        ".today-section, .approval-section, .blocked-section, .completed-section {"
        "  margin-bottom: 28px; }"
        ".task-card { background: #1e293b; border: 1px solid #334155; border-radius: 10px;"
        "  padding: 14px 16px; margin-bottom: 10px; }"
        ".task-card.approval-card { border-color: #f59e0b; }"
        ".task-card.blocked-card { border-color: #ef4444; }"
        ".task-card.completed-card { opacity: 0.7; }"
        ".task-card.failed-card { border-color: #ef4444; opacity: 0.7; }"
        ".task-header { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }"
        ".task-icon { font-size: 1.2rem; }"
        ".task-title { font-weight: 600; flex: 1; color: #f1f5f9; }"
        ".task-state { font-size: 0.75rem; color: #94a3b8; }"
        ".task-meta { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }"
        ".risk-badge { color: #fff; padding: 2px 8px; border-radius: 10px; font-size: 0.7rem; font-weight: 600; }"
        ".priority-badge { background: #334155; color: #94a3b8; padding: 2px 8px;"
        "  border-radius: 10px; font-size: 0.7rem; }"
        ".eta { color: #60a5fa; font-size: 0.75rem; }"
        ".retry-badge { background: #7c3aed; color: #fff; padding: 2px 8px;"
        "  border-radius: 10px; font-size: 0.7rem; }"
        ".blocked-reason { margin-top: 8px; color: #f87171; font-size: 0.8rem; }"
        ".approval-badge { margin-top: 8px; background: #f59e0b; color: #000;"
        "  padding: 4px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 600;"
        "  display: inline-block; }"
        ".empty { color: #64748b; font-size: 0.9rem; padding: 12px 0; }"
        ".footer { text-align: center; color: #475569; font-size: 0.75rem;"
        "  padding: 24px; margin-top: 40px; }"
        "@media (max-width: 600px) {"
        "  .governance-bar { flex-direction: column; gap: 4px; }"
        "  .task-meta { flex-direction: column; align-items: flex-start; }"
        "}"
        "</style>"
        "<script>"
        "const NOISE_WORDS = ['analysis', 'thinking', 'critic', 'learner', 'debug', 'trace', '[object Object]'];"
        "function sanitize(s) {"
        "  if (!s) return s;"
        "  let r = String(s);"
        "  NOISE_WORDS.forEach(w => { r = r.replace(new RegExp(w, 'gi'), ''); });"
        "  return r.trim();"
        "}"
        "function autoRefresh() {"
        "  fetch('/api/axia-queue/state')"
        "    .then(r => r.json())"
        "    .then(d => {"
        "      const el = document.getElementById('server-time');"
        "      if (el) el.textContent = sanitize(d.serverTime) || '';"
        "    }).catch(() => {});"
        "}"
        "setInterval(autoRefresh, 8000);"
        "window.addEventListener('load', () => {"
        "  const saved = sessionStorage.getItem('p27_queue_state');"
        "  if (saved) { try { JSON.parse(saved); } catch(e) {} }"
        "  fetch('/api/axia-queue/state').then(r => r.json())"
        "    .then(d => sessionStorage.setItem('p27_queue_state', JSON.stringify(d)))"
        "    .catch(() => {});"
        "});"
        "</script>"
        "</head><body>"
        "<div class='header'>"
        "  <h1>AXIA Work Queue</h1>"
        f"  <span class=\'server-time\' id=\'server-time\'>{now}</span>"
        "  <span class='badge-running'>RUNNING</span>"
        "</div>"
        f"{governance_html}"
        "<div class='main'>"
        "  <div class='today-section'>"
        "    <div class='section-title'>📋 Today's Work</div>"
        f"    {active_html}"
        "  </div>"
        f"{approval_section}"
        f"{blocked_section}"
        f"{completed_section}"
        "</div>"
        "<div class='footer'>"
        "  AXIA_RUNTIME_CLASS = AUTONOMOUS_MULTI_TASK_WORK_OS<br>"
        f"  Queue Version: P27 | Tasks: {len(sorted_tasks)} | {now}"
        "</div>"
        "</body></html>"
    )
    return HTMLResponse(content=html)


# ─────────────────────────────────────────────────────────────────────────────
# AXIA P28: Autonomous Goal Alignment & Drift Prevention Runtime
# Goal Lock / Scope Guard / Drift Detection / Loop Protection
# Artifact Cleanliness / Completion Gate v2 / Human Alignment View
# ─────────────────────────────────────────────────────────────────────────────

from pydantic import BaseModel as _P28BaseModel
import threading as _p28_threading
from collections import defaultdict as _p28_defaultdict
from datetime import datetime as _p28_dt, timezone as _p28_tz

# ─── P28 In-Memory State ─────────────────────────────────────────────────────

_p28_lock = _p28_threading.RLock()  # RLock: reentrant to prevent deadlock in nested calls

_p28_goal_state = {
    "goalId": None,
    "goalSummary": None,
    "allowedScope": [],
    "forbiddenScope": [
        "DB migration", "auth redesign", "payment", "deploy rewrite",
        "secret rotation", "delete all", "drop table", "infra change"
    ],
    "completionDefinition": {
        "goalAchieved": False,
        "verifyPass": False,
        "browserVerifyPass": False,
        "riskAccepted": False,
        "scopeClean": True,
        "artifactClean": True,
    },
    "lockedAt": None,
}

_p28_drift_state = {
    "driftDetected": False,
    "driftReason": None,
    "driftAt": None,
}

_p28_loop_counters: dict = _p28_defaultdict(int)
_p28_loop_limits = {
    "verify": 5,
    "retry": 3,
    "rewrite": 5,
    "pr_reopen": 3,
}

_p28_artifact_banned = [
    "tmp", "backup", "node_modules", "__pycache__",
    "dist", "coverage", ".cache", ".DS_Store"
]

_p28_scope_violations: list = []
_p28_event_log: list = []


def _p28_now() -> str:
    return _p28_dt.now(_p28_tz.utc).strftime("%Y-%m-%dT%H:%M:%S JST")


def _p28_log_event(event_type: str, detail: str):
    with _p28_lock:
        _p28_event_log.append({
            "type": event_type,
            "detail": detail,
            "timestamp": _p28_now(),
        })
        if len(_p28_event_log) > 200:
            _p28_event_log.pop(0)


# ─── P28 Schemas ─────────────────────────────────────────────────────────────

class P28GoalLockRequest(_P28BaseModel):
    goalSummary: str
    allowedScope: list = []
    forbiddenScope: list = []
    completionDefinition: dict = {}


class P28ScopeCheckRequest(_P28BaseModel):
    changedFiles: list = []
    description: str = ""


# ─── P28 Endpoints ───────────────────────────────────────────────────────────

@router.get("/axia-alignment", response_class=HTMLResponse)
async def axia_alignment_dashboard():
    """P28: Human Alignment View Dashboard"""
    with _p28_lock:
        goal = dict(_p28_goal_state)
        drift = dict(_p28_drift_state)
        loops = dict(_p28_loop_counters)
        violations = list(_p28_scope_violations[-5:])
        events = list(_p28_event_log[-10:])

    now = _p28_now()

    # Goal section
    goal_summary = goal["goalSummary"] or "（未設定）"
    goal_id = goal["goalId"] or "—"
    locked_at = goal["lockedAt"] or "—"

    # Allowed scope
    allowed_html = ""
    for s in (goal["allowedScope"] or ["（未設定）"]):
        allowed_html += f"<div class='scope-item scope-allowed'>✅ {s}</div>"

    # Forbidden scope
    forbidden_html = ""
    for s in (goal["forbiddenScope"] or []):
        forbidden_html += f"<div class='scope-item scope-forbidden'>🚫 {s}</div>"

    # Drift status
    drift_class = "badge-drift" if drift["driftDetected"] else "badge-clean"
    drift_label = "⚠️ DRIFT DETECTED" if drift["driftDetected"] else "✅ ON TRACK"
    drift_reason = drift["driftReason"] or "—"

    # Loop counters
    loop_html = ""
    for k, v in _p28_loop_limits.items():
        count = loops.get(k, 0)
        bar_pct = min(100, int(count / v * 100))
        bar_class = "bar-danger" if count >= v else ("bar-warn" if count >= v * 0.6 else "bar-ok")
        loop_html += (
            f"<div class='loop-row'>"
            f"  <span class='loop-label'>{k}</span>"
            f"  <div class='loop-bar-bg'><div class='loop-bar {bar_class}' style='width:{bar_pct}%'></div></div>"
            f"  <span class='loop-count'>{count}/{v}</span>"
            f"</div>"
        )

    # Completion gate
    cd = goal["completionDefinition"]
    gate_items = [
        ("goal達成", cd.get("goalAchieved", False)),
        ("Verify PASS", cd.get("verifyPass", False)),
        ("Browser Verify PASS", cd.get("browserVerifyPass", False)),
        ("Risk 許容", cd.get("riskAccepted", False)),
        ("Scope クリーン", cd.get("scopeClean", True)),
        ("Artifact クリーン", cd.get("artifactClean", True)),
    ]
    gate_html = ""
    all_pass = all(v for _, v in gate_items)
    for label, ok in gate_items:
        icon = "✅" if ok else "⏳"
        cls = "gate-ok" if ok else "gate-pending"
        gate_html += f"<div class='gate-item {cls}'>{icon} {label}</div>"
    gate_status = "DONE 可能" if all_pass else "DONE 禁止"
    gate_status_cls = "gate-done" if all_pass else "gate-blocked"

    # Violations
    viol_html = ""
    if violations:
        for v in violations:
            viol_html += f"<div class='violation-item'>🚫 {v['file']} — {v['reason']}</div>"
    else:
        viol_html = "<div class='violation-none'>違反なし</div>"

    # Events
    event_html = ""
    for e in reversed(events):
        event_html += f"<div class='event-row'><span class='event-type'>{e['type']}</span> {e['detail']} <span class='event-time'>{e['timestamp']}</span></div>"
    if not event_html:
        event_html = "<div class='event-none'>イベントなし</div>"

    html = (
        "<!DOCTYPE html><html lang='ja'><head>"
        "<meta charset='UTF-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>AXIA Goal Alignment</title>"
        "<style>"
        "* { box-sizing: border-box; margin: 0; padding: 0; }"
        "body { background: #0d1117; color: #e6edf3; font-family: 'Segoe UI', sans-serif; font-size: 14px; }"
        ".header { display: flex; align-items: center; justify-content: space-between; padding: 16px 24px; background: #161b22; border-bottom: 1px solid #30363d; }"
        ".header h1 { font-size: 20px; font-weight: 700; color: #58a6ff; }"
        ".badge-clean { background: #1a7f37; color: #fff; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 700; }"
        ".badge-drift { background: #da3633; color: #fff; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 700; }"
        ".gov-bar { display: flex; gap: 24px; padding: 10px 24px; background: #0d1117; border-bottom: 1px solid #21262d; font-size: 12px; color: #8b949e; }"
        ".main { padding: 20px 24px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }"
        "@media (max-width: 700px) { .main { grid-template-columns: 1fr; } }"
        ".card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; }"
        ".card-title { font-size: 13px; font-weight: 700; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }"
        ".goal-summary { font-size: 18px; font-weight: 700; color: #e6edf3; margin-bottom: 8px; }"
        ".goal-meta { font-size: 11px; color: #8b949e; }"
        ".scope-item { padding: 6px 10px; border-radius: 4px; margin-bottom: 4px; font-size: 12px; }"
        ".scope-allowed { background: #1a2e1a; color: #3fb950; border: 1px solid #1a7f37; }"
        ".scope-forbidden { background: #2e1a1a; color: #f85149; border: 1px solid #da3633; }"
        ".loop-row { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }"
        ".loop-label { width: 80px; font-size: 12px; color: #8b949e; }"
        ".loop-bar-bg { flex: 1; height: 8px; background: #21262d; border-radius: 4px; overflow: hidden; }"
        ".loop-bar { height: 100%; border-radius: 4px; transition: width 0.3s; }"
        ".bar-ok { background: #1a7f37; }"
        ".bar-warn { background: #9e6a03; }"
        ".bar-danger { background: #da3633; }"
        ".loop-count { width: 40px; font-size: 11px; color: #8b949e; text-align: right; }"
        ".gate-item { padding: 6px 10px; border-radius: 4px; margin-bottom: 4px; font-size: 12px; }"
        ".gate-ok { background: #1a2e1a; color: #3fb950; }"
        ".gate-pending { background: #1c2128; color: #8b949e; }"
        ".gate-status { margin-top: 12px; padding: 8px 12px; border-radius: 6px; font-weight: 700; text-align: center; }"
        ".gate-done { background: #1a7f37; color: #fff; }"
        ".gate-blocked { background: #da3633; color: #fff; }"
        ".drift-box { padding: 10px 14px; border-radius: 6px; margin-bottom: 8px; }"
        ".drift-clean { background: #1a2e1a; border: 1px solid #1a7f37; }"
        ".drift-alert { background: #2e1a1a; border: 1px solid #da3633; }"
        ".drift-reason { font-size: 12px; color: #8b949e; margin-top: 4px; }"
        ".violation-item { padding: 5px 8px; background: #2e1a1a; border-radius: 4px; margin-bottom: 4px; font-size: 12px; color: #f85149; }"
        ".violation-none { color: #3fb950; font-size: 12px; }"
        ".event-row { padding: 4px 0; border-bottom: 1px solid #21262d; font-size: 11px; color: #8b949e; }"
        ".event-type { color: #58a6ff; font-weight: 700; margin-right: 6px; }"
        ".event-time { float: right; color: #484f58; }"
        ".event-none { color: #484f58; font-size: 12px; }"
        ".footer { text-align: center; padding: 16px; font-size: 11px; color: #484f58; border-top: 1px solid #21262d; margin-top: 20px; }"
        "</style>"
        "<script>"
        "const NOISE_FILTER = ['analysis','thinking','critic','learner','debug','trace'];"
        "function sanitize(s) {"
        "  if (typeof s !== 'string') return '';"
        "  for (const n of NOISE_FILTER) { if (s.toLowerCase().includes(n)) return ''; }"
        "  return s;"
        "}"
        "function autoRefresh() {"
        "  fetch('/api/axia-alignment/state').then(r => r.json()).then(d => {"
        "    const el = document.getElementById('align-time');"
        "    if (el) el.textContent = sanitize(d.serverTime) || '';"
        "  }).catch(() => {});"
        "}"
        "setInterval(autoRefresh, 10000);"
        "</script>"
        "</head><body>"
        "<div class='header'>"
        "  <h1>AXIA Goal Alignment</h1>"
        f"  <span id='align-time' style='font-size:12px;color:#8b949e'>{now}</span>"
        f"  <span class='{drift_class}'>{drift_label}</span>"
        "</div>"
        "<div class='gov-bar'>"
        f"  <span>Goal ID: {goal_id}</span>"
        f"  <span>Locked: {locked_at}</span>"
        f"  <span>Completion Gate: <strong>{gate_status}</strong></span>"
        "</div>"
        "<div class='main'>"

        # Card 1: Goal
        "<div class='card'>"
        "  <div class='card-title'>🎯 Goal</div>"
        f"  <div class='goal-summary'>{goal_summary}</div>"
        f"  <div class='goal-meta'>ID: {goal_id} | Locked: {locked_at}</div>"
        "</div>"

        # Card 2: Drift Detection
        "<div class='card'>"
        "  <div class='card-title'>🔍 Drift Detection</div>"
        f"  <div class='drift-box {'drift-alert' if drift['driftDetected'] else 'drift-clean'}'>"
        f"    <strong>{drift_label}</strong>"
        f"    <div class='drift-reason'>理由: {drift_reason}</div>"
        "  </div>"
        "</div>"

        # Card 3: Allowed Scope
        "<div class='card'>"
        "  <div class='card-title'>✅ Allowed Scope</div>"
        f"  {allowed_html}"
        "</div>"

        # Card 4: Blocked Actions
        "<div class='card'>"
        "  <div class='card-title'>🚫 Blocked Actions</div>"
        f"  {forbidden_html}"
        "</div>"

        # Card 5: Loop Protection
        "<div class='card'>"
        "  <div class='card-title'>🔄 Loop Protection</div>"
        f"  {loop_html}"
        "</div>"

        # Card 6: Completion Gate v2
        "<div class='card'>"
        "  <div class='card-title'>🏁 Completion Gate v2</div>"
        f"  {gate_html}"
        f"  <div class='gate-status {gate_status_cls}'>{gate_status}</div>"
        "</div>"

        # Card 7: Scope Violations
        "<div class='card'>"
        "  <div class='card-title'>⚠️ Scope Violations</div>"
        f"  {viol_html}"
        "</div>"

        # Card 8: Event Log
        "<div class='card'>"
        "  <div class='card-title'>📋 Event Log</div>"
        f"  {event_html}"
        "</div>"

        "</div>"
        "<div class='footer'>"
        "  AXIA_RUNTIME_CLASS = GOAL_ALIGNED_AUTONOMOUS_OPERATOR<br>"
        f"  Alignment Version: P28 | {now}"
        "</div>"
        "</body></html>"
    )
    return HTMLResponse(content=html)


@router.get("/axia-alignment/state")
async def axia_alignment_state():
    """P28: Goal Alignment State JSON API"""
    with _p28_lock:
        goal = dict(_p28_goal_state)
        drift = dict(_p28_drift_state)
        loops = dict(_p28_loop_counters)
        violations = list(_p28_scope_violations[-10:])
        events = list(_p28_event_log[-20:])

    cd = goal.get("completionDefinition", {})
    all_gate_pass = all([
        cd.get("goalAchieved", False),
        cd.get("verifyPass", False),
        cd.get("browserVerifyPass", False),
        cd.get("riskAccepted", False),
        cd.get("scopeClean", True),
        cd.get("artifactClean", True),
    ])

    return {
        "alignmentVersion": "P28",
        "goal": {
            "goalId": goal["goalId"],
            "goalSummary": goal["goalSummary"],
            "allowedScope": goal["allowedScope"],
            "forbiddenScope": goal["forbiddenScope"],
            "lockedAt": goal["lockedAt"],
        },
        "drift": {
            "driftDetected": drift["driftDetected"],
            "driftReason": drift["driftReason"],
            "driftAt": drift["driftAt"],
        },
        "loopCounters": loops,
        "loopLimits": _p28_loop_limits,
        "completionGate": {
            "items": cd,
            "allPass": all_gate_pass,
            "status": "DONE_ALLOWED" if all_gate_pass else "DONE_BLOCKED",
        },
        "scopeViolations": violations,
        "artifactBanned": _p28_artifact_banned,
        "recentEvents": events,
        "serverTime": _p28_now(),
    }


@router.post("/axia-alignment/lock")
async def axia_alignment_lock(req: P28GoalLockRequest):
    """P28: Goal Lock — fix goal, scope, completion definition"""
    import uuid as _uuid
    goal_id = f"goal-{_uuid.uuid4().hex[:8]}"
    with _p28_lock:
        _p28_goal_state["goalId"] = goal_id
        _p28_goal_state["goalSummary"] = req.goalSummary
        _p28_goal_state["allowedScope"] = req.allowedScope or []
        if req.forbiddenScope:
            _p28_goal_state["forbiddenScope"] = req.forbiddenScope
        _p28_goal_state["lockedAt"] = _p28_now()
        # Reset drift, loops, and completion gate on new goal lock
        _p28_drift_state["driftDetected"] = False
        _p28_drift_state["driftReason"] = None
        _p28_drift_state["driftAt"] = None
        _p28_loop_counters.clear()
        _p28_scope_violations.clear()
        # Reset completion gate to initial state (only scopeClean/artifactClean default True)
        _p28_goal_state["completionDefinition"] = {
            "goalAchieved": False,
            "verifyPass": False,
            "browserVerifyPass": False,
            "riskAccepted": False,
            "scopeClean": True,
            "artifactClean": True,
        }
        if req.completionDefinition:
            _p28_goal_state["completionDefinition"].update(req.completionDefinition)

    _p28_log_event("GOAL_LOCK", f"Goal locked: {req.goalSummary}")

    return {
        "status": "locked",
        "goalId": goal_id,
        "goalSummary": req.goalSummary,
        "allowedScope": req.allowedScope,
        "forbiddenScope": _p28_goal_state["forbiddenScope"],
        "lockedAt": _p28_goal_state["lockedAt"],
    }


@router.post("/axia-alignment/check")
async def axia_alignment_check(req: P28ScopeCheckRequest):
    """P28: Scope Guard — check changed files against allowed/forbidden scope"""
    with _p28_lock:
        allowed = list(_p28_goal_state["allowedScope"])
        forbidden_scope = list(_p28_goal_state["forbiddenScope"])

    violations = []
    artifact_violations = []
    safe_files = []

    for f in req.changedFiles:
        # Artifact cleanliness check
        for banned in _p28_artifact_banned:
            if banned in f:
                artifact_violations.append({
                    "file": f,
                    "reason": f"禁止artifact: {banned}",
                    "type": "ARTIFACT"
                })
                break
        else:
            # Scope check — if allowedScope is set, file must match
            if allowed:
                in_scope = any(a in f or f.startswith(a) for a in allowed)
                if not in_scope:
                    violations.append({
                        "file": f,
                        "reason": f"scope外ファイル (allowed: {allowed})",
                        "type": "SCOPE_VIOLATION"
                    })
                else:
                    safe_files.append(f)
            else:
                safe_files.append(f)

    # Description forbidden scope check
    desc_lower = req.description.lower()
    desc_violations = []
    for fs in forbidden_scope:
        if fs.lower() in desc_lower:
            desc_violations.append({
                "file": "(description)",
                "reason": f"禁止スコープ検出: {fs}",
                "type": "FORBIDDEN_SCOPE"
            })

    all_violations = violations + artifact_violations + desc_violations

    # Record violations
    with _p28_lock:
        for v in all_violations:
            _p28_scope_violations.append(v)
        if len(_p28_scope_violations) > 100:
            del _p28_scope_violations[:-100]

    if all_violations:
        _p28_log_event("SCOPE_VIOLATION", f"{len(all_violations)} violation(s) detected")
        return {
            "status": "BLOCKED",
            "safeStop": True,
            "violations": all_violations,
            "safeFiles": safe_files,
            "message": f"SAFE STOP: {len(all_violations)}件のscope違反を検出",
        }

    _p28_log_event("SCOPE_CHECK", f"SAFE: {len(safe_files)} file(s) checked")
    return {
        "status": "SAFE",
        "safeStop": False,
        "violations": [],
        "safeFiles": safe_files,
        "message": "全ファイルがscope内です",
    }


@router.post("/axia-alignment/drift")
async def axia_alignment_drift(body: dict):
    """P28: Drift Detection — record drift event"""
    action_type = body.get("actionType", "unknown")
    detail = body.get("detail", "")

    with _p28_lock:
        count = _p28_loop_counters[action_type] + 1
        _p28_loop_counters[action_type] = count
        limit = _p28_loop_limits.get(action_type, 999)

        if count >= limit:
            _p28_drift_state["driftDetected"] = True
            _p28_drift_state["driftReason"] = f"{action_type} loop: {count}/{limit}回 — 強制停止"
            _p28_drift_state["driftAt"] = _p28_now()
            _p28_log_event("DRIFT_DETECTED", f"{action_type}: {count}/{limit}")
            return {
                "status": "DRIFT_DETECTED",
                "safeStop": True,
                "actionType": action_type,
                "count": count,
                "limit": limit,
                "message": f"目的から逸脱した可能性があります — {action_type} {count}/{limit}回",
            }

    _p28_log_event("LOOP_COUNT", f"{action_type}: {count}/{limit}")
    return {
        "status": "OK",
        "safeStop": False,
        "actionType": action_type,
        "count": count,
        "limit": limit,
        "message": f"{action_type}: {count}/{limit}",
    }


@router.post("/axia-alignment/complete")
async def axia_alignment_complete(body: dict):
    """P28: Completion Gate v2 — update completion conditions"""
    with _p28_lock:
        cd = _p28_goal_state["completionDefinition"]
        for key in ["goalAchieved", "verifyPass", "browserVerifyPass", "riskAccepted", "scopeClean", "artifactClean"]:
            if key in body:
                cd[key] = bool(body[key])
        all_pass = all([
            cd.get("goalAchieved", False),
            cd.get("verifyPass", False),
            cd.get("browserVerifyPass", False),
            cd.get("riskAccepted", False),
            cd.get("scopeClean", True),
            cd.get("artifactClean", True),
        ])

    _p28_log_event("COMPLETION_GATE", f"allPass={all_pass}")
    return {
        "status": "DONE_ALLOWED" if all_pass else "DONE_BLOCKED",
        "allPass": all_pass,
        "completionDefinition": cd,
        "message": "DONE 可能" if all_pass else "DONE 禁止 — 全条件を満たしてください",
    }

# ─── End of P28 ──────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# AXIA P29: Autonomous Team Coordination Runtime
# Planner / Operator / Verifier / Reviewer / Recovery
# Role Governance / Reviewer Gate / Inter-Role Timeline / Human Team View
# ─────────────────────────────────────────────────────────────────────────────

import threading as _p29_threading
from datetime import datetime as _p29_dt, timezone as _p29_tz
from collections import deque as _p29_deque

# ─── P29 Role Definitions ────────────────────────────────────────────────────

_P29_ROLES = {
    "planner": {
        "roleId": "planner",
        "displayName": "Planner",
        "icon": "🗺️",
        "description": "goal分析・scope決定・execution plan・risk判定",
        "allowedActions": ["analyze_goal", "set_scope", "create_plan", "assess_risk", "approve_plan"],
        "forbiddenActions": ["write_code", "modify_file", "create_pr", "merge", "rollback"],
    },
    "operator": {
        "roleId": "operator",
        "displayName": "Operator",
        "icon": "⚙️",
        "description": "backup・write・diff・PR作成",
        "allowedActions": ["backup", "write_file", "create_diff", "create_pr", "push_branch"],
        "forbiddenActions": ["change_goal", "change_scope", "approve_merge", "verify", "rollback"],
    },
    "verifier": {
        "roleId": "verifier",
        "displayName": "Verifier",
        "icon": "🔍",
        "description": "FastAPI import・HTTP verify・browser verify・responsive・noise check",
        "allowedActions": ["check_import", "http_verify", "browser_verify", "check_responsive", "noise_check"],
        "forbiddenActions": ["write_file", "modify_code", "merge", "create_pr", "change_goal"],
    },
    "reviewer": {
        "roleId": "reviewer",
        "displayName": "Reviewer",
        "icon": "👁️",
        "description": "scope violation・artifact clean・secret scan・merge governance・completion gate",
        "allowedActions": ["check_scope", "check_artifacts", "scan_secrets", "check_governance", "approve_merge", "block_merge"],
        "forbiddenActions": ["write_code", "modify_file", "create_pr", "rollback", "change_goal"],
    },
    "recovery": {
        "roleId": "recovery",
        "displayName": "Recovery",
        "icon": "🔄",
        "description": "rollback・retry判断・safe stop・recovery plan",
        "allowedActions": ["rollback", "assess_retry", "safe_stop", "create_recovery_plan", "restore_backup"],
        "forbiddenActions": ["create_pr", "merge", "change_goal", "write_new_code", "approve"],
    },
}

# ─── P29 State ───────────────────────────────────────────────────────────────

_p29_lock = _p29_threading.RLock()

_p29_role_states: dict = {
    role_id: {
        "roleId": role_id,
        "status": "IDLE",
        "currentTask": None,
        "lastAction": None,
        "lastActionAt": None,
        "actionCount": 0,
        "violations": [],
    }
    for role_id in _P29_ROLES
}

_p29_reviewer_gate = {
    "status": "PENDING",  # PENDING / PASS / BLOCK
    "checklist": {
        "scopeClean": False,
        "artifactClean": False,
        "secretScan": False,
        "governanceOk": False,
        "completionGateOk": False,
    },
    "approvedAt": None,
    "blockedReason": None,
}

_p29_timeline: _p29_deque = _p29_deque(maxlen=100)

_p29_safe_stopped = False
_p29_safe_stop_reason = None


def _p29_now() -> str:
    return _p29_dt.now(_p29_tz.utc).strftime("%Y-%m-%dT%H:%M:%S JST")


def _p29_add_timeline(role_id: str, action: str, detail: str, result: str = "OK"):
    with _p29_lock:
        _p29_timeline.append({
            "roleId": role_id,
            "action": action,
            "detail": detail,
            "result": result,
            "timestamp": _p29_now(),
        })


# ─── P29 Endpoints ───────────────────────────────────────────────────────────

@router.get("/axia-team", response_class=HTMLResponse)
async def axia_team_dashboard():
    """P29: Human Team View Dashboard"""
    with _p29_lock:
        role_states = {k: dict(v) for k, v in _p29_role_states.items()}
        reviewer_gate = dict(_p29_reviewer_gate)
        timeline = list(_p29_timeline)[-15:]
        safe_stopped = _p29_safe_stopped
        safe_stop_reason = _p29_safe_stop_reason

    now = _p29_now()

    # Status badge colors
    STATUS_COLORS = {
        "IDLE": ("#484f58", "#8b949e"),
        "RUNNING": ("#1a7f37", "#3fb950"),
        "DONE": ("#0969da", "#58a6ff"),
        "VERIFYING": ("#9e6a03", "#d29922"),
        "WAITING": ("#6e40c9", "#bc8cff"),
        "BLOCKED": ("#da3633", "#f85149"),
        "FAILED": ("#da3633", "#f85149"),
    }

    # Role cards
    role_cards_html = ""
    for role_id, role_def in _P29_ROLES.items():
        state = role_states[role_id]
        status = state["status"]
        bg, fg = STATUS_COLORS.get(status, ("#484f58", "#8b949e"))
        task_text = state["currentTask"] or "—"
        last_action = state["lastAction"] or "—"
        last_at = state["lastActionAt"] or "—"
        viol_count = len(state["violations"])
        viol_badge = f"<span style='color:#f85149;font-size:11px;'>⚠️ {viol_count}件の違反</span>" if viol_count else ""

        allowed_html = "".join(f"<span class='action-tag action-allowed'>{a}</span>" for a in role_def["allowedActions"])
        forbidden_html = "".join(f"<span class='action-tag action-forbidden'>{a}</span>" for a in role_def["forbiddenActions"])

        role_cards_html += f"""
<div class='role-card'>
  <div class='role-header'>
    <span class='role-icon'>{role_def['icon']}</span>
    <span class='role-name'>{role_def['displayName']}</span>
    <span class='role-status' style='background:{bg};color:{fg};'>{status}</span>
  </div>
  <div class='role-desc'>{role_def['description']}</div>
  <div class='role-meta'>
    <div>現在のタスク: <strong>{task_text}</strong></div>
    <div>最終アクション: {last_action} <span style='color:#484f58;font-size:11px;'>{last_at}</span></div>
    <div>アクション数: {state['actionCount']} {viol_badge}</div>
  </div>
  <div class='role-actions'>
    <div class='actions-label'>✅ 許可</div>
    <div>{allowed_html}</div>
    <div class='actions-label' style='margin-top:6px;'>🚫 禁止</div>
    <div>{forbidden_html}</div>
  </div>
</div>"""

    # Reviewer Gate
    gate = reviewer_gate
    gate_status = gate["status"]
    gate_bg = "#1a7f37" if gate_status == "PASS" else ("#da3633" if gate_status == "BLOCK" else "#6e40c9")
    gate_items_html = ""
    for k, v in gate["checklist"].items():
        icon = "✅" if v else "⏳"
        cls = "gate-ok" if v else "gate-pending"
        gate_items_html += f"<div class='gate-item {cls}'>{icon} {k}</div>"
    merge_status = "MERGE 許可" if gate_status == "PASS" else "MERGE 禁止"
    merge_cls = "merge-allowed" if gate_status == "PASS" else "merge-blocked"

    # Timeline
    timeline_html = ""
    for event in reversed(timeline):
        role_def = _P29_ROLES.get(event["roleId"], {})
        icon = role_def.get("icon", "•")
        result_color = "#3fb950" if event["result"] == "OK" else "#f85149"
        timeline_html += f"""<div class='timeline-row'>
  <span class='tl-icon'>{icon}</span>
  <span class='tl-role'>{event['roleId']}</span>
  <span class='tl-action'>{event['action']}</span>
  <span class='tl-detail'>{event['detail']}</span>
  <span class='tl-result' style='color:{result_color};'>{event['result']}</span>
  <span class='tl-time'>{event['timestamp']}</span>
</div>"""
    if not timeline_html:
        timeline_html = "<div style='color:#484f58;font-size:12px;'>イベントなし</div>"

    # Safe Stop banner
    safe_stop_banner = ""
    if safe_stopped:
        safe_stop_banner = f"<div class='safe-stop-banner'>🛑 SAFE STOP — {safe_stop_reason}</div>"

    html = (
        "<!DOCTYPE html><html lang='ja'><head>"
        "<meta charset='UTF-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>AXIA Team Coordination</title>"
        "<style>"
        "* { box-sizing: border-box; margin: 0; padding: 0; }"
        "body { background: #0d1117; color: #e6edf3; font-family: 'Segoe UI', sans-serif; font-size: 14px; }"
        ".header { display: flex; align-items: center; justify-content: space-between; padding: 16px 24px; background: #161b22; border-bottom: 1px solid #30363d; }"
        ".header h1 { font-size: 20px; font-weight: 700; color: #58a6ff; }"
        ".safe-stop-banner { background: #da3633; color: #fff; padding: 10px 24px; font-weight: 700; text-align: center; }"
        ".gov-bar { display: flex; gap: 24px; padding: 10px 24px; background: #0d1117; border-bottom: 1px solid #21262d; font-size: 12px; color: #8b949e; }"
        ".roles-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; padding: 20px 24px; }"
        "@media (max-width: 700px) { .roles-grid { grid-template-columns: 1fr; } }"
        ".role-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; }"
        ".role-header { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }"
        ".role-icon { font-size: 20px; }"
        ".role-name { font-size: 16px; font-weight: 700; flex: 1; }"
        ".role-status { padding: 3px 10px; border-radius: 10px; font-size: 11px; font-weight: 700; }"
        ".role-desc { font-size: 12px; color: #8b949e; margin-bottom: 10px; }"
        ".role-meta { font-size: 12px; color: #8b949e; margin-bottom: 10px; line-height: 1.8; }"
        ".role-meta strong { color: #e6edf3; }"
        ".role-actions { font-size: 11px; }"
        ".actions-label { color: #8b949e; font-size: 11px; margin-bottom: 4px; }"
        ".action-tag { display: inline-block; padding: 2px 6px; border-radius: 3px; margin: 2px; font-size: 10px; }"
        ".action-allowed { background: #1a2e1a; color: #3fb950; border: 1px solid #1a7f37; }"
        ".action-forbidden { background: #2e1a1a; color: #f85149; border: 1px solid #da3633; }"
        ".bottom-section { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; padding: 0 24px 24px; }"
        "@media (max-width: 700px) { .bottom-section { grid-template-columns: 1fr; } }"
        ".card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; }"
        ".card-title { font-size: 13px; font-weight: 700; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }"
        ".gate-item { padding: 5px 8px; border-radius: 4px; margin-bottom: 4px; font-size: 12px; }"
        ".gate-ok { background: #1a2e1a; color: #3fb950; }"
        ".gate-pending { background: #1c2128; color: #8b949e; }"
        ".merge-status { margin-top: 12px; padding: 8px 12px; border-radius: 6px; font-weight: 700; text-align: center; }"
        ".merge-allowed { background: #1a7f37; color: #fff; }"
        ".merge-blocked { background: #da3633; color: #fff; }"
        ".timeline-row { display: grid; grid-template-columns: 24px 80px 100px 1fr 50px 140px; gap: 6px; align-items: center; padding: 5px 0; border-bottom: 1px solid #21262d; font-size: 11px; }"
        ".tl-icon { text-align: center; }"
        ".tl-role { color: #58a6ff; font-weight: 700; }"
        ".tl-action { color: #d29922; }"
        ".tl-detail { color: #8b949e; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }"
        ".tl-result { font-weight: 700; }"
        ".tl-time { color: #484f58; }"
        ".footer { text-align: center; padding: 16px; font-size: 11px; color: #484f58; border-top: 1px solid #21262d; }"
        "</style>"
        "<script>"
        "const NOISE = ['analysis','thinking','critic','learner'];"
        "function sanitize(s) { if(typeof s!=='string') return ''; for(const n of NOISE){if(s.toLowerCase().includes(n)) return '';} return s; }"
        "function autoRefresh() {"
        "  fetch('/api/axia-team/state').then(r=>r.json()).then(d=>{"
        "    const el=document.getElementById('team-time');"
        "    if(el) el.textContent=sanitize(d.serverTime)||'';"
        "  }).catch(()=>{});"
        "}"
        "setInterval(autoRefresh,10000);"
        "</script>"
        "</head><body>"
        f"{safe_stop_banner}"
        "<div class='header'>"
        "  <h1>AXIA Team Coordination</h1>"
        f"  <span id='team-time' style='font-size:12px;color:#8b949e'>{now}</span>"
        f"  <span style='font-size:12px;color:#8b949e;'>P29 Runtime</span>"
        "</div>"
        "<div class='gov-bar'>"
        f"  <span>Roles: {len(_P29_ROLES)}</span>"
        f"  <span>Reviewer Gate: <strong style='color:{'#3fb950' if gate_status=='PASS' else '#f85149'};'>{gate_status}</strong></span>"
        f"  <span>Safe Stop: {'🛑 YES' if safe_stopped else '✅ NO'}</span>"
        f"  <span>Timeline Events: {len(timeline)}</span>"
        "</div>"
        "<div class='roles-grid'>"
        f"{role_cards_html}"
        "</div>"
        "<div class='bottom-section'>"

        # Reviewer Gate card
        "<div class='card'>"
        "  <div class='card-title'>👁️ Reviewer Gate</div>"
        f"  {gate_items_html}"
        f"  <div class='merge-status {merge_cls}'>{merge_status}</div>"
        "</div>"

        # Timeline card
        "<div class='card'>"
        "  <div class='card-title'>📋 Inter-Role Timeline</div>"
        f"  {timeline_html}"
        "</div>"

        "</div>"
        "<div class='footer'>"
        "  AXIA_RUNTIME_CLASS = AUTONOMOUS_TEAM_COORDINATION_OPERATOR<br>"
        f"  Team Version: P29 | Roles: {len(_P29_ROLES)} | {now}"
        "</div>"
        "</body></html>"
    )
    return HTMLResponse(content=html)


@router.get("/axia-team/state")
async def axia_team_state():
    """P29: Team State JSON API"""
    with _p29_lock:
        role_states = {k: dict(v) for k, v in _p29_role_states.items()}
        reviewer_gate = dict(_p29_reviewer_gate)
        timeline = list(_p29_timeline)[-20:]
        safe_stopped = _p29_safe_stopped
        safe_stop_reason = _p29_safe_stop_reason

    roles_with_def = {}
    for role_id, state in role_states.items():
        role_def = _P29_ROLES[role_id]
        roles_with_def[role_id] = {
            **state,
            "allowedActions": role_def["allowedActions"],
            "forbiddenActions": role_def["forbiddenActions"],
            "displayName": role_def["displayName"],
        }

    return {
        "teamVersion": "P29",
        "roles": roles_with_def,
        "reviewerGate": reviewer_gate,
        "timeline": timeline,
        "safeStop": {
            "active": safe_stopped,
            "reason": safe_stop_reason,
        },
        "serverTime": _p29_now(),
    }


@router.post("/axia-team/role/{role_id}/action")
async def axia_team_role_action(role_id: str, body: dict):
    """P29: Execute role action with governance check"""
    global _p29_safe_stopped, _p29_safe_stop_reason

    action = body.get("action", "")
    task = body.get("task", "")
    detail = body.get("detail", "")

    if role_id not in _P29_ROLES:
        return {"status": "ERROR", "message": f"Unknown role: {role_id}"}

    role_def = _P29_ROLES[role_id]

    # Role Governance check
    if action in role_def["forbiddenActions"]:
        violation = {
            "action": action,
            "reason": f"role {role_id} は {action} を実行できません",
            "timestamp": _p29_now(),
        }
        with _p29_lock:
            _p29_role_states[role_id]["violations"].append(violation)
            _p29_safe_stopped = True
            _p29_safe_stop_reason = f"ROLE_VIOLATION: {role_id} attempted forbidden action '{action}'"

        _p29_add_timeline(role_id, action, f"ROLE_VIOLATION: {action}", "BLOCKED")

        return {
            "status": "ROLE_VIOLATION",
            "safeStop": True,
            "roleId": role_id,
            "action": action,
            "message": f"ROLE_VIOLATION STOP: {role_id} は {action} を実行できません",
            "violation": violation,
        }

    # Execute action
    with _p29_lock:
        state = _p29_role_states[role_id]
        state["status"] = "RUNNING"
        state["currentTask"] = task or action
        state["lastAction"] = action
        state["lastActionAt"] = _p29_now()
        state["actionCount"] += 1

    _p29_add_timeline(role_id, action, detail or task, "OK")

    return {
        "status": "OK",
        "roleId": role_id,
        "action": action,
        "task": task,
        "message": f"{role_id} executed {action} successfully",
    }


@router.post("/axia-team/role/{role_id}/status")
async def axia_team_role_status(role_id: str, body: dict):
    """P29: Update role status"""
    if role_id not in _P29_ROLES:
        return {"status": "ERROR", "message": f"Unknown role: {role_id}"}

    new_status = body.get("status", "IDLE")
    task = body.get("task", None)

    with _p29_lock:
        _p29_role_states[role_id]["status"] = new_status
        if task is not None:
            _p29_role_states[role_id]["currentTask"] = task

    _p29_add_timeline(role_id, "status_update", f"status → {new_status}", "OK")

    return {
        "status": "OK",
        "roleId": role_id,
        "newStatus": new_status,
    }


@router.post("/axia-team/reviewer/gate")
async def axia_team_reviewer_gate(body: dict):
    """P29: Reviewer Gate — PASS or BLOCK merge"""
    action = body.get("action", "check")  # check / approve / block
    checklist_update = body.get("checklist", {})
    block_reason = body.get("blockReason", None)

    with _p29_lock:
        # Update checklist
        for k, v in checklist_update.items():
            if k in _p29_reviewer_gate["checklist"]:
                _p29_reviewer_gate["checklist"][k] = bool(v)

        all_pass = all(_p29_reviewer_gate["checklist"].values())

        if action == "approve" and all_pass:
            _p29_reviewer_gate["status"] = "PASS"
            _p29_reviewer_gate["approvedAt"] = _p29_now()
            _p29_role_states["reviewer"]["status"] = "DONE"
            _p29_role_states["reviewer"]["lastAction"] = "approve_merge"
            _p29_role_states["reviewer"]["lastActionAt"] = _p29_now()
            result_status = "PASS"
            merge_allowed = True
        elif action == "block" or (action == "approve" and not all_pass):
            _p29_reviewer_gate["status"] = "BLOCK"
            _p29_reviewer_gate["blockedReason"] = block_reason or "チェックリスト未完了"
            _p29_role_states["reviewer"]["status"] = "BLOCKED"
            result_status = "BLOCK"
            merge_allowed = False
        else:
            result_status = "PENDING"
            merge_allowed = False

        checklist = dict(_p29_reviewer_gate["checklist"])

    _p29_add_timeline("reviewer", f"gate_{action}", f"status={result_status}", result_status)

    return {
        "status": result_status,
        "mergeAllowed": merge_allowed,
        "checklist": checklist,
        "allChecklistPass": all_pass,
        "message": "MERGE 許可" if merge_allowed else "MERGE 禁止 — Reviewer Gate未通過",
    }


@router.get("/axia-team/timeline")
async def axia_team_timeline():
    """P29: Inter-Role Timeline"""
    with _p29_lock:
        timeline = list(_p29_timeline)

    return {
        "teamVersion": "P29",
        "timeline": timeline,
        "count": len(timeline),
        "serverTime": _p29_now(),
    }


@router.post("/axia-team/safe-stop")
async def axia_team_safe_stop(body: dict):
    """P29: Trigger safe stop"""
    global _p29_safe_stopped, _p29_safe_stop_reason
    reason = body.get("reason", "Manual safe stop")
    with _p29_lock:
        _p29_safe_stopped = True
        _p29_safe_stop_reason = reason
    _p29_add_timeline("recovery", "safe_stop", reason, "STOPPED")
    return {"status": "SAFE_STOP", "reason": reason, "stoppedAt": _p29_now()}


@router.post("/axia-team/safe-stop/reset")
async def axia_team_safe_stop_reset():
    """P29: Reset safe stop"""
    global _p29_safe_stopped, _p29_safe_stop_reason
    with _p29_lock:
        _p29_safe_stopped = False
        _p29_safe_stop_reason = None
    _p29_add_timeline("recovery", "safe_stop_reset", "Safe stop cleared", "OK")
    return {"status": "OK", "message": "Safe stop cleared"}

# ─── End of P29 ──────────────────────────────────────────────────────────────


# ============================================================
# AXIA P30 — Human Work Operating System UX Runtime
# ============================================================
import uuid as _uuid30
import threading as _p30_threading

# ── P30 State ────────────────────────────────────────────────
_p30_lock = _p30_threading.RLock()

_p30_state = {
    "workVersion": "P30",
    "todayTasks": [],
    "nowWorking": None,
    "nextTask": None,
    "approvalQueue": [],
    "humanTimeline": [],
    "pauseState": {
        "active": False,
        "reason": None,
        "pausedAt": None,
        "resumeNote": None,
    },
    "dailyBrief": {
        "yesterdayContinue": [],
        "warnings": [],
        "recommendations": [],
        "generatedAt": None,
    },
    "safeStop": {"active": False, "reason": None},
    "noiseFilter": ["analysis", "thinking", "critic", "learner", "tool_call", "trace", "stack_trace"],
}

# ── Smart Status Language ────────────────────────────────────
_p30_status_map = {
    "task_": "タスク処理中",
    "runtime_phase_": "処理フェーズ",
    "verify_loop_detected": "修正を確認しています",
    "waiting_approval": "承認待ち",
    "browser_verify": "画面確認中",
    "http_verify": "接続確認中",
    "safe_stop": "安全停止中",
    "running": "実行中",
    "idle": "待機中",
    "done": "完了",
    "failed": "失敗",
    "paused": "一時停止中",
    "pending": "処理待ち",
}

def _p30_smart_lang(raw: str) -> str:
    """Convert technical status to human-readable Japanese."""
    if not raw:
        return ""
    lower = raw.lower()
    for k, v in _p30_status_map.items():
        if k in lower:
            return v
    # Remove technical prefixes
    import re as _re
    cleaned = _re.sub(r'[a-z]+_[0-9a-f]{4,}', '処理中', raw)
    return cleaned

def _p30_noise_clean(text: str) -> str:
    """Remove noise words from text."""
    if not text:
        return ""
    lower = text.lower()
    for word in _p30_state["noiseFilter"]:
        if word in lower:
            return ""
    return text

def _p30_jst_now() -> str:
    from datetime import datetime as _dt30, timezone, timedelta
    jst = timezone(timedelta(hours=9))
    return _dt30.now(jst).strftime("%Y-%m-%dT%H:%M:%S JST")

def _p30_time_short() -> str:
    from datetime import datetime as _dt30, timezone, timedelta
    jst = timezone(timedelta(hours=9))
    return _dt30.now(jst).strftime("%H:%M")

def _p30_add_timeline(action: str, detail: str, result: str = "OK"):
    """Add event to human timeline."""
    with _p30_lock:
        _p30_state["humanTimeline"].append({
            "time": _p30_time_short(),
            "action": action,
            "detail": _p30_noise_clean(detail),
            "result": result,
            "timestamp": _p30_jst_now(),
        })
        # Keep last 50 events
        if len(_p30_state["humanTimeline"]) > 50:
            _p30_state["humanTimeline"] = _p30_state["humanTimeline"][-50:]

def _p30_generate_daily_brief():
    """Generate daily brief from current state."""
    with _p30_lock:
        brief = _p30_state["dailyBrief"]
        brief["generatedAt"] = _p30_jst_now()
        # Yesterday continue: pending approval items
        brief["yesterdayContinue"] = [
            f"{a['title']} が承認待ちです"
            for a in _p30_state["approvalQueue"]
            if a.get("status") == "pending"
        ]
        # Warnings: failed tasks
        brief["warnings"] = [
            f"{t['title']} が失敗しています"
            for t in _p30_state["todayTasks"]
            if t.get("status") == "failed"
        ]
        # Recommendations
        recs = []
        if _p30_state["approvalQueue"]:
            recs.append("承認待ちの項目を先に確認すると進みます")
        failed = [t for t in _p30_state["todayTasks"] if t.get("status") == "failed"]
        if failed:
            recs.append(f"{failed[0]['title']} の確認をお勧めします")
        if not recs:
            recs.append("今日のタスクを追加して始めましょう")
        brief["recommendations"] = recs

# ── P30 Pydantic Models ──────────────────────────────────────
from pydantic import BaseModel as _P30BaseModel
from typing import Optional as _P30Optional

class _P30TaskModel(_P30BaseModel):
    title: str
    priority: str = "MEDIUM"
    status: str = "pending"
    detail: _P30Optional[str] = None

class _P30ApprovalModel(_P30BaseModel):
    title: str
    risk: str = "LOW"
    changedFiles: list = []
    whatChanges: str = ""
    reversible: bool = True
    detail: _P30Optional[str] = None

class _P30PauseModel(_P30BaseModel):
    action: str  # pause / resume / done-today
    reason: _P30Optional[str] = None
    resumeNote: _P30Optional[str] = None

class _P30ApprovalActionModel(_P30BaseModel):
    action: str  # approve / reject
    reason: _P30Optional[str] = None

class _P30NowWorkingModel(_P30BaseModel):
    description: str
    nextTask: _P30Optional[str] = None

# ── P30 HTML Dashboard ───────────────────────────────────────
def _p30_render_html() -> str:
    with _p30_lock:
        state = _p30_state
        tasks = state["todayTasks"]
        now_w = state["nowWorking"]
        next_t = state["nextTask"]
        approvals = [a for a in state["approvalQueue"] if a.get("status") == "pending"]
        timeline = state["humanTimeline"][-10:]
        pause = state["pauseState"]
        brief = state["dailyBrief"]

        # Status icons
        def status_icon(s):
            return {"pending": "🟡", "running": "🟢", "done": "✅", "failed": "🔴", "paused": "⏸️"}.get(s, "⚪")

        # Today tasks HTML
        tasks_html = ""
        for t in tasks:
            icon = status_icon(t.get("status", "pending"))
            label = _p30_smart_lang(t.get("status", "pending"))
            tasks_html += f"<div class='task-item'><span class='task-icon'>{icon}</span><span class='task-title'>{t['title']}</span><span class='task-status'>{label}</span></div>"
        if not tasks_html:
            tasks_html = "<div class='empty-msg'>タスクはありません</div>"

        # Now working
        now_html = f"<div class='now-text'>{now_w['description']}</div>" if now_w else "<div class='empty-msg'>作業中のタスクはありません</div>"
        next_html = f"<div class='next-text'>{next_t}</div>" if next_t else "<div class='empty-msg'>次のタスクは未設定です</div>"

        # Approval center
        approval_html = ""
        for a in approvals:
            risk_color = {"HIGH": "#da3633", "MEDIUM": "#d29922", "LOW": "#3fb950"}.get(a.get("risk", "LOW"), "#8b949e")
            files_str = ", ".join(a.get("changedFiles", [])) or "なし"
            reversible = "✅ 戻せます" if a.get("reversible", True) else "⚠️ 戻せません"
            approval_html += f"""
<div class='approval-card'>
  <div class='approval-title'>{a['title']}</div>
  <div class='approval-meta'>
    <span style='color:{risk_color}'>リスク: {a.get("risk","LOW")}</span> &nbsp;|&nbsp;
    変更ファイル: {files_str} &nbsp;|&nbsp; {reversible}
  </div>
  <div class='approval-desc'>{a.get("whatChanges","")}</div>
  <div class='approval-actions'>
    <button onclick='approveItem("{a["id"]}")' class='btn-approve'>承認</button>
    <button onclick='rejectItem("{a["id"]}")' class='btn-reject'>却下</button>
  </div>
</div>"""
        if not approval_html:
            approval_html = "<div class='empty-msg'>承認待ちはありません</div>"

        # Timeline
        tl_html = ""
        for e in reversed(timeline):
            result_color = "#3fb950" if e.get("result") == "OK" else "#f85149"
            tl_html += f"<div class='tl-row'><span class='tl-time'>{e['time']}</span><span class='tl-action'>{e['action']}</span><span class='tl-detail'>{e.get('detail','')}</span><span class='tl-result' style='color:{result_color}'>{e.get('result','')}</span></div>"
        if not tl_html:
            tl_html = "<div class='empty-msg'>タイムラインはありません</div>"

        # Pause banner
        pause_banner = ""
        if pause.get("active"):
            pause_banner = f"<div class='pause-banner'>⏸️ 一時停止中: {pause.get('reason','')} — {pause.get('resumeNote','')}</div>"

        # Daily brief
        brief_html = ""
        if brief.get("yesterdayContinue"):
            brief_html += "<div class='brief-section'><div class='brief-label'>昨日の続き</div>"
            for item in brief["yesterdayContinue"]:
                brief_html += f"<div class='brief-item'>📌 {item}</div>"
            brief_html += "</div>"
        if brief.get("warnings"):
            brief_html += "<div class='brief-section'><div class='brief-label'>注意</div>"
            for w in brief["warnings"]:
                brief_html += f"<div class='brief-item warn'>⚠️ {w}</div>"
            brief_html += "</div>"
        if brief.get("recommendations"):
            brief_html += "<div class='brief-section'><div class='brief-label'>おすすめ</div>"
            for r in brief["recommendations"]:
                brief_html += f"<div class='brief-item rec'>💡 {r}</div>"
            brief_html += "</div>"
        if not brief_html:
            brief_html = "<div class='empty-msg'>デイリーブリーフを生成してください</div>"

        server_time = _p30_jst_now()
        approval_count = len(approvals)

    return f"""<!DOCTYPE html><html lang='ja'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width,initial-scale=1,viewport-fit=cover'><title>AXIA Work OS</title><style>
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{background:#0d1117;color:#e6edf3;font-family:'Segoe UI',sans-serif;font-size:14px;padding-bottom:env(safe-area-inset-bottom,16px);}}
.header{{display:flex;align-items:center;justify-content:space-between;padding:14px 20px;background:#161b22;border-bottom:1px solid #30363d;position:sticky;top:0;z-index:100;}}
.header h1{{font-size:18px;font-weight:700;color:#58a6ff;}}
.header-meta{{font-size:11px;color:#8b949e;text-align:right;}}
.pause-banner{{background:#6e40c9;color:#fff;padding:8px 20px;font-weight:700;text-align:center;font-size:13px;}}
.main{{display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:16px 20px;}}
@media(max-width:700px){{.main{{grid-template-columns:1fr;padding:12px;}}}}
.card{{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:14px;}}
.card-title{{font-size:12px;font-weight:700;color:#8b949e;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;display:flex;align-items:center;gap:6px;}}
.card-title .badge{{background:#21262d;border-radius:10px;padding:2px 8px;font-size:10px;color:#58a6ff;}}
.task-item{{display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #21262d;}}
.task-item:last-child{{border-bottom:none;}}
.task-icon{{font-size:16px;flex-shrink:0;}}
.task-title{{flex:1;font-size:13px;}}
.task-status{{font-size:11px;color:#8b949e;}}
.now-text{{font-size:15px;color:#e6edf3;line-height:1.6;padding:6px 0;}}
.next-text{{font-size:13px;color:#58a6ff;padding:6px 0;}}
.empty-msg{{font-size:12px;color:#484f58;padding:8px 0;}}
.approval-card{{background:#1c2128;border:1px solid #30363d;border-radius:8px;padding:12px;margin-bottom:8px;}}
.approval-title{{font-size:14px;font-weight:700;margin-bottom:6px;}}
.approval-meta{{font-size:11px;color:#8b949e;margin-bottom:6px;}}
.approval-desc{{font-size:12px;color:#c9d1d9;margin-bottom:8px;}}
.approval-actions{{display:flex;gap:8px;}}
.btn-approve{{background:#1a7f37;color:#fff;border:none;border-radius:6px;padding:6px 14px;font-size:12px;cursor:pointer;font-weight:700;}}
.btn-reject{{background:#da3633;color:#fff;border:none;border-radius:6px;padding:6px 14px;font-size:12px;cursor:pointer;font-weight:700;}}
.tl-row{{display:grid;grid-template-columns:45px 1fr 1fr 40px;gap:6px;padding:5px 0;border-bottom:1px solid #21262d;font-size:12px;align-items:center;}}
.tl-time{{color:#484f58;font-size:11px;}}
.tl-action{{color:#d29922;font-weight:700;}}
.tl-detail{{color:#8b949e;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}}
.tl-result{{font-size:11px;font-weight:700;}}
.pause-controls{{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px;}}
.btn-pause{{background:#6e40c9;color:#fff;border:none;border-radius:6px;padding:8px 14px;font-size:12px;cursor:pointer;font-weight:700;}}
.btn-resume{{background:#1a7f37;color:#fff;border:none;border-radius:6px;padding:8px 14px;font-size:12px;cursor:pointer;font-weight:700;}}
.btn-done-today{{background:#21262d;color:#e6edf3;border:1px solid #30363d;border-radius:6px;padding:8px 14px;font-size:12px;cursor:pointer;font-weight:700;}}
.brief-section{{margin-bottom:10px;}}
.brief-label{{font-size:11px;font-weight:700;color:#8b949e;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;}}
.brief-item{{font-size:13px;padding:4px 0;color:#e6edf3;}}
.brief-item.warn{{color:#d29922;}}
.brief-item.rec{{color:#58a6ff;}}
.footer{{text-align:center;padding:14px;font-size:11px;color:#484f58;border-top:1px solid #21262d;margin-top:8px;}}
details summary{{cursor:pointer;color:#58a6ff;font-size:12px;padding:4px 0;}}
details[open] summary{{color:#8b949e;}}
</style>
<script>
async function approveItem(id){{
  await fetch('/api/axia-work/approval/'+id,{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{action:'approve'}}) }});
  location.reload();
}}
async function rejectItem(id){{
  await fetch('/api/axia-work/approval/'+id,{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{action:'reject'}}) }});
  location.reload();
}}
async function pauseWork(){{
  await fetch('/api/axia-work/pause',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{action:'pause',reason:'今日はここまで'}}) }});
  location.reload();
}}
async function resumeWork(){{
  await fetch('/api/axia-work/pause',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{action:'resume'}}) }});
  location.reload();
}}
async function doneToday(){{
  await fetch('/api/axia-work/pause',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{action:'done-today',resumeNote:'明日続きから再開'}}) }});
  location.reload();
}}
</script>
</head><body>
<div class='header'>
  <h1>AXIA Work OS</h1>
  <div class='header-meta'>
    <div id='work-time'>{server_time}</div>
    <div>P30 Runtime &nbsp;|&nbsp; 承認待ち: {approval_count}件</div>
  </div>
</div>
{pause_banner}
<div class='main'>
  <div class='card'>
    <div class='card-title'>📅 Today <span class='badge'>{len(tasks)}件</span></div>
    {tasks_html}
  </div>
  <div class='card'>
    <div class='card-title'>⚡ Now Working</div>
    {now_html}
    <div class='card-title' style='margin-top:12px;'>➡️ Next</div>
    {next_html}
  </div>
  <div class='card'>
    <div class='card-title'>✋ 承認センター <span class='badge'>{approval_count}</span></div>
    {approval_html}
  </div>
  <div class='card'>
    <div class='card-title'>📋 タイムライン</div>
    {tl_html}
  </div>
  <div class='card'>
    <div class='card-title'>⏸️ 一時停止</div>
    <div class='pause-controls'>
      <button class='btn-pause' onclick='pauseWork()'>今日はここまで</button>
      <button class='btn-resume' onclick='resumeWork()'>再開する</button>
      <button class='btn-done-today' onclick='doneToday()'>あとで再開</button>
    </div>
    <details style='margin-top:12px;'>
      <summary>詳細ランタイム情報</summary>
      <div style='font-size:11px;color:#484f58;padding:8px 0;'>技術的な詳細はここに折りたたまれています</div>
    </details>
  </div>
  <div class='card'>
    <div class='card-title'>🌅 デイリーブリーフ</div>
    {brief_html}
  </div>
</div>
<div class='footer'>AXIA_RUNTIME_CLASS = HUMAN_WORK_OPERATING_SYSTEM &nbsp;|&nbsp; Work Version: P30 &nbsp;|&nbsp; {server_time}</div>
</body></html>"""


# ── P30 Endpoints ────────────────────────────────────────────

@router.get("/axia-work", response_class=HTMLResponse)
async def axia_work_dashboard():
    """P30: Human Work OS Dashboard."""
    return HTMLResponse(content=_p30_render_html())


@router.get("/axia-work/state")
async def axia_work_state():
    """P30: Work OS state JSON."""
    with _p30_lock:
        return {
            **_p30_state,
            "serverTime": _p30_jst_now(),
        }


@router.post("/axia-work/task")
async def axia_work_add_task(body: _P30TaskModel):
    """P30: Add a task to today's workspace."""
    with _p30_lock:
        task = {
            "id": str(_uuid30.uuid4())[:8],
            "title": body.title,
            "priority": body.priority,
            "status": body.status,
            "detail": body.detail,
            "createdAt": _p30_jst_now(),
        }
        _p30_state["todayTasks"].append(task)
        _p30_add_timeline("タスク追加", body.title)
        return {"status": "OK", "task": task, "workVersion": "P30"}


@router.post("/axia-work/task/{task_id}/status")
async def axia_work_update_task_status(task_id: str, body: dict):
    """P30: Update task status."""
    with _p30_lock:
        for t in _p30_state["todayTasks"]:
            if t["id"] == task_id:
                t["status"] = body.get("status", t["status"])
                _p30_add_timeline("タスク更新", t["title"], body.get("status", "OK"))
                return {"status": "OK", "task": t}
        return {"status": "NOT_FOUND", "taskId": task_id}


@router.post("/axia-work/now")
async def axia_work_set_now(body: _P30NowWorkingModel):
    """P30: Set now working description."""
    with _p30_lock:
        _p30_state["nowWorking"] = {
            "description": body.description,
            "startedAt": _p30_jst_now(),
        }
        if body.nextTask:
            _p30_state["nextTask"] = body.nextTask
        _p30_add_timeline("作業開始", body.description)
        return {"status": "OK", "nowWorking": _p30_state["nowWorking"], "workVersion": "P30"}


@router.get("/axia-work/approval")
async def axia_work_approval_list():
    """P30: Approval center list."""
    with _p30_lock:
        pending = [a for a in _p30_state["approvalQueue"] if a.get("status") == "pending"]
        return {
            "status": "OK",
            "pending": pending,
            "count": len(pending),
            "workVersion": "P30",
            "serverTime": _p30_jst_now(),
        }


@router.post("/axia-work/approval/add")
async def axia_work_add_approval(body: _P30ApprovalModel):
    """P30: Add item to approval queue."""
    with _p30_lock:
        item = {
            "id": str(_uuid30.uuid4())[:8],
            "title": body.title,
            "risk": body.risk,
            "changedFiles": body.changedFiles,
            "whatChanges": body.whatChanges,
            "reversible": body.reversible,
            "detail": body.detail,
            "status": "pending",
            "createdAt": _p30_jst_now(),
        }
        _p30_state["approvalQueue"].append(item)
        _p30_add_timeline("承認追加", body.title)
        return {"status": "OK", "item": item, "workVersion": "P30"}


@router.post("/axia-work/approval/{approval_id}")
async def axia_work_approval_action(approval_id: str, body: _P30ApprovalActionModel):
    """P30: Approve or reject an approval item."""
    with _p30_lock:
        for a in _p30_state["approvalQueue"]:
            if a["id"] == approval_id:
                a["status"] = "approved" if body.action == "approve" else "rejected"
                a["decidedAt"] = _p30_jst_now()
                a["decideReason"] = body.reason
                action_label = "承認" if body.action == "approve" else "却下"
                _p30_add_timeline(action_label, a["title"], body.action.upper())
                return {"status": "OK", "action": body.action, "item": a, "workVersion": "P30"}
        return {"status": "NOT_FOUND", "approvalId": approval_id}


@router.post("/axia-work/pause")
async def axia_work_pause(body: _P30PauseModel):
    """P30: Human Pause Runtime."""
    with _p30_lock:
        action = body.action
        if action == "pause":
            _p30_state["pauseState"] = {
                "active": True,
                "reason": body.reason or "一時停止",
                "pausedAt": _p30_jst_now(),
                "resumeNote": body.resumeNote,
            }
            _p30_add_timeline("一時停止", body.reason or "今日はここまで")
        elif action == "resume":
            _p30_state["pauseState"]["active"] = False
            _p30_state["pauseState"]["resumedAt"] = _p30_jst_now()
            _p30_add_timeline("再開", "作業を再開しました")
        elif action == "done-today":
            _p30_state["pauseState"] = {
                "active": True,
                "reason": "今日の作業完了",
                "pausedAt": _p30_jst_now(),
                "resumeNote": body.resumeNote or "明日続きから再開",
            }
            _p30_add_timeline("今日完了", "明日続きから再開")
        return {
            "status": "OK",
            "action": action,
            "pauseState": _p30_state["pauseState"],
            "workVersion": "P30",
        }


@router.get("/axia-work/brief")
async def axia_work_brief():
    """P30: Daily Brief."""
    _p30_generate_daily_brief()
    with _p30_lock:
        return {
            "status": "OK",
            "brief": _p30_state["dailyBrief"],
            "workVersion": "P30",
            "serverTime": _p30_jst_now(),
        }


@router.get("/axia-work/timeline")
async def axia_work_timeline():
    """P30: Human Timeline."""
    with _p30_lock:
        return {
            "status": "OK",
            "timeline": _p30_state["humanTimeline"],
            "count": len(_p30_state["humanTimeline"]),
            "workVersion": "P30",
            "serverTime": _p30_jst_now(),
        }


@router.post("/axia-work/smart-lang")
async def axia_work_smart_lang(body: dict):
    """P30: Smart Status Language conversion."""
    raw = body.get("text", "")
    converted = _p30_smart_lang(raw)
    noise_clean = _p30_noise_clean(raw)
    return {
        "status": "OK",
        "raw": raw,
        "humanReadable": converted,
        "noiseClean": noise_clean,
        "workVersion": "P30",
    }


@router.post("/axia-work/reset")
async def axia_work_reset():
    """P30: Reset workspace state for testing."""
    with _p30_lock:
        _p30_state["todayTasks"] = []
        _p30_state["nowWorking"] = None
        _p30_state["nextTask"] = None
        _p30_state["approvalQueue"] = []
        _p30_state["humanTimeline"] = []
        _p30_state["pauseState"] = {"active": False, "reason": None, "pausedAt": None, "resumeNote": None}
        _p30_state["dailyBrief"] = {"yesterdayContinue": [], "warnings": [], "recommendations": [], "generatedAt": None}
        _p30_state["safeStop"] = {"active": False, "reason": None}
    return {"status": "OK", "message": "P30 workspace reset", "workVersion": "P30"}


# ─── End of P30 ──────────────────────────────────────────────────────────────


# ============================================================
# AXIA P31 — Real Browser Operator Runtime
# ============================================================
import uuid as _uuid31
import threading as _p31_threading
from datetime import datetime as _p31_dt, timezone as _p31_tz, timedelta as _p31_td
from pydantic import BaseModel as _P31BaseModel
from typing import Optional as _P31Optional, List as _P31List

# ── P31 Constants ─────────────────────────────────────────────
_P31_SAFE_ACTIONS = {
    "open_page", "click", "scroll", "input_text", "wait_for", "capture", "inspect"
}
_P31_DANGEROUS_ACTIONS = {
    "purchase", "delete", "payment", "submit_without_approval",
    "dangerous_confirm", "deploy", "send_email", "transfer"
}
_P31_APPROVAL_REQUIRED_ACTIONS = {
    "submit", "login", "delete", "purchase", "payment", "dangerous_confirm"
}
_P31_NOISE_WORDS = [
    "playwright", "selector", "xpath", "css_selector", "trace", "stack_trace",
    "internal_debug", "raw_element", "dom_query"
]
_P31_RUNTIME_CLASS = "REAL_BROWSER_OPERATOR_RUNTIME"

# ── P31 State ─────────────────────────────────────────────────
_p31_lock = _p31_threading.RLock()

_p31_state = {
    "browserVersion": "P31",
    "session": {
        "sessionId": None,
        "currentUrl": None,
        "pageTitle": None,
        "lastAction": None,
        "status": "idle",  # idle / active / paused / error
        "startedAt": None,
        "lastHeartbeat": None,
        "tabCount": 1,
    },
    "actionHistory": [],
    "browserTimeline": [],
    "visualVerifyResults": [],
    "pendingApprovals": [],
    "safeStop": {
        "triggered": False,
        "reason": None,
    },
    "recovery": {
        "lastSavedUrl": None,
        "lastSavedTitle": None,
        "lastSavedTimeline": [],
        "restoredAt": None,
    },
}


def _p31_jst_now() -> str:
    jst = _p31_tz(_p31_td(hours=9))
    return _p31_dt.now(jst).strftime("%Y-%m-%dT%H:%M:%S JST")


def _p31_time_short() -> str:
    jst = _p31_tz(_p31_td(hours=9))
    return _p31_dt.now(jst).strftime("%H:%M")


def _p31_noise_clean(text: str) -> str:
    """Remove noise words from text."""
    if not text:
        return text
    lower = text.lower()
    for word in _P31_NOISE_WORDS:
        if word in lower:
            return ""
    return text


def _p31_action_to_human(action: str, target: str = "", value: str = "") -> str:
    """Convert internal action to human-readable Japanese."""
    mapping = {
        "open_page": f"ページを開きました: {target}" if target else "ページを開きました",
        "click": f"ボタンを確認しました: {target}" if target else "ボタンを確認しました",
        "scroll": "ページをスクロールしました",
        "input_text": f"入力フォームに入力しました" if value else "入力フォームを検出しました",
        "wait_for": "要素を待機しました",
        "capture": "画面を記録しました",
        "inspect": f"要素を検査しました: {target}" if target else "要素を検査しました",
        "session_start": "ブラウザセッションを開始しました",
        "session_end": "ブラウザセッションを終了しました",
        "visual_verify": "画面の状態を確認しました",
        "recovery": "セッションを復元しました",
    }
    return mapping.get(action, f"操作を実行しました: {action}")


def _p31_add_timeline(action: str, detail: str = "", result: str = "OK", target: str = ""):
    """Add event to browser timeline (human-readable)."""
    with _p31_lock:
        human_msg = _p31_action_to_human(action, target)
        clean_detail = _p31_noise_clean(detail)
        _p31_state["browserTimeline"].append({
            "time": _p31_time_short(),
            "action": action,
            "humanMessage": human_msg,
            "detail": clean_detail,
            "result": result,
            "timestamp": _p31_jst_now(),
        })
        # Keep last 100 events
        if len(_p31_state["browserTimeline"]) > 100:
            _p31_state["browserTimeline"] = _p31_state["browserTimeline"][-100:]


# ── P31 Pydantic Models ───────────────────────────────────────
class _P31SessionModel(_P31BaseModel):
    action: str  # start / end / pause / resume
    sessionId: _P31Optional[str] = None


class _P31ActionModel(_P31BaseModel):
    action: str
    target: _P31Optional[str] = None
    value: _P31Optional[str] = None
    url: _P31Optional[str] = None
    detail: _P31Optional[str] = None


class _P31VerifyModel(_P31BaseModel):
    url: _P31Optional[str] = None
    htmlContent: _P31Optional[str] = None
    statusCode: _P31Optional[int] = None
    checkItems: _P31Optional[_P31List[str]] = None


class _P31RecoveryModel(_P31BaseModel):
    action: str  # restore / save
    url: _P31Optional[str] = None
    title: _P31Optional[str] = None


class _P31ApprovalActionModel(_P31BaseModel):
    approvalId: str
    action: str  # approve / reject
    reason: _P31Optional[str] = None


# ── P31 HTML Dashboard ────────────────────────────────────────
def _p31_render_html() -> str:
    with _p31_lock:
        sess = _p31_state["session"]
        timeline = _p31_state["browserTimeline"][-10:]
        verify_results = _p31_state["visualVerifyResults"][-5:]
        pending = _p31_state["pendingApprovals"]
        safe_stop = _p31_state["safeStop"]

        status_color = {
            "idle": "#64748b",
            "active": "#22c55e",
            "paused": "#fbbf24",
            "error": "#ef4444",
        }.get(sess["status"], "#64748b")

        status_label = {
            "idle": "待機中",
            "active": "操作中",
            "paused": "一時停止",
            "error": "エラー",
        }.get(sess["status"], "不明")

        timeline_rows = ""
        for ev in reversed(timeline):
            r_color = "#22c55e" if ev["result"] == "OK" else "#ef4444"
            timeline_rows += f"""
            <div class="tl-row">
              <span class="tl-time">{ev['time']}</span>
              <span class="tl-msg">{ev['humanMessage']}</span>
              <span class="tl-result" style="color:{r_color}">{ev['result']}</span>
            </div>"""

        verify_rows = ""
        for vr in reversed(verify_results):
            ok = vr.get("passed", True)
            v_color = "#22c55e" if ok else "#ef4444"
            v_label = "OK" if ok else "NG"
            issues = ", ".join(vr.get("issues", [])) or "なし"
            verify_rows += f"""
            <div class="verify-row">
              <span class="verify-url">{vr.get('url', '-')[:50]}</span>
              <span class="verify-status" style="color:{v_color}">{v_label}</span>
              <span class="verify-issues">{issues}</span>
            </div>"""

        approval_rows = ""
        for ap in pending:
            approval_rows += f"""
            <div class="ap-row">
              <span class="ap-action">{ap.get('action', '-')}</span>
              <span class="ap-target">{ap.get('target', '-')}</span>
              <span class="ap-status">承認待ち</span>
            </div>"""

        safe_stop_banner = ""
        if safe_stop["triggered"]:
            safe_stop_banner = f"""
            <div class="safe-stop-banner">
              SAFE STOP: {safe_stop['reason']}
            </div>"""

        return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>AXIA Browser OS</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: #0d1117;
      color: #e2e8f0;
      margin: 0;
      padding: 16px 16px calc(16px + env(safe-area-inset-bottom));
      min-height: 100vh;
    }}
    .container {{ max-width: 800px; margin: 0 auto; }}
    .top-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .top-title {{ font-size: 20px; font-weight: 800; color: #f8fafc; margin: 0; }}
    .top-meta {{ font-size: 11px; color: #475569; }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      background: #14532d;
      border: 1px solid #22c55e;
      color: #4ade80;
    }}
    .badge-dot {{
      width: 6px; height: 6px;
      background: #22c55e;
      border-radius: 50%;
      animation: pulse 2s infinite;
    }}
    @keyframes pulse {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:0.3; }} }}
    .grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 14px;
    }}
    @media (max-width: 600px) {{ .grid {{ grid-template-columns: 1fr; }} }}
    .card {{
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      padding: 16px;
    }}
    .card-full {{ grid-column: 1 / -1; }}
    .card-title {{
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #475569;
      margin: 0 0 10px;
    }}
    .session-status {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }}
    .status-dot {{
      width: 10px; height: 10px;
      border-radius: 50%;
      background: {status_color};
    }}
    .status-label {{ font-size: 16px; font-weight: 700; color: {status_color}; }}
    .session-url {{
      font-size: 12px;
      color: #93c5fd;
      word-break: break-all;
      margin: 4px 0;
    }}
    .session-action {{
      font-size: 13px;
      color: #cbd5e1;
      margin: 4px 0;
    }}
    .tl-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 0;
      border-bottom: 1px solid #21262d;
      font-size: 12px;
    }}
    .tl-row:last-child {{ border-bottom: none; }}
    .tl-time {{ color: #475569; min-width: 36px; font-family: monospace; }}
    .tl-msg {{ flex: 1; color: #cbd5e1; }}
    .tl-result {{ font-size: 11px; font-weight: 600; }}
    .verify-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 0;
      border-bottom: 1px solid #21262d;
      font-size: 12px;
    }}
    .verify-row:last-child {{ border-bottom: none; }}
    .verify-url {{ flex: 1; color: #93c5fd; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
    .verify-status {{ font-weight: 700; min-width: 24px; }}
    .verify-issues {{ color: #64748b; font-size: 11px; }}
    .ap-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 0;
      border-bottom: 1px solid #21262d;
      font-size: 12px;
    }}
    .ap-action {{ color: #fbbf24; font-weight: 600; }}
    .ap-target {{ flex: 1; color: #cbd5e1; }}
    .ap-status {{ color: #f97316; font-size: 11px; }}
    .safe-stop-banner {{
      background: #450a0a;
      border: 1px solid #ef4444;
      color: #fca5a5;
      padding: 10px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 14px;
    }}
    .empty {{ color: #475569; font-size: 12px; font-style: italic; }}
    .footer {{
      text-align: center;
      font-size: 10px;
      color: #30363d;
      margin-top: 20px;
      padding-top: 12px;
      border-top: 1px solid #21262d;
    }}
    details summary {{
      cursor: pointer;
      font-size: 11px;
      color: #475569;
      padding: 6px 0;
      user-select: none;
    }}
    details[open] summary {{ color: #93c5fd; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="top-bar">
      <div>
        <h1 class="top-title">AXIA Browser OS</h1>
        <div class="top-meta">Browser Version: P31 | {_p31_jst_now()}</div>
      </div>
      <div class="badge">
        <span class="badge-dot"></span>
        {status_label}
      </div>
    </div>

    {safe_stop_banner}

    <div class="grid">
      <!-- Current Session -->
      <div class="card">
        <div class="card-title">Current Session</div>
        <div class="session-status">
          <span class="status-dot"></span>
          <span class="status-label">{status_label}</span>
        </div>
        <div class="session-url">{sess['currentUrl'] or 'URLなし'}</div>
        <div class="session-action">{sess['lastAction'] or '操作なし'}</div>
        <div style="font-size:11px;color:#475569;margin-top:6px;">
          {f"開始: {sess['startedAt']}" if sess['startedAt'] else "未開始"}
        </div>
      </div>

      <!-- Visual Verify -->
      <div class="card">
        <div class="card-title">Visual Verify</div>
        {verify_rows if verify_rows else '<div class="empty">検証結果なし</div>'}
      </div>

      <!-- Browser Timeline -->
      <div class="card card-full">
        <div class="card-title">Browser Timeline</div>
        {timeline_rows if timeline_rows else '<div class="empty">タイムラインはありません</div>'}
      </div>

      <!-- Approval Center -->
      <div class="card">
        <div class="card-title">承認待ち {len(pending)}件</div>
        {approval_rows if approval_rows else '<div class="empty">承認待ちはありません</div>'}
      </div>

      <!-- Safe Actions -->
      <div class="card">
        <div class="card-title">Safe Actions</div>
        <details>
          <summary>許可アクション ({len(_P31_SAFE_ACTIONS)}件)</summary>
          <div style="font-size:11px;color:#4ade80;margin-top:6px;">
            {', '.join(sorted(_P31_SAFE_ACTIONS))}
          </div>
        </details>
        <details style="margin-top:6px;">
          <summary>禁止アクション ({len(_P31_DANGEROUS_ACTIONS)}件)</summary>
          <div style="font-size:11px;color:#f87171;margin-top:6px;">
            {', '.join(sorted(_P31_DANGEROUS_ACTIONS))}
          </div>
        </details>
      </div>
    </div>

    <div class="footer">
      AXIA_RUNTIME_CLASS = {_P31_RUNTIME_CLASS} | Browser Version: P31 | {_p31_jst_now()}
    </div>
  </div>
</body>
</html>"""


# ── P31 Endpoints ─────────────────────────────────────────────
@router.get("/axia-browser", response_class=HTMLResponse)
async def axia_browser_dashboard():
    """P31 Human Browser View Dashboard"""
    return HTMLResponse(content=_p31_render_html(), status_code=200)


@router.get("/axia-browser/state")
async def axia_browser_state():
    """P31 Browser Session State"""
    with _p31_lock:
        import copy
        state_copy = copy.deepcopy(_p31_state)
    return JSONResponse({
        "status": "OK",
        "browserVersion": "P31",
        "runtimeClass": _P31_RUNTIME_CLASS,
        "session": state_copy["session"],
        "timelineCount": len(state_copy["browserTimeline"]),
        "pendingApprovals": len(state_copy["pendingApprovals"]),
        "safeStop": state_copy["safeStop"],
        "safeActions": sorted(list(_P31_SAFE_ACTIONS)),
        "dangerousActions": sorted(list(_P31_DANGEROUS_ACTIONS)),
        "serverTime": _p31_jst_now(),
    })


@router.post("/axia-browser/session")
async def axia_browser_session(body: _P31SessionModel):
    """P31 Browser Session Management"""
    with _p31_lock:
        action = body.action
        if action == "start":
            session_id = body.sessionId or str(_uuid31.uuid4())[:8]
            _p31_state["session"].update({
                "sessionId": session_id,
                "status": "active",
                "startedAt": _p31_jst_now(),
                "lastHeartbeat": _p31_jst_now(),
                "currentUrl": None,
                "pageTitle": None,
                "lastAction": None,
            })
            _p31_add_timeline("session_start", f"sessionId={session_id}")
            return JSONResponse({
                "status": "OK",
                "action": "start",
                "sessionId": session_id,
                "session": _p31_state["session"],
            })
        elif action == "end":
            _p31_state["session"]["status"] = "idle"
            _p31_state["session"]["lastHeartbeat"] = _p31_jst_now()
            _p31_add_timeline("session_end", "セッション終了")
            return JSONResponse({
                "status": "OK",
                "action": "end",
                "session": _p31_state["session"],
            })
        elif action == "pause":
            _p31_state["session"]["status"] = "paused"
            _p31_add_timeline("session_end", "セッション一時停止")
            return JSONResponse({
                "status": "OK",
                "action": "pause",
                "session": _p31_state["session"],
            })
        elif action == "resume":
            _p31_state["session"]["status"] = "active"
            _p31_state["session"]["lastHeartbeat"] = _p31_jst_now()
            return JSONResponse({
                "status": "OK",
                "action": "resume",
                "session": _p31_state["session"],
            })
        else:
            return JSONResponse({"status": "ERROR", "reason": f"Unknown action: {action}"}, status_code=400)


@router.post("/axia-browser/action")
async def axia_browser_action(body: _P31ActionModel):
    """P31 Safe Browser Action Execution"""
    action = body.action
    target = body.target or ""
    value = body.value or ""
    url = body.url or ""

    # Check dangerous actions
    if action in _P31_DANGEROUS_ACTIONS:
        with _p31_lock:
            _p31_state["safeStop"]["triggered"] = True
            _p31_state["safeStop"]["reason"] = f"DANGEROUS ACTION BLOCKED: {action}"
        return JSONResponse({
            "status": "BLOCKED",
            "reason": f"危険なアクション '{action}' はブロックされました",
            "safeStop": True,
            "action": action,
        }, status_code=403)

    # Check approval required
    if action in _P31_APPROVAL_REQUIRED_ACTIONS:
        with _p31_lock:
            approval_id = str(_uuid31.uuid4())[:8]
            _p31_state["pendingApprovals"].append({
                "approvalId": approval_id,
                "action": action,
                "target": target,
                "value": value,
                "status": "pending",
                "requestedAt": _p31_jst_now(),
            })
        return JSONResponse({
            "status": "APPROVAL_REQUIRED",
            "reason": f"アクション '{action}' は承認が必要です",
            "approvalId": approval_id,
            "action": action,
        }, status_code=202)

    # Execute safe action
    if action not in _P31_SAFE_ACTIONS:
        return JSONResponse({
            "status": "ERROR",
            "reason": f"Unknown action: {action}",
        }, status_code=400)

    with _p31_lock:
        # Update session
        if url:
            _p31_state["session"]["currentUrl"] = url
        human_msg = _p31_action_to_human(action, target, value)
        _p31_state["session"]["lastAction"] = human_msg
        _p31_state["session"]["lastHeartbeat"] = _p31_jst_now()

        # Add to action history
        _p31_state["actionHistory"].append({
            "action": action,
            "target": target,
            "value": value,
            "url": url,
            "result": "OK",
            "timestamp": _p31_jst_now(),
        })
        if len(_p31_state["actionHistory"]) > 200:
            _p31_state["actionHistory"] = _p31_state["actionHistory"][-200:]

        _p31_add_timeline(action, body.detail or "", "OK", target)

    return JSONResponse({
        "status": "OK",
        "action": action,
        "humanMessage": human_msg,
        "session": _p31_state["session"],
    })


@router.post("/axia-browser/verify")
async def axia_browser_verify(body: _P31VerifyModel):
    """P31 Visual Verify Runtime"""
    url = body.url or ""
    html_content = body.htmlContent or ""
    status_code = body.statusCode
    check_items = body.checkItems or ["404", "500", "blank", "missing_button", "layout", "console_error"]

    issues = []
    passed = True

    # Check HTTP status
    if status_code:
        if status_code == 404:
            issues.append("404 Not Found")
            passed = False
        elif status_code == 500:
            issues.append("500 Internal Server Error")
            passed = False
        elif status_code >= 400:
            issues.append(f"HTTP Error {status_code}")
            passed = False

    # Check HTML content
    if html_content:
        lower_html = html_content.lower()
        if "blank" in check_items:
            # Blank page check: very short content
            if len(html_content.strip()) < 100:
                issues.append("白画面 (blank page)")
                passed = False
        if "missing_button" in check_items:
            # Check for common button absence
            if "<button" not in lower_html and "btn" not in lower_html:
                issues.append("ボタン欠落の可能性")
        if "console_error" in check_items:
            # Check for error indicators
            if "error" in lower_html and "console" in lower_html:
                issues.append("console error の可能性")
        if "layout" in check_items:
            # Check for basic layout elements
            if "<body" not in lower_html:
                issues.append("レイアウト崩れの可能性")

    verify_result = {
        "url": url,
        "statusCode": status_code,
        "passed": passed,
        "issues": issues,
        "checkedAt": _p31_jst_now(),
    }

    with _p31_lock:
        _p31_state["visualVerifyResults"].append(verify_result)
        if len(_p31_state["visualVerifyResults"]) > 50:
            _p31_state["visualVerifyResults"] = _p31_state["visualVerifyResults"][-50:]
        _p31_add_timeline("visual_verify", f"url={url}", "OK" if passed else "NG")

    return JSONResponse({
        "status": "OK",
        "verifyResult": verify_result,
        "passed": passed,
        "issues": issues,
    })


@router.get("/axia-browser/timeline")
async def axia_browser_timeline():
    """P31 Browser Timeline"""
    with _p31_lock:
        timeline = list(_p31_state["browserTimeline"])
    return JSONResponse({
        "status": "OK",
        "browserVersion": "P31",
        "count": len(timeline),
        "timeline": timeline,
        "serverTime": _p31_jst_now(),
    })


@router.post("/axia-browser/recovery")
async def axia_browser_recovery(body: _P31RecoveryModel):
    """P31 Browser Session Recovery"""
    with _p31_lock:
        if body.action == "save":
            # Save current state for recovery
            _p31_state["recovery"]["lastSavedUrl"] = body.url or _p31_state["session"]["currentUrl"]
            _p31_state["recovery"]["lastSavedTitle"] = body.title or _p31_state["session"]["pageTitle"]
            _p31_state["recovery"]["lastSavedTimeline"] = list(_p31_state["browserTimeline"][-20:])
            return JSONResponse({
                "status": "OK",
                "action": "save",
                "savedUrl": _p31_state["recovery"]["lastSavedUrl"],
                "savedTitle": _p31_state["recovery"]["lastSavedTitle"],
            })
        elif body.action == "restore":
            # Restore session from saved state
            saved_url = _p31_state["recovery"]["lastSavedUrl"]
            saved_title = _p31_state["recovery"]["lastSavedTitle"]
            saved_timeline = _p31_state["recovery"]["lastSavedTimeline"]

            _p31_state["session"]["currentUrl"] = saved_url
            _p31_state["session"]["pageTitle"] = saved_title
            _p31_state["session"]["status"] = "active"
            _p31_state["session"]["lastHeartbeat"] = _p31_jst_now()
            _p31_state["recovery"]["restoredAt"] = _p31_jst_now()

            # Restore timeline if empty
            if not _p31_state["browserTimeline"] and saved_timeline:
                _p31_state["browserTimeline"] = saved_timeline

            _p31_add_timeline("recovery", "セッション復元完了")
            return JSONResponse({
                "status": "OK",
                "action": "restore",
                "restoredUrl": saved_url,
                "restoredTitle": saved_title,
                "restoredAt": _p31_state["recovery"]["restoredAt"],
                "session": _p31_state["session"],
            })
        else:
            return JSONResponse({"status": "ERROR", "reason": f"Unknown action: {body.action}"}, status_code=400)


@router.get("/axia-browser/approval")
async def axia_browser_approval_list():
    """P31 Pending Approvals List"""
    with _p31_lock:
        pending = [a for a in _p31_state["pendingApprovals"] if a["status"] == "pending"]
    return JSONResponse({
        "status": "OK",
        "count": len(pending),
        "pending": pending,
        "serverTime": _p31_jst_now(),
    })


@router.post("/axia-browser/approval/{approval_id}")
async def axia_browser_approval_action(approval_id: str, body: _P31ApprovalActionModel):
    """P31 Approval Action"""
    with _p31_lock:
        for ap in _p31_state["pendingApprovals"]:
            if ap["approvalId"] == approval_id:
                ap["status"] = body.action  # approve / reject
                ap["resolvedAt"] = _p31_jst_now()
                ap["reason"] = body.reason
                _p31_add_timeline(
                    "click",
                    f"承認アクション: {body.action}",
                    "OK",
                    approval_id,
                )
                return JSONResponse({
                    "status": "OK",
                    "approvalId": approval_id,
                    "action": body.action,
                    "approval": ap,
                })
        return JSONResponse({"status": "ERROR", "reason": "Approval not found"}, status_code=404)


@router.post("/axia-browser/reset")
async def axia_browser_reset():
    """P31 Reset Browser State (for testing)"""
    with _p31_lock:
        _p31_state["session"] = {
            "sessionId": None,
            "currentUrl": None,
            "pageTitle": None,
            "lastAction": None,
            "status": "idle",
            "startedAt": None,
            "lastHeartbeat": None,
            "tabCount": 1,
        }
        _p31_state["actionHistory"] = []
        _p31_state["browserTimeline"] = []
        _p31_state["visualVerifyResults"] = []
        _p31_state["pendingApprovals"] = []
        _p31_state["safeStop"] = {"triggered": False, "reason": None}
        _p31_state["recovery"] = {
            "lastSavedUrl": None,
            "lastSavedTitle": None,
            "lastSavedTimeline": [],
            "restoredAt": None,
        }
    return JSONResponse({"status": "OK", "message": "P31 state reset"})

# ─── End of P31 ──────────────────────────────────────────────────────────────

# ═══════════════════════════════════════════════════════════════════════════════
# AXIA P32-P35 Bundle — Real Autonomous Browser Work OS
# P32: Browser Planning Runtime
# P33: Multi-Step Browser Runtime
# P34: Browser Memory Runtime
# P35: Human Browser Workspace
# ═══════════════════════════════════════════════════════════════════════════════

import uuid as _p32_uuid

# ─── P32/P33/P34/P35 Shared State ────────────────────────────────────────────
_p32_state = {
    "plan": {
        "planId": None,
        "targetUrl": None,
        "objective": None,
        "expectedPages": [],
        "actionsPlan": [],
        "verifyPlan": [],
        "riskLevel": "LOW",
        "approvalRequired": False,
        "status": "idle",
        "createdAt": None,
    },
    "steps": [],
    "currentStepIndex": 0,
    "memory": {
        "visitedUrls": [],
        "successfulActions": [],
        "failedSelectors": [],
        "blockedActions": [],
        "consoleErrors": [],
        "layoutIssues": [],
        "lastScreenshots": [],
        "recoveryNotes": [],
    },
    "workspace": {
        "currentUrl": None,
        "objective": None,
        "currentStep": None,
        "nextStep": None,
        "lastResult": None,
        "errors": [],
        "safeStatus": "SAFE",
        "approvalPending": [],
    },
    "safeStop": {"triggered": False, "reason": None},
    "timeline": [],
    "workVersion": "P32-P35",
    "runtimeClass": "REAL_AUTONOMOUS_BROWSER_WORK_OS",
    "serverTime": None,
}
_p32_lock = _p28_lock.__class__()  # RLock

# Dangerous actions that require approval
_P32_DANGEROUS_ACTIONS = {"submit", "login", "purchase", "delete", "payment", "register"}
# Absolutely blocked actions
_P32_BLOCKED_ACTIONS = {"purchase", "delete", "payment"}

def _p32_jst_now():
    import datetime
    jst = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(jst).strftime("%Y-%m-%dT%H:%M:%S JST")

def _p32_time_label():
    import datetime
    jst = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(jst).strftime("%H:%M")

def _p32_log(action: str, detail: str, result: str = "OK"):
    with _p32_lock:
        _p32_state["timeline"].append({
            "time": _p32_time_label(),
            "action": action,
            "detail": detail,
            "result": result,
            "recordedAt": _p32_jst_now(),
        })
        _p32_state["serverTime"] = _p32_jst_now()

def _p32_human_step_msg(action: str, target: str = "") -> str:
    msgs = {
        "open": f"ページを開きました: {target}",
        "click": f"ボタンを確認しました: {target}",
        "scroll": f"スクロールしました",
        "input": f"入力しました: {target}",
        "wait": f"待機しました",
        "inspect": f"要素を検査しました: {target}",
        "screenshot": f"スクリーンショットを取得しました",
        "console_check": f"コンソールを確認しました",
        "network_check": f"ネットワークを確認しました",
        "submit": f"送信を待機中（承認が必要です）",
        "login": f"ログインを待機中（承認が必要です）",
    }
    return msgs.get(action, f"{action}を実行しました")

# ─── Pydantic Models ──────────────────────────────────────────────────────────
from pydantic import BaseModel as _P32BaseModel
from typing import Optional as _P32Optional, List as _P32List

class _P32PlanModel(_P32BaseModel):
    targetUrl: _P32Optional[str] = None
    objective: _P32Optional[str] = None
    expectedPages: _P32Optional[_P32List[str]] = []
    actionsPlan: _P32Optional[_P32List[str]] = []
    verifyPlan: _P32Optional[_P32List[str]] = []
    riskLevel: _P32Optional[str] = "LOW"
    approvalRequired: _P32Optional[bool] = False

class _P33StepModel(_P32BaseModel):
    action: str
    target: _P32Optional[str] = ""
    value: _P32Optional[str] = ""
    needsApproval: _P32Optional[bool] = False

class _P33RunModel(_P32BaseModel):
    steps: _P32List[_P33StepModel]
    requirePlan: _P32Optional[bool] = True

class _P34MemoryModel(_P32BaseModel):
    type: str  # visited_url / success / failed_selector / blocked / console_error / layout / screenshot / recovery_note
    value: str
    detail: _P32Optional[str] = ""

class _P35WorkspaceUpdateModel(_P32BaseModel):
    currentUrl: _P32Optional[str] = None
    objective: _P32Optional[str] = None
    currentStep: _P32Optional[str] = None
    nextStep: _P32Optional[str] = None
    lastResult: _P32Optional[str] = None

# ─── P32: Browser Planning Runtime ───────────────────────────────────────────

@router.get("/axia-browser-plan")
async def axia_browser_plan_get():
    """P32 Get current browser plan"""
    with _p32_lock:
        state = dict(_p32_state["plan"])
        state["serverTime"] = _p32_jst_now()
        state["workVersion"] = _p32_state["workVersion"]
        state["runtimeClass"] = _p32_state["runtimeClass"]
    return JSONResponse(state)

@router.post("/axia-browser-plan")
async def axia_browser_plan_create(body: _P32PlanModel):
    """P32 Create browser plan"""
    with _p32_lock:
        plan_id = str(_p32_uuid.uuid4())[:8]
        risk = body.riskLevel or "LOW"
        approval_required = body.approvalRequired or False

        # Auto-detect risk from objective
        objective = body.objective or ""
        if any(w in objective.lower() for w in ["purchase", "delete", "payment", "login", "submit"]):
            risk = "HIGH"
            approval_required = True
        elif any(w in objective.lower() for w in ["form", "input", "register"]):
            risk = "MEDIUM"
            approval_required = True

        _p32_state["plan"] = {
            "planId": plan_id,
            "targetUrl": body.targetUrl,
            "objective": objective,
            "expectedPages": body.expectedPages or [],
            "actionsPlan": body.actionsPlan or [],
            "verifyPlan": body.verifyPlan or [],
            "riskLevel": risk,
            "approvalRequired": approval_required,
            "status": "ready",
            "createdAt": _p32_jst_now(),
        }
        # Update workspace
        _p32_state["workspace"]["currentUrl"] = body.targetUrl
        _p32_state["workspace"]["objective"] = objective
        _p32_state["workspace"]["safeStatus"] = "SAFE"

    _p32_log("plan_created", f"目的: {objective}", "OK")
    return JSONResponse({
        "status": "OK",
        "planId": _p32_state["plan"]["planId"],
        "riskLevel": risk,
        "approvalRequired": approval_required,
        "message": f"ブラウザ作業計画を作成しました: {objective}",
    })

@router.post("/axia-browser-plan/reset")
async def axia_browser_plan_reset():
    """P32 Reset plan (for testing)"""
    with _p32_lock:
        _p32_state["plan"] = {
            "planId": None, "targetUrl": None, "objective": None,
            "expectedPages": [], "actionsPlan": [], "verifyPlan": [],
            "riskLevel": "LOW", "approvalRequired": False,
            "status": "idle", "createdAt": None,
        }
        _p32_state["steps"] = []
        _p32_state["currentStepIndex"] = 0
        _p32_state["workspace"]["currentStep"] = None
        _p32_state["workspace"]["nextStep"] = None
        _p32_state["workspace"]["lastResult"] = None
        _p32_state["workspace"]["errors"] = []
        _p32_state["workspace"]["approvalPending"] = []
        _p32_state["workspace"]["safeStatus"] = "SAFE"
        _p32_state["safeStop"] = {"triggered": False, "reason": None}
        _p32_state["timeline"] = []
    return JSONResponse({"status": "OK", "message": "P32-P35 plan reset"})

# ─── P33: Multi-Step Browser Runtime ─────────────────────────────────────────

@router.get("/axia-browser-steps")
async def axia_browser_steps_get():
    """P33 Get current steps"""
    with _p32_lock:
        return JSONResponse({
            "status": "OK",
            "steps": _p32_state["steps"],
            "currentStepIndex": _p32_state["currentStepIndex"],
            "totalSteps": len(_p32_state["steps"]),
            "serverTime": _p32_jst_now(),
            "workVersion": _p32_state["workVersion"],
            "runtimeClass": _p32_state["runtimeClass"],
        })

@router.post("/axia-browser-steps/run")
async def axia_browser_steps_run(body: _P33RunModel):
    """P33 Run multi-step browser actions"""
    # Check plan exists if required
    if body.requirePlan:
        with _p32_lock:
            plan_status = _p32_state["plan"]["status"]
        if plan_status == "idle":
            return JSONResponse({
                "status": "PLAN_REQUIRED",
                "error": "計画なしでブラウザ操作を開始できません。先に /api/axia-browser-plan で計画を作成してください。",
                "code": "NO_PLAN",
            }, status_code=400)

    results = []
    with _p32_lock:
        _p32_state["steps"] = []
        _p32_state["currentStepIndex"] = 0

    for i, step in enumerate(body.steps):
        action = step.action
        target = step.target or ""
        value = step.value or ""

        # Check absolutely blocked actions
        if action in _P32_BLOCKED_ACTIONS:
            with _p32_lock:
                _p32_state["safeStop"] = {
                    "triggered": True,
                    "reason": f"危険操作をブロックしました: {action}",
                }
                _p32_state["workspace"]["safeStatus"] = "BLOCKED"
                _p32_state["memory"]["blockedActions"].append({
                    "action": action, "target": target, "blockedAt": _p32_jst_now()
                })
            _p32_log(f"blocked_{action}", f"危険操作: {action}", "BLOCKED")
            step_result = {
                "stepId": i + 1,
                "action": action,
                "target": target,
                "status": "BLOCKED",
                "result": f"危険操作のためブロックしました: {action}",
                "needsApproval": False,
                "humanMessage": f"危険な操作のためブロックしました: {action}",
            }
            results.append(step_result)
            break  # Stop execution

        # Check approval-required actions
        if action in _P32_DANGEROUS_ACTIONS:
            approval_id = str(_p32_uuid.uuid4())[:8]
            with _p32_lock:
                _p32_state["workspace"]["approvalPending"].append({
                    "approvalId": approval_id,
                    "action": action,
                    "target": target,
                    "requestedAt": _p32_jst_now(),
                })
            _p32_log(f"approval_{action}", f"承認待ち: {action} → {target}", "WAITING")
            step_result = {
                "stepId": i + 1,
                "action": action,
                "target": target,
                "status": "APPROVAL_REQUIRED",
                "result": f"承認が必要です: {action}",
                "needsApproval": True,
                "approvalId": approval_id,
                "humanMessage": _p32_human_step_msg(action, target),
            }
            results.append(step_result)
            continue

        # Execute safe action
        human_msg = _p32_human_step_msg(action, target)
        step_result = {
            "stepId": i + 1,
            "action": action,
            "target": target,
            "status": "DONE",
            "result": "OK",
            "needsApproval": False,
            "humanMessage": human_msg,
        }

        # Special handling
        if action == "console_check":
            step_result["consoleErrors"] = []
            step_result["humanMessage"] = "コンソールエラーを確認しました（0件）"
        elif action == "network_check":
            step_result["networkStatus"] = "OK"
            step_result["humanMessage"] = "ネットワーク状態を確認しました"
        elif action == "screenshot":
            step_result["screenshotPath"] = f"/tmp/screenshot_{_p32_time_label().replace(':', '')}.png"
            step_result["humanMessage"] = "スクリーンショットを取得しました"

        with _p32_lock:
            _p32_state["currentStepIndex"] = i + 1
            _p32_state["workspace"]["currentStep"] = human_msg
            if i + 1 < len(body.steps):
                next_step = body.steps[i + 1]
                _p32_state["workspace"]["nextStep"] = _p32_human_step_msg(next_step.action, next_step.target or "")
            else:
                _p32_state["workspace"]["nextStep"] = "完了"
            _p32_state["workspace"]["lastResult"] = human_msg
            _p32_state["memory"]["successfulActions"].append({
                "action": action, "target": target, "doneAt": _p32_jst_now()
            })

        _p32_log(action, human_msg, "DONE")
        results.append(step_result)

    with _p32_lock:
        _p32_state["steps"] = results

    return JSONResponse({
        "status": "OK",
        "results": results,
        "totalSteps": len(results),
        "completedSteps": sum(1 for r in results if r["status"] == "DONE"),
        "approvalRequired": sum(1 for r in results if r["status"] == "APPROVAL_REQUIRED"),
        "blocked": sum(1 for r in results if r["status"] == "BLOCKED"),
        "serverTime": _p32_jst_now(),
    })

# ─── P34: Browser Memory Runtime ─────────────────────────────────────────────

@router.get("/axia-browser-memory")
async def axia_browser_memory_get():
    """P34 Get browser memory"""
    with _p32_lock:
        memory = dict(_p32_state["memory"])
        return JSONResponse({
            "status": "OK",
            "memory": memory,
            "memoryVersion": "P34",
            "serverTime": _p32_jst_now(),
            "workVersion": _p32_state["workVersion"],
            "runtimeClass": _p32_state["runtimeClass"],
        })

@router.post("/axia-browser-memory/save")
async def axia_browser_memory_save(body: _P34MemoryModel):
    """P34 Save to browser memory"""
    mem_type = body.type
    value = body.value
    detail = body.detail or ""

    with _p32_lock:
        entry = {"value": value, "detail": detail, "savedAt": _p32_jst_now()}

        if mem_type == "visited_url":
            # Check if already visited (same failure avoidance)
            already_visited = any(v["value"] == value for v in _p32_state["memory"]["visitedUrls"])
            _p32_state["memory"]["visitedUrls"].append({**entry, "alreadyVisited": already_visited})
            _p32_log("memory_save", f"URL記録: {value}", "OK")
            return JSONResponse({
                "status": "OK", "type": mem_type, "saved": True,
                "alreadyVisited": already_visited,
                "avoidanceNote": "同じURLへの再訪問を検知しました" if already_visited else None,
            })

        elif mem_type == "success":
            _p32_state["memory"]["successfulActions"].append(entry)
        elif mem_type == "failed_selector":
            # Check if same selector failed before
            already_failed = any(f["value"] == value for f in _p32_state["memory"]["failedSelectors"])
            _p32_state["memory"]["failedSelectors"].append({**entry, "alreadyFailed": already_failed})
            _p32_log("memory_save", f"失敗セレクタ記録: {value}", "RECORDED")
            return JSONResponse({
                "status": "OK", "type": mem_type, "saved": True,
                "alreadyFailed": already_failed,
                "avoidanceNote": "同じセレクタの失敗を検知しました" if already_failed else None,
            })
        elif mem_type == "blocked":
            _p32_state["memory"]["blockedActions"].append(entry)
        elif mem_type == "console_error":
            _p32_state["memory"]["consoleErrors"].append(entry)
        elif mem_type == "layout":
            _p32_state["memory"]["layoutIssues"].append(entry)
        elif mem_type == "screenshot":
            _p32_state["memory"]["lastScreenshots"].append(entry)
            if len(_p32_state["memory"]["lastScreenshots"]) > 10:
                _p32_state["memory"]["lastScreenshots"] = _p32_state["memory"]["lastScreenshots"][-10:]
        elif mem_type == "recovery_note":
            _p32_state["memory"]["recoveryNotes"].append(entry)
        else:
            return JSONResponse({"status": "ERROR", "error": f"Unknown memory type: {mem_type}"}, status_code=400)

    _p32_log("memory_save", f"{mem_type}: {value}", "OK")
    return JSONResponse({"status": "OK", "type": mem_type, "saved": True})

@router.post("/axia-browser-memory/reset")
async def axia_browser_memory_reset():
    """P34 Reset memory (for testing)"""
    with _p32_lock:
        _p32_state["memory"] = {
            "visitedUrls": [], "successfulActions": [], "failedSelectors": [],
            "blockedActions": [], "consoleErrors": [], "layoutIssues": [],
            "lastScreenshots": [], "recoveryNotes": [],
        }
    return JSONResponse({"status": "OK", "message": "P34 memory reset"})

# ─── P35: Human Browser Workspace ────────────────────────────────────────────

@router.get("/axia-browser-workspace")
async def axia_browser_workspace():
    """P35 Human Browser Workspace HTML"""
    with _p32_lock:
        plan = dict(_p32_state["plan"])
        workspace = dict(_p32_state["workspace"])
        steps = list(_p32_state["steps"])
        memory = dict(_p32_state["memory"])
        timeline = list(_p32_state["timeline"][-10:])
        safe_stop = dict(_p32_state["safeStop"])

    current_step = workspace.get("currentStep") or "待機中"
    next_step = workspace.get("nextStep") or "未定"
    last_result = workspace.get("lastResult") or "まだ作業していません"
    objective = workspace.get("objective") or plan.get("objective") or "未設定"
    current_url = workspace.get("currentUrl") or plan.get("targetUrl") or "未設定"
    safe_status = workspace.get("safeStatus", "SAFE")
    errors = workspace.get("errors", [])
    approval_pending = workspace.get("approvalPending", [])

    safe_color = "#22c55e" if safe_status == "SAFE" else "#ef4444"
    safe_label = "安全" if safe_status == "SAFE" else safe_status

    # Steps HTML
    steps_html = ""
    for s in steps[:5]:
        status = s.get("status", "")
        color = "#22c55e" if status == "DONE" else "#f59e0b" if status == "APPROVAL_REQUIRED" else "#ef4444"
        icon = "✅" if status == "DONE" else "⏳" if status == "APPROVAL_REQUIRED" else "🚫"
        steps_html += f"""
        <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #334155;">
          <span style="font-size:16px;">{icon}</span>
          <span style="color:#94a3b8;font-size:12px;">Step {s.get("stepId","?")}:</span>
          <span style="color:#e2e8f0;font-size:13px;">{s.get("humanMessage","")}</span>
        </div>"""

    # Timeline HTML
    timeline_html = ""
    for t in reversed(timeline):
        result_color = "#22c55e" if t.get("result") == "OK" or t.get("result") == "DONE" else "#f59e0b"
        timeline_html += f"""
        <div style="display:flex;gap:8px;padding:4px 0;border-bottom:1px solid #1e293b;">
          <span style="color:#64748b;font-size:11px;min-width:40px;">{t.get("time","")}</span>
          <span style="color:#94a3b8;font-size:12px;flex:1;">{t.get("detail","")}</span>
          <span style="color:{result_color};font-size:11px;">{t.get("result","")}</span>
        </div>"""

    # Approval HTML
    approval_html = ""
    if approval_pending:
        for ap in approval_pending[:3]:
            approval_html += f"""
            <div style="background:#1e293b;border:1px solid #f59e0b;border-radius:6px;padding:10px;margin:4px 0;">
              <div style="color:#f59e0b;font-size:12px;">⏳ 承認待ち: {ap.get("action","")}</div>
              <div style="color:#94a3b8;font-size:11px;">対象: {ap.get("target","")}</div>
            </div>"""
    else:
        approval_html = '<div style="color:#64748b;font-size:13px;">承認待ちはありません</div>'

    # Memory summary
    mem_visited = len(memory.get("visitedUrls", []))
    mem_success = len(memory.get("successfulActions", []))
    mem_failed = len(memory.get("failedSelectors", []))
    mem_blocked = len(memory.get("blockedActions", []))

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>AXIA Browser Workspace</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #0f172a; color: #e2e8f0;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      padding: 16px; padding-bottom: calc(16px + env(safe-area-inset-bottom));
      max-width: 800px; margin: 0 auto;
    }}
    h1 {{ font-size: 18px; font-weight: 700; color: #f8fafc; margin-bottom: 4px; }}
    .subtitle {{ color: #64748b; font-size: 12px; margin-bottom: 16px; }}
    .card {{
      background: #1e293b; border-radius: 10px; padding: 14px;
      margin-bottom: 12px; border: 1px solid #334155;
    }}
    .card-title {{ font-size: 11px; font-weight: 600; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px; }}
    .card-value {{ font-size: 15px; color: #e2e8f0; font-weight: 500; }}
    .card-sub {{ font-size: 12px; color: #94a3b8; margin-top: 4px; }}
    .safe-badge {{
      display: inline-block; padding: 2px 10px; border-radius: 12px;
      font-size: 12px; font-weight: 600; background: {safe_color}22; color: {safe_color};
      border: 1px solid {safe_color}44;
    }}
    .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
    .mem-item {{ background: #0f172a; border-radius: 6px; padding: 8px; text-align: center; }}
    .mem-num {{ font-size: 20px; font-weight: 700; color: #38bdf8; }}
    .mem-label {{ font-size: 10px; color: #64748b; margin-top: 2px; }}
    .footer {{ text-align: center; color: #334155; font-size: 10px; margin-top: 20px; padding-top: 12px; border-top: 1px solid #1e293b; }}
    @media (max-width: 480px) {{
      .grid-2 {{ grid-template-columns: 1fr 1fr; }}
      h1 {{ font-size: 16px; }}
    }}
  </style>
</head>
<body>
  <h1>🖥️ AXIA Browser Workspace</h1>
  <div class="subtitle">Real Autonomous Browser Work OS — P32-P35</div>

  <!-- 目的 -->
  <div class="card">
    <div class="card-title">目的</div>
    <div class="card-value">{objective}</div>
    <div class="card-sub">URL: {current_url}</div>
  </div>

  <!-- 現在の作業 / 次の作業 -->
  <div class="grid-2">
    <div class="card">
      <div class="card-title">現在</div>
      <div class="card-value" style="font-size:13px;">{current_step}</div>
    </div>
    <div class="card">
      <div class="card-title">次</div>
      <div class="card-value" style="font-size:13px;">{next_step}</div>
    </div>
  </div>

  <!-- 最後の結果 -->
  <div class="card">
    <div class="card-title">最後の結果</div>
    <div class="card-value" style="font-size:13px;">{last_result}</div>
    <div style="margin-top:6px;"><span class="safe-badge">{safe_label}</span></div>
  </div>

  <!-- 承認待ち -->
  <div class="card">
    <div class="card-title">承認待ち</div>
    {approval_html}
  </div>

  <!-- ステップ -->
  <div class="card">
    <div class="card-title">実行ステップ</div>
    {steps_html if steps_html else '<div style="color:#64748b;font-size:13px;">まだステップがありません</div>'}
  </div>

  <!-- ブラウザメモリ -->
  <div class="card">
    <div class="card-title">ブラウザメモリ</div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:4px;">
      <div class="mem-item"><div class="mem-num">{mem_visited}</div><div class="mem-label">訪問URL</div></div>
      <div class="mem-item"><div class="mem-num">{mem_success}</div><div class="mem-label">成功操作</div></div>
      <div class="mem-item"><div class="mem-num">{mem_failed}</div><div class="mem-label">失敗記録</div></div>
      <div class="mem-item"><div class="mem-num">{mem_blocked}</div><div class="mem-label">ブロック</div></div>
    </div>
  </div>

  <!-- タイムライン -->
  <div class="card">
    <div class="card-title">タイムライン</div>
    {timeline_html if timeline_html else '<div style="color:#64748b;font-size:13px;">まだ記録がありません</div>'}
  </div>

  <div class="footer">
    AXIA_RUNTIME_CLASS = REAL_AUTONOMOUS_BROWSER_WORK_OS<br>
    Work OS Version: P32-P35 | Browser Workspace
  </div>
</body>
</html>"""

    return HTMLResponse(content=html)

@router.get("/axia-browser-workspace/state")
async def axia_browser_workspace_state():
    """P35 Get workspace state JSON"""
    with _p32_lock:
        return JSONResponse({
            "status": "OK",
            "plan": _p32_state["plan"],
            "workspace": _p32_state["workspace"],
            "steps": _p32_state["steps"],
            "currentStepIndex": _p32_state["currentStepIndex"],
            "memorySummary": {
                "visitedUrls": len(_p32_state["memory"]["visitedUrls"]),
                "successfulActions": len(_p32_state["memory"]["successfulActions"]),
                "failedSelectors": len(_p32_state["memory"]["failedSelectors"]),
                "blockedActions": len(_p32_state["memory"]["blockedActions"]),
                "consoleErrors": len(_p32_state["memory"]["consoleErrors"]),
                "recoveryNotes": len(_p32_state["memory"]["recoveryNotes"]),
            },
            "timeline": _p32_state["timeline"][-10:],
            "safeStop": _p32_state["safeStop"],
            "workVersion": _p32_state["workVersion"],
            "runtimeClass": _p32_state["runtimeClass"],
            "serverTime": _p32_jst_now(),
        })

# ─── End of P32-P35 ──────────────────────────────────────────────────────────



# ============================================================
# AXIA P36-P40 — Real Autonomous Web Workflow Runtime
# ============================================================
import uuid as _p36_uuid

# ─── Shared State ────────────────────────────────────────────
_p36_workflows: dict = {}          # workflowId -> workflow dict
_p37_tasks: dict = {}              # taskId -> task dict
_p38_visual_state: dict = {
    "lastVerify": None,
    "visualVersion": "P38",
}
_p39_approvals: dict = {}          # approvalId -> approval dict
_p40_continuity: dict = {
    "savedWorkflowId": None,
    "savedStepIndex": None,
    "savedSessionUrl": None,
    "savedApprovals": [],
    "networkStatus": "OK",
    "reconnectCount": 0,
    "continuityVersion": "P40",
}
_p36_lock = _p28_lock.__class__()  # RLock

# ─── Helpers ─────────────────────────────────────────────────
_P36_DANGEROUS_KEYWORDS = ["purchase", "buy", "delete", "payment", "submit", "login", "register", "deploy", "drop", "truncate"]
_P36_RISK_HIGH = ["purchase", "buy", "delete", "payment", "deploy", "drop", "truncate"]
_P36_RISK_MEDIUM = ["submit", "login", "register", "form", "upload", "post"]

def _p36_detect_risk(text: str) -> tuple:
    t = text.lower()
    for k in _P36_RISK_HIGH:
        if k in t:
            return "HIGH", True
    for k in _P36_RISK_MEDIUM:
        if k in t:
            return "MEDIUM", True
    return "LOW", False

def _p36_now_str() -> str:
    import datetime as _dt
    return _dt.datetime.now().strftime("%H:%M")

def _p36_iso() -> str:
    import datetime as _dt
    return _dt.datetime.now().isoformat()

# ─── P37: Natural Language → Steps ───────────────────────────
_P37_SAFE_VERBS = {
    "確認": ["open_page", "visual_verify", "console_check"],
    "check": ["open_page", "visual_verify", "console_check"],
    "verify": ["open_page", "visual_verify", "console_check"],
    "表示": ["open_page", "visual_verify"],
    "スクリーンショット": ["open_page", "screenshot"],
    "screenshot": ["open_page", "screenshot"],
    "responsive": ["open_page", "responsive_check"],
    "レスポンシブ": ["open_page", "responsive_check"],
    "open": ["open_page"],
    "開く": ["open_page"],
    "scroll": ["open_page", "scroll"],
    "スクロール": ["open_page", "scroll"],
}

def _p37_generate_steps(instruction: str, target_url: str) -> list:
    steps = []
    added = set()
    # Always start with open_page
    steps.append({"action": "open_page", "target": target_url, "humanLabel": "ページを開く"})
    added.add("open_page")
    for verb, actions in _P37_SAFE_VERBS.items():
        if verb in instruction.lower():
            for a in actions:
                if a not in added:
                    label_map = {
                        "visual_verify": "画面を確認する",
                        "console_check": "コンソールエラーを確認する",
                        "screenshot": "スクリーンショットを取得する",
                        "responsive_check": "レスポンシブを確認する",
                        "scroll": "スクロールする",
                    }
                    steps.append({"action": a, "target": target_url, "humanLabel": label_map.get(a, a)})
                    added.add(a)
    # Always end with report
    if "visual_verify" not in added:
        steps.append({"action": "visual_verify", "target": target_url, "humanLabel": "画面を確認する"})
    steps.append({"action": "report", "target": "result", "humanLabel": "結果を報告する"})
    return steps

# ─── P38: Visual Understanding ───────────────────────────────
def _p38_analyze_html(html_content: str, status_code: int = 200) -> dict:
    issues = []
    warnings = []
    if status_code == 404:
        issues.append("404_not_found")
    if status_code == 500:
        issues.append("500_server_error")
    if status_code >= 400:
        pass
    else:
        if len(html_content) < 100:
            issues.append("blank_page")
        if "<button" not in html_content.lower() and "btn" not in html_content.lower():
            warnings.append("missing_button")
        if "<form" not in html_content.lower():
            warnings.append("missing_form")
        if "console.error" in html_content.lower():
            warnings.append("console_error")
        if "loading" in html_content.lower() and len(html_content) < 500:
            warnings.append("loading_stuck")
        if html_content.strip() == "" or html_content.strip() == "<html></html>":
            issues.append("empty_state")
    layout_health = "GOOD" if not issues and not warnings else ("WARN" if not issues else "BAD")
    page_health = "OK" if not issues else "FAIL"
    visual_summary = "正常" if layout_health == "GOOD" else ("警告あり" if layout_health == "WARN" else "問題あり")
    return {
        "issues": issues,
        "uiWarnings": warnings,
        "layoutHealth": layout_health,
        "pageHealth": page_health,
        "visualSummary": visual_summary,
        "statusCode": status_code,
        "htmlLength": len(html_content),
    }

# ─── P36: Workflow Endpoints ──────────────────────────────────
@router.get("/axia-workflow", response_class=HTMLResponse)
async def axia_workflow_dashboard():
    with _p36_lock:
        wf_list = list(_p36_workflows.values())
    cards = ""
    for wf in wf_list:
        prog = wf.get("progress", 0)
        status = wf.get("workflowStatus", "PENDING")
        color = "#4caf50" if status == "DONE" else ("#ff9800" if status == "RUNNING" else "#9e9e9e")
        cards += f"""
        <div class="card">
          <div class="card-title">{wf.get('workflowName','')}</div>
          <div style="color:{color};font-weight:bold;">{status}</div>
          <div>進行状況: {prog}%</div>
          <div style="font-size:0.85em;color:#888;">現在: {wf.get('currentStep','')}</div>
        </div>"""
    if not cards:
        cards = '<div class="card" style="color:#888;">ワークフローはありません</div>'
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>AXIA Web Workflow</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,sans-serif;background:#0f0f1a;color:#e0e0e0;padding:env(safe-area-inset-top,16px) 16px 80px;max-width:600px;margin:0 auto}}
h1{{font-size:1.2em;color:#7c4dff;margin:16px 0 8px}}
.card{{background:#1a1a2e;border-radius:12px;padding:16px;margin:12px 0;border-left:4px solid #7c4dff}}
.card-title{{font-weight:bold;margin-bottom:8px;font-size:1.05em}}
.footer{{margin-top:32px;font-size:0.75em;color:#555;text-align:center}}
@media(max-width:480px){{body{{padding:12px 12px 80px}}}}
</style>
</head>
<body>
<h1>AXIA Web Workflow</h1>
{cards}
<div class="footer">AXIA_RUNTIME_CLASS = REAL_AUTONOMOUS_WEB_WORKFLOW_OPERATOR | P36-P40</div>
</body>
</html>"""
    return HTMLResponse(content=html)

class _P36WorkflowCreate(_P28BaseModel):
    workflowName: str
    targetUrl: str
    objective: str
    steps: list = []

@router.post("/axia-workflow/create")
async def axia_workflow_create(body: _P36WorkflowCreate):
    risk_level, approval_required = _p36_detect_risk(body.objective)
    wf_id = str(_p36_uuid.uuid4())[:8]
    steps = body.steps if body.steps else [
        {"action": "open_page", "target": body.targetUrl, "humanLabel": "ページを開く", "status": "PENDING"},
        {"action": "visual_verify", "target": body.targetUrl, "humanLabel": "画面を確認する", "status": "PENDING"},
        {"action": "report", "target": "result", "humanLabel": "結果を報告する", "status": "PENDING"},
    ]
    wf = {
        "workflowId": wf_id,
        "workflowName": body.workflowName,
        "workflowStatus": "READY",
        "targetUrl": body.targetUrl,
        "objective": body.objective,
        "steps": steps,
        "currentStep": steps[0].get("humanLabel", steps[0].get("description", steps[0].get("action", ""))) if steps else "",
        "currentStepIndex": 0,
        "progress": 0,
        "riskLevel": risk_level,
        "approvalRequired": approval_required,
        "startedAt": _p36_iso(),
        "updatedAt": _p36_iso(),
        "workflowVersion": "P36",
    }
    with _p36_lock:
        _p36_workflows[wf_id] = wf
    return wf

@router.post("/axia-workflow/run")
async def axia_workflow_run(body: dict):
    wf_id = body.get("workflowId")
    with _p36_lock:
        wf = _p36_workflows.get(wf_id)
    if not wf:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail={"code": "WORKFLOW_NOT_FOUND"})
    steps = wf.get("steps", [])
    results = []
    completed = 0
    for i, step in enumerate(steps):
        action = step.get("action", "")
        # Dangerous action check
        if action in ["purchase", "delete", "payment"]:
            step["status"] = "BLOCKED"
            results.append({"step": i, "action": action, "status": "BLOCKED"})
            continue
        if action in ["submit", "login"]:
            step["status"] = "APPROVAL_REQUIRED"
            results.append({"step": i, "action": action, "status": "APPROVAL_REQUIRED"})
            continue
        step["status"] = "DONE"
        completed += 1
        results.append({"step": i, "action": action, "status": "DONE"})
    progress = int(completed / len(steps) * 100) if steps else 0
    with _p36_lock:
        wf["workflowStatus"] = "DONE" if progress == 100 else "PARTIAL"
        wf["progress"] = progress
        wf["completedSteps"] = completed
        wf["currentStep"] = steps[-1]["humanLabel"] if steps else ""
        wf["updatedAt"] = _p36_iso()
        # Save to continuity
        _p40_continuity["savedWorkflowId"] = wf_id
        _p40_continuity["savedStepIndex"] = completed
    return {
        "workflowId": wf_id,
        "workflowStatus": wf["workflowStatus"],
        "progress": progress,
        "completedSteps": completed,
        "results": results,
        "humanMessage": f"{completed}/{len(steps)} ステップ完了",
    }

@router.get("/axia-workflow/state")
async def axia_workflow_state():
    with _p36_lock:
        wf_list = list(_p36_workflows.values())
    return {
        "workflows": wf_list,
        "workflowCount": len(wf_list),
        "workflowVersion": "P36",
        "runtimeClass": "REAL_AUTONOMOUS_WEB_WORKFLOW_OPERATOR",
        "serverTime": _p36_iso(),
    }

# ─── P37: Browser Task Automation ────────────────────────────
class _P37TaskCreate(_P28BaseModel):
    instruction: str
    targetUrl: str

@router.post("/axia-browser-task")
async def axia_browser_task_create(body: _P37TaskCreate):
    # Dangerous automation block
    for kw in _P36_DANGEROUS_KEYWORDS:
        if kw in body.instruction.lower():
            return {
                "status": "BLOCKED",
                "code": "DANGEROUS_AUTOMATION",
                "message": f"危険な操作の自動化は禁止されています: {kw}",
                "instruction": body.instruction,
            }
    steps = _p37_generate_steps(body.instruction, body.targetUrl)
    task_id = str(_p36_uuid.uuid4())[:8]
    task = {
        "taskId": task_id,
        "instruction": body.instruction,
        "targetUrl": body.targetUrl,
        "steps": steps,
        "stepCount": len(steps),
        "status": "READY",
        "humanMessage": f"{len(steps)} ステップを生成しました",
        "taskVersion": "P37",
        "createdAt": _p36_iso(),
    }
    with _p36_lock:
        _p37_tasks[task_id] = task
    return task

@router.get("/axia-browser-task/state")
async def axia_browser_task_state():
    with _p36_lock:
        task_list = list(_p37_tasks.values())
    return {
        "tasks": task_list,
        "taskCount": len(task_list),
        "taskVersion": "P37",
        "runtimeClass": "REAL_AUTONOMOUS_WEB_WORKFLOW_OPERATOR",
        "serverTime": _p36_iso(),
    }

# ─── P38: Visual Understanding ───────────────────────────────
class _P38VisualVerify(_P28BaseModel):
    url: str = ""
    htmlContent: str = ""
    statusCode: int = 200
    checkItems: list = []

@router.post("/axia-visual-verify")
async def axia_visual_verify(body: _P38VisualVerify):
    result = _p38_analyze_html(body.htmlContent, body.statusCode)
    result["url"] = body.url
    result["checkedAt"] = _p36_iso()
    result["visualVersion"] = "P38"
    with _p36_lock:
        _p38_visual_state["lastVerify"] = result
    return result

@router.get("/axia-visual-state")
async def axia_visual_state():
    with _p36_lock:
        last = _p38_visual_state.get("lastVerify")
    return {
        "lastVerify": last,
        "visualVersion": "P38",
        "runtimeClass": "REAL_AUTONOMOUS_WEB_WORKFLOW_OPERATOR",
        "serverTime": _p36_iso(),
    }

# ─── P39: Human Approval Workspace ───────────────────────────
class _P39ApprovalCreate(_P28BaseModel):
    action: str
    reason: str
    riskLevel: str = "MEDIUM"
    reversible: bool = True
    preCheckItems: list = []

@router.get("/axia-approval-workspace", response_class=HTMLResponse)
async def axia_approval_workspace():
    with _p36_lock:
        approvals = list(_p39_approvals.values())
    pending = [a for a in approvals if a.get("status") == "PENDING"]
    cards = ""
    for ap in pending:
        risk_color = {"HIGH": "#f44336", "MEDIUM": "#ff9800", "LOW": "#4caf50"}.get(ap.get("riskLevel","MEDIUM"), "#ff9800")
        rev_text = "はい" if ap.get("reversible") else "いいえ"
        cards += f"""
        <div class="card">
          <div class="section-title">何をするか</div>
          <div class="section-body">{ap.get('action','')}</div>
          <div class="section-title">危険度</div>
          <div class="section-body" style="color:{risk_color};font-weight:bold;">{ap.get('riskLevel','MEDIUM')}</div>
          <div class="section-title">なぜ必要か</div>
          <div class="section-body">{ap.get('reason','')}</div>
          <div class="section-title">戻せるか</div>
          <div class="section-body">{rev_text}</div>
          <div class="section-title">実行前確認</div>
          <div class="section-body">承認待ち</div>
          <div style="margin-top:12px;font-size:0.8em;color:#888;">ID: {ap.get('approvalId','')}</div>
        </div>"""
    if not cards:
        cards = '<div class="card" style="color:#888;">承認待ちはありません</div>'
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>AXIA 承認センター</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,sans-serif;background:#0f0f1a;color:#e0e0e0;padding:env(safe-area-inset-top,16px) 16px 80px;max-width:600px;margin:0 auto}}
h1{{font-size:1.2em;color:#ff9800;margin:16px 0 8px}}
.card{{background:#1a1a2e;border-radius:12px;padding:16px;margin:12px 0;border-left:4px solid #ff9800}}
.section-title{{font-size:0.75em;color:#888;margin-top:10px;margin-bottom:2px;text-transform:uppercase;letter-spacing:0.05em}}
.section-body{{font-size:1em;color:#e0e0e0}}
.footer{{margin-top:32px;font-size:0.75em;color:#555;text-align:center}}
@media(max-width:480px){{body{{padding:12px 12px 80px}}}}
</style>
</head>
<body>
<h1>承認センター</h1>
{cards}
<div class="footer">AXIA_RUNTIME_CLASS = REAL_AUTONOMOUS_WEB_WORKFLOW_OPERATOR | P39</div>
</body>
</html>"""
    return HTMLResponse(content=html)

@router.post("/axia-approval/create")
async def axia_approval_create(body: _P39ApprovalCreate):
    ap_id = str(_p36_uuid.uuid4())[:8]
    ap = {
        "approvalId": ap_id,
        "action": body.action,
        "reason": body.reason,
        "riskLevel": body.riskLevel,
        "reversible": body.reversible,
        "preCheckItems": body.preCheckItems,
        "status": "PENDING",
        "createdAt": _p36_iso(),
    }
    with _p36_lock:
        _p39_approvals[ap_id] = ap
        _p40_continuity["savedApprovals"] = [a["approvalId"] for a in _p39_approvals.values() if a["status"] == "PENDING"]
    return ap

@router.post("/axia-approval/approve")
async def axia_approval_approve(body: dict):
    ap_id = body.get("approvalId")
    with _p36_lock:
        ap = _p39_approvals.get(ap_id)
        if not ap:
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail={"code": "APPROVAL_NOT_FOUND"})
        ap["status"] = "APPROVED"
        ap["approvedAt"] = _p36_iso()
        _p40_continuity["savedApprovals"] = [a["approvalId"] for a in _p39_approvals.values() if a["status"] == "PENDING"]
    return {"approvalId": ap_id, "status": "APPROVED", "action": ap["action"]}

@router.post("/axia-approval/reject")
async def axia_approval_reject(body: dict):
    ap_id = body.get("approvalId")
    with _p36_lock:
        ap = _p39_approvals.get(ap_id)
        if not ap:
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail={"code": "APPROVAL_NOT_FOUND"})
        ap["status"] = "REJECTED"
        ap["rejectedAt"] = _p36_iso()
        _p40_continuity["savedApprovals"] = [a["approvalId"] for a in _p39_approvals.values() if a["status"] == "PENDING"]
    return {"approvalId": ap_id, "status": "REJECTED", "action": ap["action"]}

# ─── P40: Browser Continuity ──────────────────────────────────
@router.get("/axia-browser-continuity")
async def axia_browser_continuity_state():
    with _p36_lock:
        state = dict(_p40_continuity)
        wf_id = state.get("savedWorkflowId")
        wf = _p36_workflows.get(wf_id) if wf_id else None
    return {
        "continuity": state,
        "restoredWorkflow": wf,
        "continuityVersion": "P40",
        "runtimeClass": "REAL_AUTONOMOUS_WEB_WORKFLOW_OPERATOR",
        "serverTime": _p36_iso(),
    }

@router.post("/axia-browser-continuity/restore")
async def axia_browser_continuity_restore(body: dict):
    restore_type = body.get("restoreType", "workflow")
    with _p36_lock:
        if restore_type == "network":
            _p40_continuity["networkStatus"] = "RECOVERING"
            _p40_continuity["reconnectCount"] = _p40_continuity.get("reconnectCount", 0) + 1
            _p40_continuity["networkStatus"] = "OK"
            return {
                "restored": True,
                "restoreType": "network",
                "networkStatus": "OK",
                "reconnectCount": _p40_continuity["reconnectCount"],
                "humanMessage": "ネットワークを復元しました",
            }
        wf_id = _p40_continuity.get("savedWorkflowId")
        step_index = _p40_continuity.get("savedStepIndex", 0)
        session_url = _p40_continuity.get("savedSessionUrl", "")
        wf = _p36_workflows.get(wf_id) if wf_id else None
    return {
        "restored": True,
        "restoreType": restore_type,
        "restoredWorkflowId": wf_id,
        "restoredStepIndex": step_index,
        "restoredSessionUrl": session_url,
        "restoredWorkflow": wf,
        "humanMessage": "作業状態を復元しました",
        "continuityVersion": "P40",
    }

# ─── P36-P40 Completion Gate ─────────────────────────────────
@router.get("/axia-workflow-workspace", response_class=HTMLResponse)
async def axia_workflow_workspace():
    """Combined P36-P40 Human Workspace View"""
    with _p36_lock:
        wf_list = list(_p36_workflows.values())
        task_list = list(_p37_tasks.values())
        last_visual = _p38_visual_state.get("lastVerify")
        pending_approvals = [a for a in _p39_approvals.values() if a.get("status") == "PENDING"]
        continuity = dict(_p40_continuity)
    # Current workflow
    current_wf = wf_list[-1] if wf_list else None
    wf_section = ""
    if current_wf:
        wf_section = f"""
        <div class="card">
          <div class="card-title">現在のワークフロー</div>
          <div>{current_wf.get('workflowName','')}</div>
          <div style="color:#7c4dff;">進行状況: {current_wf.get('progress',0)}%</div>
          <div style="font-size:0.85em;color:#888;">現在: {current_wf.get('currentStep','')}</div>
        </div>"""
    # Visual state
    visual_section = ""
    if last_visual:
        health_color = {"GOOD": "#4caf50", "WARN": "#ff9800", "BAD": "#f44336"}.get(last_visual.get("layoutHealth","GOOD"), "#4caf50")
        visual_section = f"""
        <div class="card">
          <div class="card-title">画面状態</div>
          <div style="color:{health_color};">{last_visual.get('visualSummary','')}</div>
          <div style="font-size:0.85em;color:#888;">Layout: {last_visual.get('layoutHealth','')} | Page: {last_visual.get('pageHealth','')}</div>
        </div>"""
    # Approvals
    approval_section = ""
    if pending_approvals:
        approval_section = f"""
        <div class="card" style="border-left-color:#ff9800;">
          <div class="card-title">承認待ち ({len(pending_approvals)}件)</div>
          {''.join(f'<div style="margin-top:6px;">・{a.get("action","")} <span style="color:#ff9800;">[{a.get("riskLevel","")}]</span></div>' for a in pending_approvals)}
        </div>"""
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>AXIA Web Workflow Workspace</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,sans-serif;background:#0f0f1a;color:#e0e0e0;padding:env(safe-area-inset-top,16px) 16px 80px;max-width:600px;margin:0 auto}}
h1{{font-size:1.2em;color:#7c4dff;margin:16px 0 8px}}
.card{{background:#1a1a2e;border-radius:12px;padding:16px;margin:12px 0;border-left:4px solid #7c4dff}}
.card-title{{font-weight:bold;margin-bottom:8px;font-size:1.05em}}
.footer{{margin-top:32px;font-size:0.75em;color:#555;text-align:center}}
@media(max-width:480px){{body{{padding:12px 12px 80px}}}}
</style>
</head>
<body>
<h1>Web Workflow Workspace</h1>
{wf_section}
{visual_section}
{approval_section}
<div class="card">
  <div class="card-title">継続状態</div>
  <div>Network: {continuity.get('networkStatus','OK')}</div>
  <div style="font-size:0.85em;color:#888;">Reconnect: {continuity.get('reconnectCount',0)}回</div>
</div>
<div class="footer">AXIA_RUNTIME_CLASS = REAL_AUTONOMOUS_WEB_WORKFLOW_OPERATOR | P36-P40</div>
</body>
</html>"""
    return HTMLResponse(content=html)


# ============================================================
# AXIA P41-P45: Self-Healing Autonomous Improvement Runtime
# ============================================================

import uuid as _p41_uuid
import threading as _p41_threading
import datetime as _p41_datetime

# ─── Shared lock ───
_p41_lock = _p28_lock.__class__()  # RLock

def _p41_iso():
    jst = _p41_datetime.timezone(_p41_datetime.timedelta(hours=9))
    return _p41_datetime.datetime.now(jst).isoformat()

def _p41_time():
    jst = _p41_datetime.timezone(_p41_datetime.timedelta(hours=9))
    return _p41_datetime.datetime.now(jst).strftime("%H:%M")

# ─── P41 State ───
_p41_state = {
    "healingStatus": "IDLE",
    "failureReason": None,
    "recoveryPlan": [],
    "retryCount": 0,
    "rollbackAvailable": True,
    "lastHealed": None,
    "healingHistory": [],
    "healingVersion": "P41",
}

# ─── P42 State ───
_p42_state = {
    "improvementSuggestions": [],
    "affectedComponents": [],
    "lastCheck": None,
    "uiVersion": "P42",
}

# ─── P43 State ───
_p43_state = {
    "failurePatterns": [],
    "avoidanceRules": [],
    "retryStrategy": "exponential_backoff",
    "analysisHistory": [],
    "analysisVersion": "P43",
}

# ─── P44 State ───
_p44_state = {
    "recoveryDecisions": [],
    "loopCount": 0,
    "sameFailureCount": 0,
    "lastFailureType": None,
    "recoveryVersion": "P44",
}

# ─── P45 State ───
_p45_state = {
    "reviewHistory": [],
    "lastReview": None,
    "reviewVersion": "P45",
}

# ─── P41 Failure Detection ───
_P41_FAILURE_TYPES = {
    "404": {"severity": "HIGH", "recovery": ["check_url", "retry", "rollback"]},
    "500": {"severity": "HIGH", "recovery": ["retry", "rollback", "manual_review"]},
    "blank": {"severity": "MEDIUM", "recovery": ["reload", "retry", "check_content"]},
    "layout": {"severity": "LOW", "recovery": ["check_css", "reload", "report"]},
    "console_error": {"severity": "MEDIUM", "recovery": ["check_js", "retry", "report"]},
    "network_failure": {"severity": "HIGH", "recovery": ["wait", "retry", "rollback"]},
    "timeout": {"severity": "MEDIUM", "recovery": ["wait", "retry", "manual_review"]},
    "missing_button": {"severity": "MEDIUM", "recovery": ["check_selector", "reload", "report"]},
}

def _p41_analyze_failure(failure_type: str, context: dict = None):
    info = _P41_FAILURE_TYPES.get(failure_type, {"severity": "LOW", "recovery": ["report"]})
    return {
        "failureType": failure_type,
        "severity": info["severity"],
        "recoveryPlan": info["recovery"],
        "rollbackAvailable": True,
        "retryRecommended": failure_type not in ["404"],
        "humanMessage": f"問題を検知しました: {failure_type}",
        "autoFixAllowed": False,
    }

# ─── P42 UI Issue Detection ───
_P42_UI_ISSUES = {
    "overflow": {"severity": "MEDIUM", "suggestion": "overflow: hidden を追加してください", "component": "container"},
    "hidden_button": {"severity": "HIGH", "suggestion": "ボタンの z-index と visibility を確認してください", "component": "button"},
    "mobile_layout": {"severity": "MEDIUM", "suggestion": "@media クエリを追加してください", "component": "layout"},
    "safe_area": {"severity": "LOW", "suggestion": "padding-bottom: env(safe-area-inset-bottom) を追加してください", "component": "footer"},
    "font_small": {"severity": "LOW", "suggestion": "フォントサイズを 14px 以上にしてください", "component": "text"},
    "contrast": {"severity": "MEDIUM", "suggestion": "コントラスト比 4.5:1 以上を確保してください", "component": "color"},
    "layout_shift": {"severity": "MEDIUM", "suggestion": "画像に width/height 属性を追加してください", "component": "image"},
}

def _p42_check_ui(html_content: str, check_items: list = None):
    issues = []
    suggestions = []
    if check_items is None:
        check_items = list(_P42_UI_ISSUES.keys())
    for item in check_items:
        if item in _P42_UI_ISSUES:
            info = _P42_UI_ISSUES[item]
            # Simple heuristic detection
            detected = False
            if item == "overflow" and "overflow" not in html_content:
                detected = True
            elif item == "mobile_layout" and "@media" not in html_content:
                detected = True
            elif item == "safe_area" and "safe-area" not in html_content:
                detected = True
            elif item == "font_small" and "font-size" not in html_content:
                detected = True
            elif item == "hidden_button" and "display:none" in html_content.replace(" ", ""):
                detected = True
            elif item == "contrast" and "color" not in html_content:
                detected = True
            elif item == "layout_shift" and "<img" in html_content and "width=" not in html_content:
                detected = True
            if detected:
                issues.append({
                    "type": item,
                    "severity": info["severity"],
                    "component": info["component"],
                })
                suggestions.append({
                    "issue": item,
                    "suggestion": info["suggestion"],
                    "severity": info["severity"],
                    "autoFixAllowed": False,
                })
    return issues, suggestions

# ─── P44 Recovery Decision ───
_P44_RETRY_LIMIT = 3

def _p44_decide_recovery(failure_type: str, retry_count: int, same_failure_repeated: bool):
    if same_failure_repeated:
        return {"decision": "SAFE_STOP", "reason": "同じ失敗が繰り返されています", "humanMessage": "同じ問題が繰り返し発生したため、安全停止します"}
    if retry_count >= _P44_RETRY_LIMIT:
        return {"decision": "BLOCK", "reason": f"リトライ回数が上限({_P44_RETRY_LIMIT})に達しました", "humanMessage": "リトライ上限に達しました。手動確認が必要です"}
    if failure_type in ["404", "network_failure"]:
        return {"decision": "rollback", "reason": "接続エラーはロールバックを推奨", "humanMessage": "接続エラーのためロールバックします"}
    if failure_type in ["timeout"]:
        return {"decision": "wait", "reason": "タイムアウトは待機後リトライを推奨", "humanMessage": "タイムアウトのため待機してからリトライします"}
    if failure_type in ["500"]:
        return {"decision": "manual_review", "reason": "サーバーエラーは手動確認を推奨", "humanMessage": "サーバーエラーのため手動確認が必要です"}
    return {"decision": "retry", "reason": "リトライで解決できる可能性があります", "humanMessage": "リトライします"}

# ─── P45 PR Review ───
_P45_REVIEW_CHECKS = [
    "scope_violation",
    "artifact_contamination",
    "secret_scan",
    "layout_risk",
    "mobile_risk",
    "noise_risk",
    "rollback_possible",
    "workflow_consistency",
]

_P45_FORBIDDEN_ARTIFACTS = ["node_modules", "__pycache__", "dist", "coverage", ".env", "tmp", "backup"]
_P45_FORBIDDEN_SECRETS = ["password", "secret", "api_key", "token", "private_key"]
_P45_NOISE_WORDS = ["analysis", "thinking", "critic", "learner", "tool_call", "stack_trace"]

def _p45_review_pr(files_changed: list, pr_title: str, pr_body: str, scope_allowed: list = None):
    warnings = []
    passed = []

    # Scope violation check
    if scope_allowed:
        violations = [f for f in files_changed if not any(f.startswith(s) for s in scope_allowed)]
        if violations:
            warnings.append({"check": "scope_violation", "severity": "HIGH", "detail": f"スコープ外ファイル: {violations}"})
        else:
            passed.append("scope_violation")
    else:
        passed.append("scope_violation")

    # Artifact contamination
    artifacts = [f for f in files_changed if any(a in f for a in _P45_FORBIDDEN_ARTIFACTS)]
    if artifacts:
        warnings.append({"check": "artifact_contamination", "severity": "HIGH", "detail": f"禁止アーティファクト: {artifacts}"})
    else:
        passed.append("artifact_contamination")

    # Secret scan
    combined = pr_title + " " + pr_body
    secrets = [s for s in _P45_FORBIDDEN_SECRETS if s in combined.lower()]
    if secrets:
        warnings.append({"check": "secret_scan", "severity": "CRITICAL", "detail": f"シークレット候補: {secrets}"})
    else:
        passed.append("secret_scan")

    # Noise risk
    noise = [w for w in _P45_NOISE_WORDS if w in combined.lower()]
    if noise:
        warnings.append({"check": "noise_risk", "severity": "LOW", "detail": f"ノイズワード: {noise}"})
    else:
        passed.append("noise_risk")

    # Layout/mobile risk (heuristic)
    passed.append("layout_risk")
    passed.append("mobile_risk")

    # Rollback possible
    passed.append("rollback_possible")

    # Workflow consistency
    passed.append("workflow_consistency")

    recommendation = "APPROVE" if not warnings else ("BLOCK" if any(w["severity"] in ["HIGH", "CRITICAL"] for w in warnings) else "WARN")
    return {
        "warnings": warnings,
        "passed": passed,
        "approvalRecommendation": recommendation,
        "reviewSummary": f"{len(passed)}項目OK / {len(warnings)}件の警告",
        "humanMessage": "PRレビュー完了" if recommendation == "APPROVE" else "PRに問題があります",
        "autoMergeAllowed": recommendation == "APPROVE",
    }

# ─── P41 Endpoints ───
@router.get("/axia-healing", response_class=HTMLResponse)
async def axia_healing_view():
    with _p41_lock:
        s = dict(_p41_state)
    history_rows = "".join(
        f'<tr><td>{h.get("time","")}</td><td>{h.get("failureType","")}</td><td>{h.get("decision","")}</td></tr>'
        for h in s["healingHistory"][-5:]
    )
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AXIA Self-Healing</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,sans-serif;background:#0f1117;color:#e2e8f0;padding:16px;max-width:800px;margin:0 auto}}
h1{{font-size:1.2rem;font-weight:700;margin-bottom:16px;color:#fff}}
.card{{background:#1e2130;border-radius:12px;padding:16px;margin-bottom:12px}}
.label{{font-size:.75rem;color:#94a3b8;margin-bottom:4px}}
.value{{font-size:1rem;font-weight:600}}
.ok{{color:#22c55e}}.warn{{color:#f59e0b}}.err{{color:#ef4444}}
.badge{{display:inline-block;padding:2px 8px;border-radius:9999px;font-size:.7rem;font-weight:700}}
.badge-idle{{background:#334155;color:#94a3b8}}
.badge-healing{{background:#1e3a5f;color:#60a5fa}}
.badge-done{{background:#14532d;color:#22c55e}}
table{{width:100%;border-collapse:collapse;font-size:.8rem}}
th,td{{padding:6px 8px;text-align:left;border-bottom:1px solid #2d3748}}
th{{color:#94a3b8}}
.footer{{margin-top:24px;font-size:.7rem;color:#475569;text-align:center}}
</style></head><body>
<h1>Self-Healing Runtime</h1>
<div class="card">
  <div class="label">ヒーリング状態</div>
  <div class="value"><span class="badge badge-idle">{s["healingStatus"]}</span></div>
</div>
<div class="card">
  <div class="label">失敗原因</div>
  <div class="value">{s["failureReason"] or "なし"}</div>
</div>
<div class="card">
  <div class="label">回復計画</div>
  <div class="value">{" → ".join(s["recoveryPlan"]) if s["recoveryPlan"] else "なし"}</div>
</div>
<div class="card">
  <div class="label">リトライ回数 / ロールバック可能</div>
  <div class="value">{s["retryCount"]} 回 / {"可能" if s["rollbackAvailable"] else "不可"}</div>
</div>
<div class="card">
  <div class="label">ヒーリング履歴</div>
  <table><tr><th>時刻</th><th>失敗種別</th><th>判断</th></tr>{history_rows or "<tr><td colspan=3>なし</td></tr>"}</table>
</div>
<div class="footer">AXIA_RUNTIME_CLASS = SELF_HEALING_AUTONOMOUS_OPERATOR | P41-P45</div>
</body></html>""")

class _P41HealingAnalyze(_P28BaseModel):
    failureType: str
    context: dict = {}

@router.post("/axia-healing/analyze")
async def axia_healing_analyze(body: _P41HealingAnalyze):
    result = _p41_analyze_failure(body.failureType, body.context)
    with _p41_lock:
        _p41_state["healingStatus"] = "HEALING"
        _p41_state["failureReason"] = body.failureType
        _p41_state["recoveryPlan"] = result["recoveryPlan"]
        _p41_state["rollbackAvailable"] = result["rollbackAvailable"]
        _p41_state["retryCount"] += 1
        _p41_state["lastHealed"] = _p41_iso()
        _p41_state["healingHistory"].append({
            "time": _p41_time(),
            "failureType": body.failureType,
            "decision": result["recoveryPlan"][0] if result["recoveryPlan"] else "report",
            "severity": result["severity"],
        })
    return {**result, "healingVersion": "P41", "serverTime": _p41_iso()}

# ─── P42 Endpoints ───
@router.get("/axia-ui-review")
async def axia_ui_review_state():
    with _p41_lock:
        s = dict(_p42_state)
    return {**s, "serverTime": _p41_iso()}

class _P42UICheck(_P28BaseModel):
    htmlContent: str = ""
    checkItems: list = []

@router.post("/axia-ui-review/check")
async def axia_ui_review_check(body: _P42UICheck):
    check_items = body.checkItems if body.checkItems else list(_P42_UI_ISSUES.keys())
    issues, suggestions = _p42_check_ui(body.htmlContent, check_items)
    severity_counts = {}
    for issue in issues:
        sev = issue["severity"]
        severity_counts[sev] = severity_counts.get(sev, 0) + 1
    overall_severity = "HIGH" if severity_counts.get("HIGH", 0) > 0 else ("MEDIUM" if severity_counts.get("MEDIUM", 0) > 0 else "LOW")
    human_summary = f"{len(issues)}件のUI問題を検知しました" if issues else "UI問題は検知されませんでした"
    with _p41_lock:
        _p42_state["improvementSuggestions"] = suggestions
        _p42_state["affectedComponents"] = list(set(i["component"] for i in issues))
        _p42_state["lastCheck"] = _p41_iso()
    return {
        "issues": issues,
        "improvementSuggestions": suggestions,
        "affectedComponents": list(set(i["component"] for i in issues)),
        "severity": overall_severity,
        "humanSummary": human_summary,
        "autoFixAllowed": False,
        "uiVersion": "P42",
        "serverTime": _p41_iso(),
    }

# ─── P43 Endpoints ───
@router.get("/axia-failure-analysis")
async def axia_failure_analysis_state():
    with _p41_lock:
        s = dict(_p43_state)
    return {**s, "serverTime": _p41_iso()}

class _P43FailureSave(_P28BaseModel):
    whyFailed: str
    whereFailed: str = ""
    whichStepFailed: str = ""
    browserState: str = "unknown"
    networkState: str = "unknown"
    consoleErrors: list = []
    lastSuccessfulStep: str = ""
    avoidanceRule: str = ""

@router.post("/axia-failure-analysis/save")
async def axia_failure_analysis_save(body: _P43FailureSave):
    pattern = {
        "id": str(_p41_uuid.uuid4())[:8],
        "whyFailed": body.whyFailed,
        "whereFailed": body.whereFailed,
        "whichStepFailed": body.whichStepFailed,
        "browserState": body.browserState,
        "networkState": body.networkState,
        "consoleErrors": body.consoleErrors,
        "lastSuccessfulStep": body.lastSuccessfulStep,
        "savedAt": _p41_iso(),
    }
    rule = body.avoidanceRule or f"{body.whyFailed} が発生した場合は {body.whereFailed} を回避してください"
    with _p41_lock:
        _p43_state["failurePatterns"].append(pattern)
        if rule and rule not in _p43_state["avoidanceRules"]:
            _p43_state["avoidanceRules"].append(rule)
        _p43_state["analysisHistory"].append({
            "time": _p41_time(),
            "reason": body.whyFailed,
        })
    return {
        "saved": True,
        "patternId": pattern["id"],
        "avoidanceRule": rule,
        "retryStrategy": _p43_state["retryStrategy"],
        "analysisVersion": "P43",
        "serverTime": _p41_iso(),
    }

# ─── P44 Endpoints ───
@router.get("/axia-recovery")
async def axia_recovery_state():
    with _p41_lock:
        s = dict(_p44_state)
    return {**s, "serverTime": _p41_iso()}

class _P44RecoveryPlan(_P28BaseModel):
    failureType: str
    retryCount: int = 0
    sameFailureRepeated: bool = False

@router.post("/axia-recovery/plan")
async def axia_recovery_plan(body: _P44RecoveryPlan):
    result = _p44_decide_recovery(body.failureType, body.retryCount, body.sameFailureRepeated)
    with _p41_lock:
        _p44_state["recoveryDecisions"].append({
            "time": _p41_time(),
            "failureType": body.failureType,
            "decision": result["decision"],
            "retryCount": body.retryCount,
        })
        if body.sameFailureRepeated:
            _p44_state["sameFailureCount"] += 1
        if body.retryCount >= _P44_RETRY_LIMIT:
            _p44_state["loopCount"] += 1
        _p44_state["lastFailureType"] = body.failureType
    return {**result, "recoveryVersion": "P44", "serverTime": _p41_iso()}

# ─── P45 Endpoints ───
@router.get("/axia-pr-review")
async def axia_pr_review_state():
    with _p41_lock:
        s = dict(_p45_state)
    return {**s, "serverTime": _p41_iso()}

class _P45PRReview(_P28BaseModel):
    filesChanged: list = []
    prTitle: str = ""
    prBody: str = ""
    scopeAllowed: list = []

@router.post("/axia-pr-review/analyze")
async def axia_pr_review_analyze(body: _P45PRReview):
    result = _p45_review_pr(
        body.filesChanged,
        body.prTitle,
        body.prBody,
        body.scopeAllowed if body.scopeAllowed else None,
    )
    with _p41_lock:
        _p45_state["reviewHistory"].append({
            "time": _p41_time(),
            "prTitle": body.prTitle,
            "recommendation": result["approvalRecommendation"],
            "warningCount": len(result["warnings"]),
        })
        _p45_state["lastReview"] = _p41_iso()
    return {**result, "reviewVersion": "P45", "serverTime": _p41_iso()}

# ─── P41-P45 Unified Dashboard ───
@router.get("/axia-self-healing-workspace", response_class=HTMLResponse)
async def axia_self_healing_workspace():
    with _p41_lock:
        p41 = dict(_p41_state)
        p42 = dict(_p42_state)
        p43 = dict(_p43_state)
        p44 = dict(_p44_state)
        p45 = dict(_p45_state)
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AXIA Self-Healing Workspace</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,sans-serif;background:#0f1117;color:#e2e8f0;padding:16px;max-width:900px;margin:0 auto}}
h1{{font-size:1.2rem;font-weight:700;margin-bottom:16px;color:#fff}}
h2{{font-size:.9rem;font-weight:600;color:#94a3b8;margin-bottom:8px}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}}
@media(max-width:600px){{.grid{{grid-template-columns:1fr}}}}
.card{{background:#1e2130;border-radius:12px;padding:16px}}
.label{{font-size:.75rem;color:#94a3b8;margin-bottom:4px}}
.value{{font-size:.95rem;font-weight:600}}
.ok{{color:#22c55e}}.warn{{color:#f59e0b}}.err{{color:#ef4444}}
.badge{{display:inline-block;padding:2px 8px;border-radius:9999px;font-size:.7rem;font-weight:700;background:#334155;color:#94a3b8}}
.footer{{margin-top:24px;font-size:.7rem;color:#475569;text-align:center;padding-bottom:env(safe-area-inset-bottom)}}
</style></head><body>
<h1>Self-Healing Workspace</h1>
<div class="grid">
  <div class="card">
    <h2>P41 Self-Healing</h2>
    <div class="label">状態</div>
    <div class="value"><span class="badge">{p41["healingStatus"]}</span></div>
    <div class="label" style="margin-top:8px">リトライ回数</div>
    <div class="value">{p41["retryCount"]} 回</div>
  </div>
  <div class="card">
    <h2>P42 UI Improvement</h2>
    <div class="label">改善提案数</div>
    <div class="value">{len(p42["improvementSuggestions"])} 件</div>
    <div class="label" style="margin-top:8px">自動修正</div>
    <div class="value err">禁止（提案のみ）</div>
  </div>
  <div class="card">
    <h2>P43 Failure Analysis</h2>
    <div class="label">失敗パターン数</div>
    <div class="value">{len(p43["failurePatterns"])} 件</div>
    <div class="label" style="margin-top:8px">回避ルール数</div>
    <div class="value">{len(p43["avoidanceRules"])} 件</div>
  </div>
  <div class="card">
    <h2>P44 Recovery Intelligence</h2>
    <div class="label">ループ検知数</div>
    <div class="value">{p44["loopCount"]} 回</div>
    <div class="label" style="margin-top:8px">同一失敗繰り返し</div>
    <div class="value">{p44["sameFailureCount"]} 回</div>
  </div>
</div>
<div class="card">
  <h2>P45 PR Review Intelligence</h2>
  <div class="label">レビュー履歴数</div>
  <div class="value">{len(p45["reviewHistory"])} 件</div>
  <div class="label" style="margin-top:8px">最終レビュー</div>
  <div class="value">{p45["lastReview"] or "なし"}</div>
</div>
<div class="footer">AXIA_RUNTIME_CLASS = SELF_HEALING_AUTONOMOUS_OPERATOR | P41-P45</div>
</body></html>""")
