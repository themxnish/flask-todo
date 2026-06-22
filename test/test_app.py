import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()

        yield client

        with app.app_context():
            db.session.remove()
            db.drop_all()


def test_home_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200


def test_add_todo(client):
    response = client.post(
        '/add',
        data={'title': 'Test task'},
        follow_redirects=True
    )

    assert response.status_code == 200


def test_update_todo(client):
    # Add a todo first
    client.post(
        '/add',
        data={'title': 'Update me'},
        follow_redirects=True
    )

    # Toggle completion
    response = client.get('/update/1', follow_redirects=True)

    assert response.status_code == 200


def test_delete_todo(client):
    # Add a todo first
    client.post(
        '/add',
        data={'title': 'Delete me'},
        follow_redirects=True
    )

    response = client.get('/delete/1', follow_redirects=True)

    assert response.status_code == 200
