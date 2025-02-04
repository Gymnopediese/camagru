from imports.database import *

@app.route("/api/users/<int:id>", methods=["GET"])
@jwt_required()
def get(id):
    """
    Retrieve a single user
    ---
    parameters:
        -   name: id
            in: path
            required: true
            type: integer
    """
    user = User.query.get(id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
    return abort(404, "User not found")