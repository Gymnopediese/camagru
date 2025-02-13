from services.app import app
import os
from functools import wraps

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
if os.getenv("FLASK_ENV") == "development":
    def jwt_required():
        def wrapper(fn):
            @wraps(fn)
            def decorator(*args, **kwargs):
                return fn(*args, **kwargs)
            return decorator
        return wrapper
    def get_jwt_identity():
        return {"username": "me", "id": 1}
else:
    from flask_jwt_extended import get_jwt_identity
    from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

from datetime import datetime, timedelta, timezone

import os


app.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(days=13))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response

def create_token(user):
    return create_access_token({
        "name": user.username,
        "id": user.id,
        "email": user.mail
    })
