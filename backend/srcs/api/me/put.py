from imports.database import *

@app.route("/api/me", methods=["PUT"])
@jwt_required()
def me_put():
    """
    Update the current user
    ---
    parameters:
        -   name: name
            in: body
            required: false
            type: string
            
        -   name: email
            in: body
            required: false
            type: string
            
        -   name: password
            in: body
            required: false
            type: string

        -   name: recieve_notifications
            in: body
            required: false
            type: boolean
    """
    current_user = get_jwt_identity()
    user = User.query.get(current_user["id"])
    if not user:
        return abort(404, "User not found")
    data = request.json
    user.username = data.get('name', user.username)
    user.email = data.get('email', user.email)
    if "password" in data:
        user.password = sha256(data["password"].encode()).hexdigest()
    user.recieve_notifications = data.get('recieve_notifications', user.recieve_notifications)
    db.session.commit()
    return jsonify({"message": "User updated", "id": user.id})