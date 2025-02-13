
from marshmallow import Schema, fields
import enum


class UpdateUser(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email(required=True)
    recieve_notifications = fields.Bool()
    
class UserResponse(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    recieve_notifications = fields.Bool()

class UserListResponse(Schema):
    users = fields.List(fields.Nested(UserResponse))
    


class OrderByEnum(enum.Enum):
    username = "username"
    email = "email"

class OrderEnum(enum.Enum):
    asc = "asc"
    desc = "desc"

class UserListQuery(Schema):
    order_by = fields.Enum(OrderByEnum)
    order = fields.Enum(OrderEnum)
    start = fields.Int()
    limit = fields.Int()
