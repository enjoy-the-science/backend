import typing

import flask
import flask_apispec
from flask_apispec import views

from . import models, schema


app = flask.Blueprint('users', __name__)


@flask_apispec.marshal_with(schema.UserSchema(many=True))
class Users(views.MethodResource):
    def get(self) -> typing.List[models.User]:
        return models.User.query.all()

    @flask_apispec.use_kwargs(schema.UserSchema)
    @flask_apispec.marshal_with(schema.UserSchema)
    def post(self, **kwargs: typing.Any) -> models.User:
        user = models.User.create_user(
            email=kwargs.pop('email'), password=kwargs.pop('password')
        )

        return user


@flask_apispec.use_kwargs(schema.CredentialsSchema)
@flask_apispec.marshal_with(schema.TokenSchema)
class Login(views.MethodResource):
    def post(self, **kwargs: typing.Any) -> typing.Dict[str, str]:
        access_token = models.User.get_token(
            email=kwargs.pop('email'), password=kwargs.pop('password')
        )

        return {'access_token': access_token}


app.add_url_rule('/', view_func=Users.as_view('user'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
