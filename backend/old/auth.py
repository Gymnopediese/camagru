# from app import app, db
# from database.user import User
# from flask import request, jsonify
# from flask_jwt_extended import create_access_token
# from flask import url_for
# from backend.services.mail import *
# from flask_mail import Message
# from flask import flash
# import time
# from hashlib import sha256
# # @app.route('/api/auth', methods=['GET'])
# # def admin_auth():
# #     username = request.args.get('username')
# #     access_token = create_access_token({
# #         "name": username
        
# #         })
# #     return jsonify(token=access_token)


# # users_waiting = []

# # @app.route('/api/auth', methods=['POST'])
# # def auth():
# #     """
# #     Authenticate a user.
# #     ---
    
# #     parameters:
# #         - name: name
# #           in: body
# #           required: true
# #           schema:
# #             type: object
# #             properties:
# #                 name:
# #                     type: string
# #                 email:
# #                     type: string
                
    
# #     responses:
# #         200:
# #             description: A JWT token.
# #         400:
# #             description: Invalid credentials.
# #     """
    
# #     name = request.json["name"]
# #     email = request.json["email"]
# #     password = sha256()
    
# #     token = generate_confirmation_token(email)
# #     verify_token = url_for('confirm_email', token=token, _external=True)
# #     content = f"Click the link to verify your email: {verify_token}"
# #     subject = "Verify your email"
    
# #     msg = Message(
# #         subject=subject,
# #         sender=app.config["MAIL_USERNAME"],
# #         recipients=[email],
# #         body=content) 
    
# #     mail.send(msg)
# #     flash("Check your email for a verification link")
    
    
    
# #     users_waiting.append({
# #         "name": name,
# #         "email": email,
# #         "created_at": time.time(),
# #     })
    
    
# #     return jsonify(token="salut")

# # @app.route('/api/confirm_email/<token>', methods=['GET'])
# # def confirm_email(token):
# #     """
# #     Confirm an email.
# #     ---
    
# #     """
    
# #     email = confirm_token(token)
    
# #     if not email:
# #         return jsonify(error="Invalid token"), 400
    
# #     user = next((u for u in users_waiting if u["email"] == email), None)
    
# #     if not user:
# #         return jsonify(error="User not found"), 404
    
# #     users_waiting.remove(user)
    
# #     access_token = create_access_token({
# #         "name": user["name"]
# #     })
# #     user = User(
# #         username=user["name"],
# #         mail=email,
# #         password="",
# #         recieve_notifications=False)
# #     db.session.add(user)
# #     db.session.commit()
# #     return "Done"


# @app.route('/api/request_change_password', methods=['POST'])
# def request_change_password():
#     """
#     Change a user's password.
#     ---
    
#     parameters:
#         - name: email
#           in: body
#           required: true
#           schema:
#             type: object
#             properties:
#                 email:
#                     type: string
#                 password:
#                     type: string
#     """

#     email = request.json["email"]
#     token = generate_confirmation_token(email)
#     verify_token = os.getenv("FRONTEND_URL") + "change_password?token=" + token
#     content = f"Click the link to change: {verify_token}"
#     subject = "Verify your email"
    
#     msg = Message(
#         subject=subject,
#         sender=app.config["MAIL_USERNAME"],
#         recipients=[email],
#         body=content) 
    
#     mail.send(msg)
#     flash("Check your email for a verification link")
    
#     return "Done"

# @app.route('/api/change_password/<token>', methods=['POST'])
# def change_password(token):
#     """
#     Change a user's password.
#     ---
    
#     parameters:
#         - name: password
#           in: body
#           required: true
#           schema:
#             type: object
#             properties:
#                 password:
#                     type: string
#     """
#     email = confirm_token(token)
    
#     if not email:
#         return jsonify(error="Invalid token"), 400
    
#     user = User.query.filter_by(mail=email).first()
    
#     if not user:
#         return jsonify(error="User not found"), 404
    
#     user.password = request.json["password"]
#     db.session.commit()
    
#     return "Done"