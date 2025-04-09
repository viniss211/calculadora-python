from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_soma():
    response = client.get("/soma?a=5&b=3")
    assert response.status_code == 200
    assert response.json()["resultado"] == 8

def test_subtrai():
    response = client.get("/subtrai?a=9&b=4")
    assert response.status_code == 200
    assert response.json()["resultado"] == 5

def test_multiplica():
    response = client.get("/multiplica?a=3&b=3")
    assert response.status_code == 200
    assert response.json()["resultado"] == 9

def test_divide():
    response = client.get("/divide?a=10&b=2")
    assert response.status_code == 200
    assert response.json()["resultado"] == 5

def test_divide_por_zero():
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 200
    assert "erro" in response.json()

def test_decimal_soma():
    response = client.get("/soma?a=1.5&b=2.3")
    assert response.status_code == 200
    assert response.json()["resultado"] == 3.8

def test_decimal_multiplica():
    response = client.get("/multiplica?a=2.5&b=4")
    assert response.status_code == 200
    assert response.json()["resultado"] == 10.0

def test_negativo_subtrai():
    response = client.get("/subtrai?a=-5&b=-5")
    assert response.status_code == 200
    assert response.json()["resultado"] == 0

def test_zero_multiplica():
    response = client.get("/multiplica?a=0&b=5")
    assert response.status_code == 200
    assert response.json()["resultado"] == 0

def test_divide_float():
    response = client.get("/divide?a=5&b=2")
    assert response.status_code == 200
    assert response.json()["resultado"] == 2.5
