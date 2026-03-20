from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import bcrypt

from models.db import db
from models.account import Account

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


def check_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    existing_user = Account.query.filter(
        (Account.username == username) | (Account.email == email)
    ).first()

    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    hashed_password = hash_password(password)

    new_user = Account(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = Account.query.filter_by(email=email).first()

    if not user or not check_password(password, user.password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)

    return jsonify({
        "access_token": access_token,
        "account_id": user.id
    }), 200