from imports.database import *

@app.route('/api/publications', methods=['POST'])
@jwt_required()
def post_publication():
    """
    Upload a publication. 
    ---
    parameters:
        - name: title
            in: body
            required: true
            type: string
        - name: content
            in: body    
            required: true
            type: string
            
    """
    user = get_jwt_identity()
    
    # TODO: ADD IMAGE LOGIC
    
    publication = Publication(
        title=request.json["title"],
        content=request.json["content"],
        user_id=user["id"],
        url="",
    )
    db.session.add(publication)
    db.session.commit()

    return jsonify(publication.serialize())