import sqlite3
import json
import os

DB_PATH = "store_analytics.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Create events table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        event_type TEXT NOT NULL,
        visitor_id INTEGER NOT NULL,
        details TEXT
    )
    """)
    conn.commit()
    conn.close()

def log_event(timestamp, event_type, visitor_id, details=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    details_str = json.dumps(details) if details is not None else None
    cursor.execute(
        "INSERT INTO events (timestamp, event_type, visitor_id, details) VALUES (?, ?, ?, ?)",
        (timestamp, event_type, visitor_id, details_str)
    )
    conn.commit()
    conn.close()

def get_events(event_type=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if event_type:
        cursor.execute("SELECT timestamp, event_type, visitor_id, details FROM events WHERE event_type = ? ORDER BY timestamp ASC", (event_type,))
    else:
        cursor.execute("SELECT timestamp, event_type, visitor_id, details FROM events ORDER BY timestamp ASC")
    rows = cursor.fetchall()
    conn.close()
    
    events = []
    for r in rows:
        events.append({
            "timestamp": r[0],
            "event_type": r[1],
            "visitor_id": r[2],
            "details": json.loads(r[3]) if r[3] else None
        })
    return events

def clear_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM events")
    conn.commit()
    conn.close()
