from imports.database import *

@app.route('/api/publications/<int:publication_id>', methods=['DELETE'])
@jwt_required()
def delete_publication(publication_id):
    """
    Delete a publication. Only the owner of the publication can delete it.
    ---
    parameters:
        -   name: publication_id
            in: path
            required: true
            type: integer
    """
    
    user = get_jwt_identity()
    
    publication = Publication.query.get(publication_id)
    
    if not publication:
        return jsonify(error="Publication not found"), 404
    
    if publication.user_id != user["id"]:
        return jsonify(error="Unauthorized"), 401

    db.session.delete(publication)
    db.session.commit()
    
    return jsonify("Publication deleted")