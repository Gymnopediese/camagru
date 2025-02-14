from imports.main import *

from pathlib import Path


@images.route('/stickers', methods=['GET'])
@images.doc(description="Get all stickers")
@jwt_required()
def get_stickers():
    stickers = Path("images/stickers").rglob("*.png")
    return jsonify({"stickers": stickers})