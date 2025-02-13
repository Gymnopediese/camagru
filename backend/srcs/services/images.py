
from imports.main import *
from flask import send_from_directory

@images.route('/<string:url>', methods=['GET'])
# @jwt_required()
def get_image(url):
    print(url, "not found")
    return send_from_directory('/app/images', url)