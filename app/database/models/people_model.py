from app.core.database import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from app.core.marshmallow import ma
from random import randrange


class People(db.Model, SerializerMixin):
    __tablename__ = "people"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(
        db.String,
        nullable=False,
        default=datetime.utcnow().strftime("%Y-%m-%d - %H:%M:%S"),
        server_default=db.text("0"),
    )
    updated_at = db.Column(db.String, onupdate=datetime.utcnow().strftime("%Y-%m-%d - %H:%M:%S"), nullable=True)

    def __init__(self, name):
        self.name = name
        self.updated_at = datetime.utcnow().strftime("%Y-%m-%d - %H:%M:%S")
        self.updated_at = datetime.utcnow().strftime("%Y-%m-%d - %H:%M:%S")



class PeopleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "name", "created_at")
        model = People

    id = ma.auto_field()
    name = ma.auto_field()
    created_at = ma.auto_field()
