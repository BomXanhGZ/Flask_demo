from ..extensions import ma
from marshmallow import Schema, fields
from ..models.user import User


# local register Schema
class RegisterUserDTO(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)


# local login Schema
class LoginUserDTO(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


# user response Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ('password_hash',)


user_schema = UserSchema()
