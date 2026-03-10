import os
from flask import Flask, jsonify
from flask_cors import CORS

from config import Config
from routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    register_routes(app)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "Spend Tracker API is running"
        }), 200

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
