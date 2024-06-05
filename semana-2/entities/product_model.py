from extensions import db
from datetime import datetime, timezone


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=True)
    stock = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
