from flask import Flask

app = Flask(__name__)

import src.routes.main  # регистрируем маршруты

if __name__ == "__main__":
    app.run(debug=False)
