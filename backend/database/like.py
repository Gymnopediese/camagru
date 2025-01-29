from app import db

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='likes')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    post = db.relationship('Post', backref='likes')
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    
    dislike = db.Column(db.Boolean, nullable=False)
    
    
    