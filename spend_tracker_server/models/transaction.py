from datetime import datetime
from models.db import db
import uuid


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True, default=lambda: uuid.uuid4().hex)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)

    date = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)
    source = db.Column(db.String(20), nullable=True)
    category = db.Column(db.String(100), nullable=True)
    merchant_name = db.Column(db.String(150), nullable=True)
    is_recurring = db.Column(db.Boolean, default=False)
    notes = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)