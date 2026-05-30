# src/app.py
from flask import Flask

app = Flask(__name__)

# Импортируем наверх
from src.routes.main import register_routes
register_routes(app)
