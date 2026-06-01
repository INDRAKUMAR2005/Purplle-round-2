import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["store_id"] == "ST1008"

def test_metrics_endpoint():
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    
    # Verify primary structures
    assert "store_summary" in data
    assert "salesperson_performance" in data
    assert "traffic_by_hour" in data
    
    # Verify store summary values
    summary = data["store_summary"]
    assert summary["store_id"] == "ST1008"
    assert summary["total_visitors"] > 0
    assert summary["non_staff_visitors"] > 0
    assert summary["total_transactions"] == 24 # 24 unique transactions in our CSV
    assert summary["overall_conversion_rate"] > 0
    
    # Verify salesperson contributions
    sp = data["salesperson_performance"]
    assert len(sp) > 0
    assert sp[0]["salesperson_name"] == "Zufishan Khazra" # Top salesperson by transactions in our CSV

def test_funnel_endpoint():
    response = client.get("/funnel")
    assert response.status_code == 200
    data = response.json()
    
    assert "stages" in data
    assert "overall_funnel_efficiency_percentage" in data
    
    stages = data["stages"]
    assert len(stages) == 4
    
    # Verify logical drop-off sizes
    s1 = stages[0]["unique_visitors"]
    s2 = stages[1]["unique_visitors"]
    s3 = stages[2]["unique_visitors"]
    s4 = stages[3]["unique_visitors"]
    
    assert s1 >= s2
    assert s2 >= s3
    assert s3 >= s4
    
    assert stages[3]["stage_name"] == "Purchases (Transactions)"

def test_anomalies_endpoint():
    response = client.get("/anomalies")
    assert response.status_code == 200
    data = response.json()
    
    assert "anomalies_count" in data
    assert "detected_anomalies" in data
    assert data["anomalies_count"] > 0
    
    # Verify specific anomalies list
    anom_types = [a["type"] for a in data["detected_anomalies"]]
    assert any("Staff" in t for t in anom_types)
    assert any("Re-entry" in t or "Customer" in t for t in anom_types)

def test_layout_endpoint():
    response = client.get("/layout")
    assert response.status_code == 200
    data = response.json()
    
    assert "layout_comparison" in data
    assert "shelf_efficiency_metrics" in data
    assert "layout_change_recommendations" in data
    
    # Verify layout lists
    comparison = data["layout_comparison"]
    assert "current_layout" in comparison
    assert "revised_layout" in comparison
    
    # Verify zone mappings
    metrics = data["shelf_efficiency_metrics"]
    assert len(metrics) > 0
    assert "brand" in metrics[0]
    assert "attention_conversion_index" in metrics[0]
