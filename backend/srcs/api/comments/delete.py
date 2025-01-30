from imports.database import *

@app.route('/api/comments/<int:comment_id>', methods=['POST'])
@jwt_required()
def delete_comment(comment_id):
    """
    Delete a comment. Only the sender of the comment and the owner of the publication can delete it.
    ---
    parameters:
        -   name: comment_id
            in: path
            required: true
            type: integer
    """
    
    user = get_jwt_identity()
    
    comment = Comment.query.get(comment_id)
    
    if not comment:
        return jsonify(error="Comment not found"), 404
    
    if comment.user_id != user["id"] and comment.publication.user_id != user["id"]:
        return jsonify(error="Unauthorized"), 401

    db.session.delete(comment)
    db.session.commit()
    
    return jsonify("Comment deleted")
   