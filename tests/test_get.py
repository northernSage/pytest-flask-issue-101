from flask import url_for

def test_get_index(client):
    assert client.get(url_for('index')).status_code == 200