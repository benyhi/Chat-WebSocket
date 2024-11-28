from app import db
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

    sender = db.relationship('Message', back_populates='sender_user', foreign_keys='Message.sender_id')
    receiver = db.relationship('Message', back_populates='receiver_user', foreign_keys='Message.receiver_id')

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    msg = db.Column(db.Text, nullable=False)

    sender_user = db.relationship('User', back_populates='sender', foreign_keys=[sender_id])
    receiver_user = db.relationship('User', back_populates='receiver', foreign_keys=[receiver_id])
