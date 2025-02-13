
from marshmallow import Schema, fields
import enum
from marshmallow.validate import ValidationError
from models.user import User
from flask_smorest.fields import Upload


class CommentJson(Schema):
    content = fields.Str()
    
