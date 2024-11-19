from models.database import db
from sqlalchemy.sql import func
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email= db.Column(db.String(100), nullable=False, unique= True)
    password = db.Column(db.String(50), nullable=False)
    posts = db.relationship('post', backref='autor', lazy=True)
    
class post(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=func.now)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))