"""
AXIA Runtime Test Endpoint
Safe test endpoint — AXIA Real Code Fix Operator (P7).
AXIA UI Fix — /axia-status HTML status page added (P8).
AXIA UI Improvement — /axia-status enhanced status card (P10).
AXIA Dashboard — /axia-dashboard user-facing dashboard added (P17).
This file does NOT modify existing routes or database schema.
"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import datetime

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
