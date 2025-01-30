# from flask import Blueprint, request, jsonify, abort
# from flask.views import MethodView
# from database.user import User
# from app import db, app
# from flask_jwt_extended import jwt_required, get_jwt_identity
# from flask import jsonify
# from flask_mail import Message
# from backend.services.mail import *
# from hashlib import sha256
# from app import generate_confirmation
# from flask import url_for
# from flask import flash
# import time
# from flask_jwt_extended import create_access_token

# # from utils import role_required

# users_blueprint = Blueprint('user', __name__)

# class UserAPI(MethodView):
    
#     waiting_users = []
    

   
        


#     def verify_account(self, token):
#         """
#         Confirm an email.
#         ---
        
#         """
#         email = confirm_token(token)
        
#         if not email:
#             return jsonify(error="Invalid token"), 400
        
#         user = next((u for u in self.waiting_users if u["email"] == email), None)
        
#         if not user:
#             return jsonify(error="User not found"), 404
        
#         self.waiting_users.remove(user)
        
#         access_token = create_access_token({
#             "name": user["name"],
#             "id": user["id"],
#             "mail": user["email"],
#         })
#         user = User(
#             username=user["name"],
#             mail=email,
#             password="",
#             recieve_notifications=False)
#         db.session.add(user)
#         db.session.commit()
#         return "Done"

#     def post(self, token):
#            """
#             Authenticate a user.
#             ---
            
#             parameters:
#                 - name: name
#                 in: body
#                 required: true
#                 schema:
#                     type: object
#                     properties:
#                         name:
#                             type: string
#                         email:
#                             type: string
                        
            
#             responses:
#                 200:
#                     description: A JWT token.
#                 400:
#                     description: Invalid credentials.
#             """
#             if not token:
#                 self.send_token()
            





# # Register the class-based view
# user_view = UserAPI.as_view('user_api')
# users_blueprint.add_url_rule('/api/users', defaults={'id': None}, view_func=user_view, methods=['GET'])

# users_blueprint.add_url_rule('/api/users', defaults={'token': None}, view_func=user_view, methods=['POST'])

# users_blueprint.add_url_rule('/api/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

# app.register_blueprint(users_blueprint)

# """
# /api/users -> send mail

# mail  ->   front  /new_acount/{token}

# front -> /api/users/{token} create user.

# """