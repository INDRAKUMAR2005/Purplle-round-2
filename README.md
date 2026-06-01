# Store Intelligence & Retail Analytics Console (Purplle Round 2)

An end-to-end computer vision and business intelligence platform built for Store `ST1008` (Brigade Road, Bangalore). The system processes multi-camera CCTV footage, logs customer tracks, filters staff traffic, detects operational anomalies, and computes layout attention-to-revenue conversion indices.

Exposes a FastAPI REST gateway and a creative Red & White Store Console Dashboard running seamlessly in a single command.

---

## 🚀 Key Features

* **Visual Customer Tracking**: Uses an optimized **OpenCV HOG + SVM person detector** and a custom **Centroid Tracker** operating at **1 FPS** on video downsamples to track visitor paths.
* **Cohesive Shopping Funnel**: Implements a session-based conversion funnel (`Entrance -> Brand Shelf Dwellers -> Checkout -> Paid Purchases`) matching unique customer tokens with zero double-counting.
* **Store Layout Optimization (ACI)**: Formulates the **Attention Conversion Index** ($\text{Sales NMV} / \text{Dwell Time}$) to compare shelf revenue-to-attention ratios for **Current** vs. **Revised** floor configurations.
* **Rules-Based Anomaly Feed**: Automatically flags re-entries ($<30$s delay), cart abandonments (completed checkouts without purchases), staff lingering, and joint group entries.
* **Salesperson Leaderboard**: Dynamic ranking of sales representatives by total net merchandise value (NMV), quantity of items sold, and basket values.
* **Vibrant Red & White Dashboard**: Served natively at `/dashboard` in a premium creative layout matching the brand.

---

## 🛠️ Tech Stack

* **Backend API Gateway**: FastAPI, Uvicorn, Pydantic
* **Computer Vision Tracking**: OpenCV (Headless MOG2 + HOG + Centroid Tracker)
* **Data Persistence**: SQLite (local schema tracking)
* **Visual Presentation**: HTML5, Vanilla CSS3 (Outfit & Inter fonts, Glassmorphism, Responsive Grid)
* **Deployment**: Docker, Docker Compose

---

## 📂 Project Directory Structure

```
├── main.py                 # FastAPI REST API Gateway & Dashboard router
├── pipeline.py             # CCTV Video Ingestion & Event Tracking Engine
├── db.py                   # SQLite Schema creation & Logging queries
├── test_app.py             # Automated Pytest Suite covering API schemas
├── requirements.txt        # Production python packages
├── Dockerfile              # Headless OpenCV optimized build
├── docker-compose.yml      # Orchestrates analytics service on port 8000
├── dashboard.html          # Breathtaking Red & White console interface
├── DESIGN.md               # Detailed system design & DB structure
├── CHOICES.md              # Architectural trade-off analysis
└── Brigade_Bangalore_10_April_26.csv # Relational transaction dataset
```

---

## 🚦 How to Deploy & Run

### A. Docker Compose Deployment (Recommended)
Launch the entire system (including the tracking database initialization and REST gateway) in a single command:
```bash
docker compose up --build
```
Once initialized:
* **Interactive Live Console**: Open **[http://localhost:8000/dashboard](http://localhost:8000/dashboard)** in your browser.
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
   pip install -r requirements.txt
   ```
3. **Execute Ingestion Pipeline**:
   ```bash
   python pipeline.py
   ```
4. **Boot REST API Web Server**:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

---

## 🧪 Running Automated Tests

Run the Pytest suite inside your virtual environment to verify the core analytics correctness, anomaly filters, and funnel logic:
```bash
pytest test_app.py
```
**Output**:
```
test_app.py .....                                                        [100%]
======================== 5 passed, 1 warning in 0.85s =========================
```

---

## 📊 API Endpoint Summary

| HTTP Verb | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/metrics` | Key store summary, salespersonLeaderboard, hourly traffic |
| `GET` | `/funnel` | Session-based visitor-to-buyer shopping conversion funnel |
| `GET` | `/anomalies` | Detected operational shop floor anomalies (Staff, Re-entry, Cart Abandonment) |
| `GET` | `/layout` | Current vs Revised shelf Attention-to-Revenue index comparison |
| `GET` | `/dashboard` | Interactive Red & White mixed creative dashboard visualizer |

---

## 👨‍💻 Author
**Indrakumar M**  
Built for the Purplle Store Intelligence Tech Challenge 2026.
