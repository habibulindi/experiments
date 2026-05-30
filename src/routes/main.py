from src.app import app

@app.route("/")
def home():
    return {"status": "ok"}

def register_routes(app):
    @app.route("/")
    def home():
        return {"status": "ok"}
