# 🏪 Store Intelligence & Retail Analytics Console (Purplle Round 2)

An end-to-end computer vision and business intelligence platform built for Store `ST1008` (Brigade Road, Bangalore). The system processes multi-camera CCTV footage, logs customer tracks, filters staff traffic, detects operational anomalies, and computes layout attention-to-revenue conversion indices.

Exposes a FastAPI REST gateway and a premium interactive Red & White Store Console Dashboard supporting Light & Dark modes running seamlessly in a single command.

---

## 🌐 Project Submission Details

* **Title**: Store Intelligence & Retail Analytics Console: End-to-End Computer Vision & Business Intelligence Pipeline
* **Theme**: Retail Technology / Computer Vision & AI Analytics
* **Live Demo Link**: [https://purplle-round-2.vercel.app/dashboard](https://purplle-round-2.vercel.app/dashboard)
* **Repository URL**: [https://github.com/INDRAKUMAR2005/Purplle-round-2](https://github.com/INDRAKUMAR2005/Purplle-round-2)

### 📈 API Endpoints Directory (Production)
| Endpoint | Description | Live Link |
| :--- | :--- | :--- |
| **API Root** | API gateway landing page and directory | [/](https://purplle-round-2.vercel.app/) |
| **Health Check** | Production DB and CSV connection health | [/health](https://purplle-round-2.vercel.app/health) |
| **Store Metrics** | Store conversion rate, leaderboards, and traffic charts | [/metrics](https://purplle-round-2.vercel.app/metrics) (or [/Metrics](https://purplle-round-2.vercel.app/Metrics)) |
| **Conversion Funnel** | Unique session-based visitor-to-buyer funnel | [/funnel](https://purplle-round-2.vercel.app/funnel) |
| **Anomaly Feed** | Operational alerts (Staff filter, re-entries, abandonments) | [/anomalies](https://purplle-round-2.vercel.app/anomalies) |
| **Layout Analytics** | Current vs Revised shelf Attention Conversion Index | [/layout](https://purplle-round-2.vercel.app/layout) |
| **Interactive Console** | Branded Light/Dark mode visual control center | [/dashboard](https://purplle-round-2.vercel.app/dashboard) |
| **Swagger Docs** | Live interactive API test console | [/docs](https://purplle-round-2.vercel.app/docs) |

---

## 🚀 Key Features

* **Visual Customer Tracking**: Uses an optimized **OpenCV HOG + SVM person detector** and a custom **Centroid Tracker** operating at **1 FPS** on video downsamples to track visitor paths.
* **Cohesive Shopping Funnel**: Implements a session-based conversion funnel (`Entrance → Brand Shelf Dwellers → Checkout → Paid Purchases`) matching unique customer tokens with zero double-counting.
* **Store Layout Optimization (ACI)**: Formulates the **Attention Conversion Index** (Sales NMV / Dwell Time) to compare shelf revenue-to-attention ratios for **Current** vs. **Revised** floor configurations.
* **Rules-Based Anomaly Feed**: Automatically flags re-entries (<30s delay), cart abandonments (completed checkouts without purchases), staff lingering, and joint group entries.
* **Salesperson Leaderboard**: Dynamic ranking of sales representatives by total net merchandise value (NMV), quantity of items sold, and basket values.
* **Vibrant Red & White Dashboard**: Served natively at `/dashboard` in a premium creative layout matching the brand.
* **Production Health Check**: `/health` endpoint returns DB event counts, CSV availability, and overall system status.
* **Structured Logging**: All API requests and pipeline events emit structured timestamped logs.

---

## 🛠️ Tech Stack

* **Backend API Gateway**: FastAPI, Uvicorn, Pydantic
* **Computer Vision Tracking**: OpenCV (Headless MOG2 + HOG + Centroid Tracker) — Docker only
* **Data Persistence**: SQLite (local schema tracking) + in-memory `/tmp` for serverless
* **Visual Presentation**: HTML5, Vanilla CSS3 (Outfit & Inter fonts, Glassmorphism, Responsive Grid)
* **Deployment**: Docker + Docker Compose (local) / Vercel Serverless (cloud)

---

## 🚦 How to Deploy & Run (Instructions to Run)

### A. Docker Compose Deployment (Recommended — Full CV Ingestion)
Launch the entire system (including the tracking database initialization and REST gateway) in a single command:
```bash
docker compose up --build
```
Once initialized:
* **Interactive Live Console**: Open **[http://localhost:8000/dashboard](http://localhost:8000/dashboard)** in your browser.
* **Health Check**: Open **[http://localhost:8000/health](http://localhost:8000/health)**.
* **Swagger API Documentation**: Open **[http://localhost:8000/docs](http://localhost:8000/docs)**.

### B. Local Virtual Environment Setup
1. **Initialize Virtual Env**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
2. **Install Requirements**:
   ```bash
   pip install -r requirements-docker.txt
   ```
3. **Execute Ingestion Pipeline**:
   ```bash
   python pipeline.py
   ```
4. **Boot REST API Web Server**:
   ```bash
   python -m uvicorn main:app --host 127.0.0.1 --port 8000
   ```

---

## 🧪 Running Automated Tests

Run the Pytest suite inside your virtual environment to verify the core analytics correctness, anomaly filters, and funnel logic:
```bash
python -m pytest test_app.py -v
```
**Expected Output**:
```
test_app.py::test_read_root PASSED
test_app.py::test_metrics_endpoint PASSED
test_app.py::test_funnel_endpoint PASSED
test_app.py::test_anomalies_endpoint PASSED
test_app.py::test_layout_endpoint PASSED
test_app.py::test_tracing_middleware PASSED
test_app.py::test_staff_exclusion_logic PASSED
======================== 7 passed in 1.18s =========================
```

---

## 👨‍💻 Author
**Indrakumar M**  
Built for the Purplle Store Intelligence Tech Challenge 2026.
