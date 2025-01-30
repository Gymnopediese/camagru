from imports.database import *

@app.route("/api/me", methods=["DELETE"])
@jwt_required()
def me_delete(self):
    """
    Delete the current user
    ---
    responses:
        200:
            description: User deleted
        404:
            description: User not found
    """

    current_user = get_jwt_identity()
    user = User.query.get(current_user["id"])
    if not user:
        return abort(404, "User not found")
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted", "id": user.id})