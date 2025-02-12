from marshmallow import Schema, fields


class CreateUser(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email(required=True)
    recieve_notifications = fields.Bool()


class LoginUser(Schema):
    credential = fields.Str(required=True)
    password = fields.Str(required=True)

    
class PasswordForgoten(Schema):
    email = fields.Str(required=True)

class ChangePassword(Schema):
    password = fields.Str(required=True)
    
class LoginResponse(Schema):
    token = fields.Str()
