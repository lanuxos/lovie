from lovie import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/test')
    assert response.data == b'Hello, Flask. <br>This is a message from __init__'
