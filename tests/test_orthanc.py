import subprocess
import time

import flask.testing
import flask_sqlalchemy
import requests


def test_orthanc_basic_auth(
    test_client: flask.testing.FlaskClient, db: flask_sqlalchemy.SQLAlchemy
) -> None:
    # Wait for orthanc to become available
    time.sleep(5)
    orthanc_resp = requests.get('http://orthanc:8042')
    assert orthanc_resp.status_code == 403

    test_client.post('/user/', data={'email': 'test@test.com', 'password': '12345678'})
    r = test_client.post(
        '/user/login', data={'email': 'test@test.com', 'password': '12345678'}
    )
    access_token = r.get_json()['access_token']

    flask_process = subprocess.Popen(['poetry', 'run', './run.sh'])
    # Wait for the subprocess to initialize
    time.sleep(5)

    orthanc_resp = requests.get(
        'http://orthanc:8042', headers={'Authorization': access_token}
    )
    assert orthanc_resp.status_code == 200

    flask_process.kill()
