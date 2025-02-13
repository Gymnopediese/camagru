from imports.database import *
# from imports. import *
from imports.main import *
from imports.routes import *
from services.swagger import *
from services.images import *


api_object.register_blueprint(users)
api_object.register_blueprint(auth)
api_object.register_blueprint(images)
publications.register_blueprint(comments)
api_object.register_blueprint(publications)