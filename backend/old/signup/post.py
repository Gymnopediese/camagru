from imports.database import *

waiting_users = []

@app.route("/api/users/signup", methods=["POST"])
def sign_up(self):
    """
    Try to create a new user. The user is added to a waiting list and an email is sent to them.
    ---
    parameters:
        -   name: name
            in: body
            required: true
            type: string
        -   name: email
            in: body
            required: true
            type: string
        -   name: password
            in: body
            required: true
            type: string
        -   name: recieve_notifications
            in: body
            required: true
            type: boolean
    """
    username = request.json["username"]
    email = request.json["email"]
    password = sha256(request.json["password"].encode()).hexdigest()
    recieve_notifications = request.json["recieve_notifications"]

    token = generate_confirmation_token(email)
    verify_token = os.getenv("FRONTEND_URL") + "verify?token=" + token
    content = f"Click the link to verify your email: {verify_token}"
    subject = "Verify your email"

    msg = Message(
        subject=subject,
        sender=app.config["MAIL_USERNAME"],
        recipients=[email],
        body=content)

    mail.send(msg)
    # flash("Check your email for a verification link")

    self.waiting_users.append({
        "username": username,
        "email": email,
        "password": password,
        "recieve_notifications": recieve_notifications,
        "created_at": time.time(),
    })
    return "Done"

@app.route("/api/users/signup/<token>", methods=["POST"])
def verify_email(token):
    """
    Verify a user's email.
    ---
    parameters:
        -   name: token
            in: path
            required: true
            type: string
    """
    email = confirm_token(token)
    if not email:
        return abort(400, "Invalid token")

    user = next((u for u in waiting_users if u["email"] == email), None)
    if not user:
        return abort(404, "User not found")

    waiting_users.remove(user)

    if time.time() - user["created_at"] > 60 * 15:
        return abort(400, "Token expired")

    user = User(
        username=user["username"],
        email=email,
        password=user["password"],
        recieve_notifications=user["recieve_notifications"])

    db.session.add(user)
    db.session.commit()
    return jsonify(token=create_token(user))
