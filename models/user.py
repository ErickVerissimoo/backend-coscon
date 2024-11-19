from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://erick:erick@localhost:3306/banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email= db.Column(db.String(100), nullable=False, unique= True)
    password = db.Column(db.String(50), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()  
    app.run(debug=True)