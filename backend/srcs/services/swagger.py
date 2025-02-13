from services.app import app
from flask_swagger import swagger

from flask import jsonify

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
