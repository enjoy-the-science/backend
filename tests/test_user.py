import flask.testing
import flask_jwt_extended
import flask_sqlalchemy

from backend import user


def test_user_registration(
    test_client: flask.testing.FlaskClient, db: flask_sqlalchemy.SQLAlchemy
) -> None:
    r = test_client.post(
        '/user/', data={'email': 'test@test.com', 'password': '12345678'}
    )
    assert r.status_code == 200

    json_data = r.get_json()
    new_user = user.User.get_user(json_data['id'])

    assert new_user.email == 'test@test.com'


def test_user_duplicate(
    test_client: flask.testing.FlaskClient, db: flask_sqlalchemy.SQLAlchemy
) -> None:
    r = test_client.post(
        '/user/', data={'email': 'test@test.com', 'password': '12345678'}
    )
    assert r.status_code == 200

    r = test_client.post(
        '/user/', data={'email': 'test@test.com', 'password': 'iamduplicate'}
    )
    assert r.status_code == 409


def test_user_login(
    test_client: flask.testing.FlaskClient, db: flask_sqlalchemy.SQLAlchemy
) -> None:
    r = test_client.post(
        '/user/', data={'email': 'test@test.com', 'password': '12345678'}
    )
    user_id = r.get_json()['id']

    r = test_client.post(
        '/user/login', data={'email': 'test@test.com', 'password': '12345678'}
    )

    access_token = r.get_json()['access_token']
    identity = flask_jwt_extended.decode_token(access_token)['identity']

    assert identity == user_id
