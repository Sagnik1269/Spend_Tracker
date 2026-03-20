import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from routes import register_routes
from models.db import db
from models.account import Account
from models.transaction import Transaction

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    register_routes(app)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "Spend Tracker API is running"
        }), 200
    
    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
