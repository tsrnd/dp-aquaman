from yashoes.models import User
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
import pytest


@pytest.fixture
def init_test_user():
    User.objects.create_user(username='test', password='test', email='test@gmail.com', address='test',
                             phone_number=1234566789)


@pytest.mark.django_db(transaction=True)
def test_loginsuccess(client, init_test_user):
    url = reverse('auth-login')
    data = {
        'username': 'test',
        'password': 'test',
    }
    response = client.post(url, data)
    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("test_input,expected", [
    ({'username': 'test', 'password': 'test1'}, 400),
    ({'username': 'test1', 'password': 'test'}, 400),
    ({'username': 'test1', 'password': 'test1'}, 400),
])
def test_loginfail(test_input, expected, client, init_test_user):
    url = reverse('auth-login')
    data = test_input
    response = client.post(url, data)
    '''
    Test login fail with incorrect username or password
    '''
    assert response.status_code == expected
    data = response.json()
    assert data.get('non_field_errors')[0] == 'Unable to log in with provided credentials.'


@pytest.mark.django_db(transaction=True)
def test_register_success(client):
    url = reverse('auth-register')
    data = {
        'username': 'test',
        'password': 'test',
        'password_confirm': 'test',
        'email': 'test@testing.com'
    }
    response = client.post(url, data)
    assert response.status_code == 200

