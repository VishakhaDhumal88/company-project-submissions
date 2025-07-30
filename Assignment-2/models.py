# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numbers = db.Column(db.String, nullable=False, unique=True)
    result = db.Column(db.Float, nullable=False)

