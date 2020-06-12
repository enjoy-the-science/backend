import flask
import flask_apispec
import flask_bcrypt
import flask_jwt_extended
import flask_migrate
import flask_sqlalchemy

from backend import settings


app = flask.Flask(__name__)
app.config.from_object(settings)

apispec = flask_apispec.FlaskApiSpec()
bcrypt = flask_bcrypt.Bcrypt()
jwt = flask_jwt_extended.JWTManager()
migrate = flask_migrate.Migrate()
db = flask_sqlalchemy.SQLAlchemy()


def create_app() -> flask.Flask:
    apispec.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    return app
