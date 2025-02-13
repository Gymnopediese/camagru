from imports.main import *
from imports.database import *

@comments.route('/', methods=['POST'])
@comments.arguments(CommentJson)
@jwt_required()
def post_comment(args, publication_id):
    """
    Comment a publication.
    """
    user = get_jwt_identity()
    
    comment = Comment(
        publication_id=publication_id,
        user_id=user["id"],
        content=args["content"],
    )
    
    
    db.session.add(comment)
    db.session.commit()
    
    
    publication = Publication.query.get(publication_id)
    
    
    if not publication.user.recieve_notifications:
        return jsonify(comment.serialize())
    
    msg = Message(
        subject="New comment",
        sender=app.config["MAIL_USERNAME"],
        recipients=[publication.user.email],
        body=f"{user['username']} commented on your publication !") 
    
    mail.send(msg)
    
    return jsonify(comment.serialize())

    
    