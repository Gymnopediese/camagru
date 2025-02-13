from imports.database import *

@app.route('/api/publications/<int:start>-<int:end>', methods=['GET'])
def get_publications(start, end):
    """
    Get publications.
    ---
    parameters:
        -   name: start
            in: path
            required: true
            type: integer

        -   name: end
            in: path
            required: true
            type: integer
    """
    publications = Publication.query.order_by(Publication.date.desc()).slice(start, end).all()
    return jsonify([publication.serialize() for publication in publications])

@app.route('/api/publications/<int:id>', methods=['GET'])
def get_publication(id):
    """
    Get a publication.
    ---
    parameters:
        -   name: id
            in: path
            required: true
            type: integer
    """
    publication = Publication.query.get(id)
    return jsonify(publication.serialize())