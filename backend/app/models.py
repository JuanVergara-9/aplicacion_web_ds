from datetime import datetime
from .extension import db
from flask_login import UserMixin
from datetime import datetime, timezone


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_mesa = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(64), nullable=False)

    def init(self, codigo_mesa, username):
        self.codigo_mes = codigo_mesa
        self.username = username


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_mesa = db.Column(db.Integer)
    status = db.Column(db.String(64), default='pending')
    timestamp = db.Column(db.DateTime, index=True, default=lambda: datetime.now(timezone.utc))
    items = db.relationship('OrderItem', backref='order', lazy='dynamic')

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, default=1)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    price = db.Column(db.Float)
    stock = db.Column(db.Integer, default=0)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128))
    amount = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=lambda: datetime.now(timezone.utc))
