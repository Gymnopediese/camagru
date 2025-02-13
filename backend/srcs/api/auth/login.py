from flask.views import MethodView
from imports.main import *
from models.user import User


@auth.route('/login', methods=['POST'])
@auth.doc(description="Login to an existing account")
@auth.arguments(LoginUser)
@auth.response(201, schema=LoginResponse)
def login(params):
    """
    Login to an existing account.
    """
    credential = params.get("credential")
    password = params.get("password")

    user = User.query.filter_by(username=credential).first()
    if not user:
        user = User.query.filter_by(email=credential).first()
    if user and user.check_password(password):
        return jsonify({'token': user.generate_token()})
    abort(401, "Invalid username or password")


