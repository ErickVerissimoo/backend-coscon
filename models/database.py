from flask import Flask
from flask_sqlalchemy import SQLAlchemy
    

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://estudante1@localhost:3306/coscon'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.drop_all()
        db.create_all()  

    return app