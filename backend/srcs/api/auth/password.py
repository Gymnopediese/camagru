from imports.database import *
from hashlib import sha256

@auth.route("/password", methods=["POST"])
@auth.doc(description="Request a password change.")
@auth.arguments(PasswordForgoten)
@auth.response(201, schema=LoginResponse)
def request_change_password(arguments):
    """
    Request a password change when the user lost it.
    """
    

    email = arguments.get("email")
    
    token = generate_confirmation_token(email)
    verify_token = os.getenv("FRONTEND_URL") + "/change_password?token=" + token
    content = f"Click the link to change: {verify_token}"
    subject = "Verify your email"
    
    msg = Message(
        subject=subject,
        sender=app.config["MAIL_USERNAME"],
        recipients=[email],
        body=content) 
    
    mail.send(msg)
    # flash("Check your email for a verification link")
    
    return "Done"

@auth.route('/password/<string:token>', methods=['POST'])
@auth.doc(description="Change a user's password.")
@auth.arguments(ChangePassword)
@auth.response(201, schema=LoginResponse)
def change_password(arguments, token):
    """
    Change a user's password.
    """
    email = confirm_token(token)
    new_password = arguments.get("password")
    
    if not email:
        return jsonify(error="Invalid token"), 400
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify(error="User not found"), 404
    
    user.password = sha256(new_password.encode()).hexdigest()
    db.session.commit()
    
    return jsonify(token=create_token(user))
