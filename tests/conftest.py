import pathlib
import sys
import time
import typing

import flask
import flask.testing
import flask_sqlalchemy
import psycopg2
import pytest
import sqlalchemy.exc


def pytest_configure() -> None:
    sys.path.insert(0, str(pathlib.Path(__file__).parents[1]))


@pytest.fixture
def test_app() -> typing.Generator[flask.Flask, None, None]:
    from backend.app import app

    app.testing = True
    with app.app_context():
        yield app


@pytest.fixture
def test_client(
    test_app: flask.Flask,
) -> typing.Generator[flask.testing.FlaskClient, None, None]:
    with test_app.test_client() as test_client:
        yield test_client


@pytest.fixture
def db(test_app: flask.Flask) -> flask_sqlalchemy.SQLAlchemy:
    from backend import db

    connected = False
    while not connected:
        try:
            db.drop_all()
            db.create_all()
        except (sqlalchemy.exc.OperationalError, psycopg2.OperationalError):
            time.sleep(1)
        else:
            connected = True
    yield db

    db.session.close()
