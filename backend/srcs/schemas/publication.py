
from marshmallow import Schema, fields
import enum
from marshmallow.validate import ValidationError
from models.user import User
from flask_smorest.fields import Upload
# class Publication(Schema):
#     id = fields.Int()
#     title = fields.Str()
#     content = fields.Str()
#     date = fields.DateTime()
#     user_id = fields.Int()
#     user = fields.Nested('User')
    
class BytesField(fields.Field):
    def _validate(self, value):
        if not isinstance(value, bytes):
            raise ValidationError('Invalid input type.')

        if value is None or value == b'':
            raise ValidationError('Invalid value')
    
class CreatePublicationImage(Schema):
    image = Upload(required=True)

class CreatePublication(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    
    x = fields.Int(required=True)
    y = fields.Int(required=True)
    
    sticker = fields.Str(required=True)
    
class UpdatePublicationImage(Schema):
    image = Upload()
    
class UpdatePublication(Schema):
    title = fields.Str()
    description = fields.Str()



    
class PublicationResponse(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    url = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    
    user = fields.Nested("UserSchema")
    likes = fields.Int()
    comments = fields.Int()

class UserListResponse(Schema):
    publications = fields.List(fields.Nested(PublicationResponse))
    

class PublicationOrderByEnum(enum.Enum):
    created_at = "created_at"
    updated_at = "updated_at"
    title = "title"
    

class PublicationOrderEnum(enum.Enum):
    asc = "asc"
    desc = "desc"

class PublicationListQuery(Schema):
    
    order_by = fields.Enum(PublicationOrderByEnum)
    order = fields.Enum(PublicationOrderEnum)
    start = fields.Int()
    limit = fields.Int()
