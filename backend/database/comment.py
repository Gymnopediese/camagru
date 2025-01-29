from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='comments')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post = db.relationship('Post', backref='comments')
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    
    
    