import typing

import flask
import flask_apispec
import flask_jwt_extended
import flask_jwt_extended.exceptions
from flask_apispec import views

from backend import settings

from . import schema


app = flask.Blueprint('workspace', __name__)


@flask_apispec.use_kwargs(schema.AuthRequestSchema)
@flask_apispec.marshal_with(schema.AuthResponseSchema)
class OrthancAuth(views.MethodResource):
    def post(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        access_token = kwargs.pop('token_value')

        granted = True
        try:
            flask_jwt_extended.decode_token(access_token)
        except flask_jwt_extended.exceptions.JWTDecodeError:
            granted = False

        return {'granted': granted, 'validity': settings.ORTHANC_SESSION_VALIDITY}


app.add_url_rule('/orthanc_auth', view_func=OrthancAuth.as_view('orthanc_auth'))
