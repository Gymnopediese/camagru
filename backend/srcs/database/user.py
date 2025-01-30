from imports.main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(100), nullable=False, unique=True)
    mail = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    recieve_notifications = db.Column(db.Boolean, nullable=True)
    
    
    