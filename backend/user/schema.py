import marshmallow
from marshmallow import fields


class UserSchema(marshmallow.Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    created_at = fields.DateTime(dump_only=True)


class CredentialsSchema(marshmallow.Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class TokenSchema(marshmallow.Schema):
    access_token = fields.Str()
