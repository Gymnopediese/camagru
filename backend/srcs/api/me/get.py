from imports.database import *

@app.route("/api/me", methods=["GET"])
@jwt_required()
def me_get():
    """
    Retrieve me
    ---
    responses:
        200:
            description: A user object.
        404:
            description: User not found.
    """
    current_user = get_jwt_identity()
    user = User.query.get(current_user["id"])
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
    return abort(404, "User not found")