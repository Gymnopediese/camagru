from services.app import app
from services.jwt import *
from flask_smorest import Api, Blueprint
from flask import request


class APIConfig:
    API_TITLE = "API for the backend"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_UI_URL = "https://cdn.jsdelivr.net/npm/redoc/bundles/"
    #     # Swagger security definition for JWT
    # # Add Security Definitions
    # OPENAPI_SECURITY_SCHEMES = {
    #     "BearerAuth": {
    #         "type": "http",
    #         "scheme": "bearer",
    #         "bearerFormat": "JWT"
    #     }
    # }
    
    # # Apply security globally
    # OPENAPI_SECURITY = [{"BearerAuth": []}]



app.config.from_object(APIConfig)

api_object = Api(app)



api_object.spec.components.security_scheme(
    "BearerAuth",
    {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    },
)

@app.before_request
def rewrite_me_routes():
    """Intercept requests and rewrite '/me/...' to '/<current_user_id>/...'"""
    if request.path.startswith("/me/"):
        current_user_id = get_jwt_identity()["id"]
        new_path = request.path.replace("/me/", f"/users/{current_user_id}/", 1)
        request.environ["PATH_INFO"] = new_path  # Modify the request path

    
    


users = Blueprint("users", "users", url_prefix="/api/users", description="Users for the backend",)
auth = Blueprint("auth", "auth", url_prefix="/api/auth", description="Authentification for the backend",)
images = Blueprint("images", "images", url_prefix="/api/images", description="Authentification for the backend",)

publications = Blueprint("publications", "publications", url_prefix="/api/publications", description="Publications for the backend",)

comments = Blueprint("comments", "comments", url_prefix="/<int:publication_id>/comments", description="Comments for the backend",)
