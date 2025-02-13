# from flask import Blueprint, request, jsonify, abort
# from flask.views import MethodView
# from database.user import User
# from app import db, app
# from flask_jwt_extended import jwt_required
# from flask import jsonify

# # from utils import role_required

# users_blueprint = Blueprint('user', __name__)

# class UserAPI(MethodView):
    
#     @jwt_required()
#     def get(self, id=None):
#         """Retrieve a single user or a list of users."""
#         if id is None:
#             dishes = User.query.all()
#             return jsonify([dish.serialize() for dish in dishes])
#         user = User.query.get(id)
#         if user:
#             return jsonify({"id": user.id, "name": user.name, "email": user.email})
#         return abort(404, "User not found")

#     def post(self):
#         """Create a new user."""
#         data = request.json
#         if not data or not data.get('name') or not data.get('email'):
#             return abort(400, "Name and email are required")
#         new_user = User(name=data['name'], email=data['email'])
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify({"message": "User created", "id": new_user.id}), 201

#     @jwt_required()
#     def put(self, id):
#         """Update an existing user."""
#         user = User.query.get(id)
#         if not user:
#             return abort(404, "User not found")
#         data = request.json
#         user.name = data.get('name', user.name)
#         user.email = data.get('email', user.email)
#         db.session.commit()
#         return jsonify({"message": "User updated", "id": user.id})

#     @jwt_required()
#     def delete(self, id):
#         """Delete a user."""
#         user = User.query.get(id)
#         if not user:
#             return abort(404, "User not found")
#         db.session.delete(user)
#         db.session.commit()
#         return jsonify({"message": "User deleted", "id": user.id})

# # Register the class-based view
# user_view = UserAPI.as_view('user_api')
# users_blueprint.add_url_rule('/api/users', defaults={'id': None}, view_func=user_view, methods=['GET'])
# users_blueprint.add_url_rule('/api/users', view_func=user_view, methods=['POST'])
# users_blueprint.add_url_rule('/api/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

# app.register_blueprint(users_blueprint)