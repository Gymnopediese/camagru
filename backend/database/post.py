from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    user = db.relationship('User', backref='posts')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    # likes = db.relationship('Like', backref='post')
    # comments = db.relationship('Comment', backref='post')
    
    