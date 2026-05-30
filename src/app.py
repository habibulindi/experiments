from flask import Flask
from src.routes.main import register_routes   # импорт наверху

app = Flask(__name__)
register_routes(app)  # вызов после создания app

if __name__ == "__main__":
    app.run(debug=False)
