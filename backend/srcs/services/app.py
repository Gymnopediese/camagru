from flask import Flask, jsonify, request, abort
import sys
import os
from flask import Flask
from flask_cors import CORS
from flask import Flask
from flask import jsonify



app = Flask(__name__)
CORS(app)

app.debug = True
app.config["SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True



@app.errorhandler(500)
def internal_server_error(e):
    print(e, file=sys.stderr)
    # note that we set the 500 status explicitly
    return "ok", 500

app.register_error_handler(500, internal_server_error)
app.register_error_handler(400, internal_server_error)

import traceback
@app.errorhandler(Exception)
def server_error(err: Exception):
    print(traceback.format_exc(), file=sys.stderr)
    print(err)

    if len(err.args)  == 0:
        return jsonify({"stderr": str(err)}), 500

    if len(err.args) and not type(err.args[0]) is dict:
        return jsonify({"stderr": str(err)}), 500
    app.logger.exception(err.args[0])
    return jsonify(err.args[0]), 500

# emit('connect', {'data': 'Connected'})