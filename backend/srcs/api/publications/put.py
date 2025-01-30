from imports.database import *

@app.route('/api/publications', methods=['PUT'])
@jwt_required()
def put_publication():
    """
    Upload a publication.
    ---
    parameters:
        -   name: title
            in: body
            required: true
            type: string

        -   name: content
            in: body    
            required: true
            type: string
    """
    user = get_jwt_identity()
    
    publication_id = request.json.get("id")
    publication = Publication.query.get(publication_id)
    
    if not publication:
        return jsonify(error="Publication not found"), 404
    
    if publication.user_id != user["id"]:
        return jsonify(error="Unauthorized"), 401
    
    publication.title = request.get("title", publication.title)
    publication.content = request.get("content", publication.content)
    
    db.session.add(publication)
    db.session.commit()
    
    return jsonify(publication.serialize())
    
    
    