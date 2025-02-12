from flask.views import MethodView
from imports.main import *
from models.user import User

security = [{"BearerAuth": []}]
security = []

@users.route('/')
class UsersAPI(MethodView):
    @users.doc(description="Get all users", security=security) 
    @users.arguments(UserListQuery, location="query")
    @users.response(200, schema=UserListResponse)
    @jwt_required()
    def get(self, args):
        order_by = args.get("order_by", OrderByEnum.username)
        order = args.get("order", OrderEnum.asc)
        limit = args.get("limit")
        start = args.get("start", 0)
        order_by = {
            OrderByEnum.username: User.username,
            OrderByEnum.email: User.email,
            OrderByEnum.age: User.age,
        }[order_by]
        reverse = order == "desc"
        query = User.query.order_by(order_by)
        query = query.offset(start)
        if reverse:
            query = query.reverse()
        if limit is not None:
            query = query.limit(limit)
        users = query.all()
        return jsonify({"users": [user.serialize() for user in users]})

    # @users.doc(description="Create a User")
    # @users.arguments(CreateUser)
    # @users.response(201, schema=LoginResponse)
    # @jwt_required()
    # def post(self, args):
    #     user = User.new(**args)
    #     db.session.add(user)
    #     db.session.commit()
    #     return jsonify({"token": user.generate_token()})


@users.route('/<int:id>')
class UserAPI(MethodView):
    @users.doc(description="Get a user by ID")
    @users.response(200, schema=UserResponse)
    @jwt_required()
    def get(self, id):
        user = User.query.get(id)
        return jsonify(user.serialize())
    
    @users.doc(description="Update a user by ID")
    @users.arguments(UpdateUser)
    @users.response(200, schema=UserResponse)
    @jwt_required()
    def put(self, args, id):
        user = User.query.get(id)
        user.update(**args)
        db.session.commit()
        return jsonify(user.serialize())
    
    @users.doc(description="Delete a user by ID")
    @users.response(204)
    @jwt_required()
    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({})
    
    