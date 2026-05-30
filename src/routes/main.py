from src.app import app


@app.route("/")
def home():
    return {"status": "ok"}
