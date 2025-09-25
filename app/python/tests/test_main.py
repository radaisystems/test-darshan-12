"""
Basic tests for test-darshan-12 Flask application
"""
import pytest
import json
from main import app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_endpoint(client):
    """Test the main hello endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'message' in data
    assert 'service' in data
    assert 'language' in data
    assert data['language'] == 'python'


def test_health_endpoint(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data


def test_ready_endpoint(client):
    """Test the readiness check endpoint."""
    response = client.get('/ready')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'ready'
    assert 'timestamp' in data


def test_info_endpoint(client):
    """Test the info endpoint."""
    response = client.get('/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'service' in data
    assert 'type' in data
    assert 'language' in data
    assert 'version' in data
