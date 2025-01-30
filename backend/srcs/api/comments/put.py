from imports.database import *

@app.route('/api/comments/<int:comment_id>', methods=['POST'])
@jwt_required()
def put_comment(comment_id):
    """
    Modify a comment.
    ---
    parameters:
        -   name: comment_id
            in: path
            required: true
            type: integer
        -   name: content
            in: body
            required: true
            type: string
    """
    
    user = get_jwt_identity()
    
    comment = Comment.query.get(comment_id)
    
    if not comment:
        return jsonify(error="Comment not found"), 404
    
    if comment.user_id != user["id"]:
        return jsonify(error="Unauthorized"), 401
    
    comment.content = request.json.get("content", comment.content)
    
    db.session.add(comment)
    db.session.commit()
    
    return jsonify(comment.serialize())
   