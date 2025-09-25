import os
from flask import Flask, jsonify
from datetime import datetime
import time

app = Flask(__name__)

# Configuration
PORT = int(os.environ.get('PORT', 3000))
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Application state
start_time = datetime.now()
request_count = 0

@app.before_request
def before_request():
    global request_count
    request_count += 1

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from test-darshan-12!',
        'service': 'web-service',
        'language': 'python',
        'python_version': '3.11',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat(),
        'uptime_seconds': int((datetime.now() - start_time).total_seconds()),
        'request_count': request_count
    })


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'uptime_seconds': int((datetime.now() - start_time).total_seconds()),
        'service': 'test-darshan-12'
    })

@app.route('/ready')
def ready():
    # Add any readiness checks here
    return jsonify({
        'status': 'ready',
        'timestamp': datetime.now().isoformat(),
        'service': 'test-darshan-12'
    })


@app.route('/info')
def info():
    return jsonify({
        'service': 'test-darshan-12',
        'type': 'web-service',
        'language': 'python',
        'python_version': '3.11',
        'version': '1.0.0',
        'start_time': start_time.isoformat(),
        'port': PORT
    })

if __name__ == '__main__':
    print(f"Starting test-darshan-12 on port {PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)

