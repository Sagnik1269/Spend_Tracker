from models.db import db
import uuid


class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True, default=lambda: uuid.uuid4().hex)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    transactions = db.relationship("Transaction", backref="account", lazy=True)