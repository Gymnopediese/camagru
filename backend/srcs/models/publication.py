from imports.main import db


class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    user = db.relationship('User',  backref=db.backref('publications', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user": self.user.serialize(),
            "url": self.url,    
            "likes": len(self.likes),
            "comments": len(self.comments)
        }
    