from imports.main import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='comments')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    publication = db.relationship('Publication', backref=db.backref('comments', cascade='all, delete-orphan'))
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    
    
    