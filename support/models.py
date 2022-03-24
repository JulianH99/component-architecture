from sqlalchemy import Table, Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from .app import db


class Message(db.Model):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    business = Column(String(15), nullable=False)
    email = Column(String(50), nullable=False)
    message = Column(String(250), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
