from models.database import db
from sqlalchemy.sql import func
from voluptuous import Schema, Invalid, Email, Length
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.String)
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
    comentarios = db.relationship('Comentario', backref='internauta', lazy=True)
class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(2000), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))


schema = Schema({
    'username': Length(min=3),
    'password': Length(min=9),
    'email': Email()
})
def authenticate(email, senha):
    usuario = User.query.filter_by(email=email, senha=senha).first()
    if usuario is not None:
        return True
    return False
def comentar(coment, idpost):
    
    comente = Comentario()
    comente.comment = coment
    comente.post_id = idpost

    
    db.session.add(comente)

def isValid(username, email, password):
    try:
        schema({'username': username, 'password': password, 'email': email})      
        return True
    except Invalid as inv:
        print(f'Dado inválido: {inv}')
        return False

def getFeed():
    return db.session.query(Post).all()


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