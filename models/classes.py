from models.database import db
from sqlalchemy.sql import func
from voluptuous import Schema, Invalid, Email, Length
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email= db.Column(db.String(100), nullable=False, unique= True)
    password = db.Column(db.String(50), nullable=False)
    posts = db.relationship('Post', backref='autor', lazy=True) 
    
class Post(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=func.now())
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))

schema = Schema({
    'username': Length(min=3),
    'password': Length(min=9),
    'email': Email()
})
def isValid(username, email, password):
    try:
        schema({'username': username, 'password': password, 'email': email})      
        return True
    except Invalid as inv:
        print(f'Dado inválido: {inv}')
        return False
    
def addUser(username, email, password):
    if isValid(username, email, password):
        usuario = User()
        usuario.email=email
        usuario.password=password
        usuario.username=username
        db.session.add(usuario)
        db.session.commit()
    else:
        raise ValueError('Dados inválidos')