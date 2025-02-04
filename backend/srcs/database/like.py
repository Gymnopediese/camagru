from imports.main import db

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='likes')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    publication = db.relationship('Publication',  backref=db.backref('likes', cascade='all, delete-orphan'))
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'), nullable=False)
    
    dislike = db.Column(db.Boolean, nullable=False)
    
    
    