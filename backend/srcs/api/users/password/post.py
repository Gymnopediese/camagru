from imports.database import *

@app.route('/api/users/password', methods=['POST'])
def request_change_password():
    """
    Change a user's password.
    ---
    
    parameters:
        -   name: email
            in: body
            required: true
            type: string

        -   name: password
            in: body
            required: true
            type: string
    """

    email = request.json["email"]
    token = generate_confirmation_token(email)
    verify_token = os.getenv("FRONTEND_URL") + "change_password?token=" + token
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

@app.route('/api/users/password/<token>', methods=['POST'])
def change_password(token):
    """
    Change a user's password.
    ---
    
    parameters:
        -   name: password
            in: body
            required: true
            type: string
    """
    email = confirm_token(token)
    
    if not email:
        return jsonify(error="Invalid token"), 400
    
    user = User.query.filter_by(mail=email).first()
    
    if not user:
        return jsonify(error="User not found"), 404
    
    user.password = sha256(request.json["password"].encode()).hexdigest()
    db.session.commit()
    
    return jsonify(token=create_token(user))