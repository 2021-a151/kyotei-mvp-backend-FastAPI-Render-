# kyotei-mvp-backend-FastAPI-Render-

競艇予想 MVP バックエンド API（FastAPI + Render デプロイ対応）

---

## 概要

FastAPI を使用した競艇予想サービスのバックエンド API です。  
Render へのデプロイを前提とした構成になっています。

---

## 起動方法

```bash
# 依存パッケージのインストール
pip install -r requirements.txt

# 開発サーバー起動
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 本番起動（Render / Railway 等）
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## 環境変数

| 変数名 | 必須 | 説明 |
|--------|------|------|
| `DATABASE_URL` | **必須** | PostgreSQL 接続 URL（例: `postgresql://user:pass@host:5432/dbname`） |
| `PORT` | 任意 | リッスンポート（Render は自動設定、デフォルト: 8000） |

---

## API エンドポイント

| メソッド | パス | 説明 |
|----------|------|------|
| GET | `/` | ルートヘルスチェック（`{"ok": true}`） |
| GET | `/api/health` | アプリケーションヘルスチェック |
| GET | `/api/health/db` | DB 接続ヘルスチェック（DATABASE_URL 必要） |
| GET | `/docs` | Swagger UI（開発時） |
| GET | `/redoc` | ReDoc ドキュメント |

---

## ランタイム

- Python: `3.12.8`（`runtime.txt` 参照）
- FastAPI: `0.115.6`
- Uvicorn: `0.30.6`（standard extras）

---

## Render / Railway デプロイ注意点

- `runtime.txt` に Python バージョンを記載済み（`python-3.12.8`）
- Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- 環境変数 `DATABASE_URL` を Render ダッシュボードで設定すること
- `/api/health` エンドポイントをヘルスチェック URL として設定推奨

---

## AXIA 確認済み項目

| 項目 | 状態 |
|------|------|
| GitHub repository 接続 | ✅ verified |
| Workspace read / write | ✅ verified |
| Diff 生成 | ✅ verified |
| Backup / restore | ✅ verified |
| FastAPI entrypoint | ✅ `app/main.py` |
| `/api/health` エンドポイント | ✅ 実装済み |
| `/api/health/db` エンドポイント | ✅ 実装済み |
| Start command | ✅ `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
| AXIA 確認日 | 2026-05-10 |
