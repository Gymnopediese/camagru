from app import app
from flask import request, jsonify
from flask_jwt_extended import create_access_token



@app.route('/api/auth', methods=['GET'])
def admin_auth():
    username = request.args.get('username')
    access_token = create_access_token({
        "name": username
        
        })
    return jsonify(token=access_token)