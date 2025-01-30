from app import app, db, socketio
# from routes.__imports__ import *
# from tests.database import fake_db
import os
from mail import *
from tests.fake_db import fake_db
from __import__ import *

os.environ['PYTHONUNBUFFERED'] = "1"


from flask_swagger import swagger

@app.route("/spec")
def spec():
    """
    Swagger API definition.
    ---
    responses:
        200:
            description: Swagger API definition.
    """
    
    info =  {
        'title': 'Kality of Life API',
        'uiversion': 3,
        'version': '1.0',
        'description': 'API for Kality of Life',
        'termsOfService': 'https://kalityoflife.com/terms',
        'contact': {
            'name': 'Kality of Life',
            'url': 'https://kalityoflife.com',
            'email': 'kalityoflife@gmail.com',
        },
        'license': {
            'name': 'MIT',
            'url': 'https://opensource.org/licenses/MIT',
        },
        'schemes': [
            'http',
            'https',
        ],
        'securityDefinitions': {
            'Bearer': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header',
            },
        },
        'security': [
            {
                'Bearer': [],
            },
        ],
    } 
    swag = swagger(app, template=info)
    
    return jsonify(swag)

if __name__ == '__main__':
    
    # if os.getenv("TEST") == "True":
    # with app.app_context():
    #     db.drop_all()
    #     # db.session.execute("DROP SCHEMA public CASCADE;")
    #     # db.session.execute("CREATE SCHEMA public;")
    #     # db.session.commit()
    #     db.create_all()
    #     fake_db()
    
    app.run(debug=True, host="0.0.0.0")
    