from .app import db


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    business = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(250), nullable=False)
