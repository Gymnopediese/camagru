from imports.database import *

@app.route('/api/comments/<int:publication_id>', methods=['POST'])
@jwt_required()
def post_comment(publication_id):
    """
    Comment a publication.
    ---
    parameters:
    
    
    
        -   name: publication_id
            in: path
            required: true
            type: integer
        -   name: content
            in: body
            required: true
            type: string
    """
    user = get_jwt_identity()
    
    comment = Comment(
        publication_id=publication_id,
        user_id=user["id"],
        content=request.json["content"],
    )
    
    
    db.session.add(comment)
    db.session.commit()
    
    
    publication = Publication.query.get(publication_id).user_id
    
    
    if not publication.user.recieve_notifications:
        return jsonify(comment.serialize())
    
    msg = Message(
        subject="New comment",
        sender=app.config["MAIL_USERNAME"],
        recipients=[publication.user.email],
        body=f"{user['username']} commented on your publication !") 
    
    mail.send(msg)
    
    return jsonify(comment.serialize())

    
    