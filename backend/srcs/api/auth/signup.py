from imports.database import *
from imports.main import *

from hashlib import sha256
waiting_users = []

@auth.route("/signup", methods=["POST"])
@auth.doc(description="Try to create a new user by sending a confirmation mail.")
@auth.arguments(CreateUser)
@auth.response(201, schema=LoginResponse)
def sign_up(arguments):
    """
    Try to create a new user by sending a confirmation mail.
    """

    username = arguments.get("username")
    email = arguments.get("email")
    password = sha256(arguments.get("password").encode()).hexdigest()
    recieve_notifications = arguments.get("recieve_notifications", True)

    token = generate_confirmation_token(email)
    verify_token = os.getenv("FRONTEND_URL") + "/verify?token=" + token
    content = f"Click the link to verify your email: {verify_token}"
    subject = "Verify your email"

    user_exist = User.query.filter_by(email=email).first()
    if user_exist:
        return abort(400, "Email already exists")

    user_exist = next((u for u in waiting_users if u["email"] == email), None)
    if user_exist:
        return abort(400, "Mail already sent")

    user_exist = User.query.filter_by(username=username).first()
    if user_exist:
        return abort(400, "Username already exists")

    msg = Message(
        subject=subject,
        sender=app.config["MAIL_USERNAME"],
        recipients=[email],
        body=content)

    mail.send(msg)
    # flash("Check your email for a verification link")
    
    waiting_users.append({
        "username": username,
        "email": email,
        "password": password,
        "recieve_notifications": recieve_notifications,
        "created_at": time.time(),
    })
    return "Done"

@auth.route("/signup/<token>", methods=["POST"])
@auth.doc(description="Confirm a user's email and create the user.")
@auth.response(201, schema=LoginResponse)
def verify_email(token):
    """
    Verify a user's email.
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
