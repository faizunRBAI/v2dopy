import pytest


@pytest.mark.django_db
def test_home_page_renders(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!doctype html>' in response.content


@pytest.mark.django_db
def test_health_reports_ok(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'
