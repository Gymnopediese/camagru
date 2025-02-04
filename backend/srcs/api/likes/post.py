from imports.database import *

@app.route('/api/likes/<int:publication_id>', methods=['POST'])
@jwt_required()
def post_like(publication_id):
    """
    Like, unlike or dilike a publication. mode = 1 , 0 or -1 respectively.
    ---
    parameters:
        -   name: publication_id
            in: path
            required: true
            type: integer
        -   name: mode
            in: body
            required: true
            type: integer

    """
    user = get_jwt_identity()
    
    like = Like.query.filter_by(publication_id=publication_id, user_id=user["id"]).first()
    
    mode = request.json.get("mode")
    
    if mode == 0 and like:
        db.session.delete(like)
        db.session.commit()
        return jsonify("Like removed")
    
    if mode == 0 and not like:
        return jsonify("Like not found"), 404
    
    if not like:
        like = Like(
            publication_id=request.json["publication_id"],
            user_id=user["id"],
            dislike=mode,
        )
    else:
        like.dislike = mode
         
        
    db.session.add(like)
    db.session.commit()

    return jsonify(like.serialize())