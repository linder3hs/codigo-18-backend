from extensions import db
from datetime import datetime, timezone
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phoneNumber = db.Column(db.String(20), nullable=True)
    genre = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    # PARA PODEMOS MOSTRAR LA INFORMACION DE LA TABLA USER EN LA RESPUESTA DE
    # MI API, DEBEMOS PARSEAR ESTA INFORMACIÓN
    # to_dict => Conviertirlo a un diccionario de datos (objeto)
    def to_dic(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'password': self.password,
            'phoneNumber': self.phoneNumber,
            'genre': self.genre
        }
