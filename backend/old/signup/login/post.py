from imports.database import *

@app.route("/users/login", methods=["POST"])
def login():
    """
    Login
    ---
    parameters:
        -   name: username
            in: body
            required: true
            type: string
        -   name: password
            in: body
            required: true
            type: string

    """
    data = request.json
    username = data.get("username", None)
    password = data.get("password")

    print(username)
    user = User.query.filter_by(username=username).first()

    if not user:
        user = User.query.filter_by(mail=username).first()

    if not user:
        return abort(404, "User not found")


    if sha256(password.encode()).hexdigest() != user.password:
        return abort(401, "Invalid password")

    return jsonify(token=create_token(user))
