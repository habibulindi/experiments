# src/main.py
from flask import Flask, jsonify, Response
from prometheus_client import (
    Counter,
    Histogram,
    Gauge,
    generate_latest,
    CONTENT_TYPE_LATEST,
)
import time
import random
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# === МЕТРИКИ PROMETHEUS ===
# Counter: общее количество запросов
http_requests_total = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status'],
)

# Histogram: время ответа
http_request_duration_seconds = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['endpoint'],
    buckets=(0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0),
)

# Gauge: активные запросы
active_requests = Gauge(
    'active_requests',
    'Number of active HTTP requests',
)

# Бизнес-метрика: количество обработанных пользователей
users_processed_total = Counter(
    'users_processed_total',
    'Total users processed',
    ['source'],
)


# === Эндпоинт для Prometheus ===
@app.route('/metrics')
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST,
    )


# === Health check ===
@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200


# === Пример бизнес-эндпоинта ===
@app.route('/api/users', methods=['GET'])
def get_users():
    start_time = time.time()
    active_requests.inc()

    try:
        # Симуляция бизнес-логики
        time.sleep(random.uniform(0.01, 0.1))

        http_requests_total.labels(
            method='GET',
            endpoint='/api/users',
            status='200',
        ).inc()
        users_processed_total.labels(source='api').inc()

        logging.info('Successfully fetched users')
        return jsonify({
            'users': ['user1', 'user2'],
            'timestamp': time.time(),
        }), 200

    except Exception as e:
        http_requests_total.labels(
            method='GET',
            endpoint='/api/users',
            status='500',
        ).inc()
        logging.error('Error fetching users: %s', e)
        return jsonify({'error': str(e)}), 500

    finally:
        duration = time.time() - start_time
        http_request_duration_seconds.labels(
            endpoint='/api/users',
        ).observe(duration)
        active_requests.dec()


# === Эндпоинт для симуляции ошибок ===
@app.route('/api/fail', methods=['POST'])
def simulate_failure():
    http_requests_total.labels(
        method='POST',
        endpoint='/api/fail',
        status='500',
    ).inc()
    return jsonify({'error': 'Simulated failure'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
