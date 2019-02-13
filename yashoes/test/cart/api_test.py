import pytest
from django.urls import reverse
from rest_framework import status

from yashoes.model.product import Product
from yashoes.model.variant import Variant
from yashoes.models import User


@pytest.fixture
def init_user_test():
    User.objects.create_user(username='test', password='test', email='test@gmail.com', address='test',
                             phone_number=1234566789)
    Product.objects.create(name="Adidas")
    Variant.objects.create(name="Black", product_id=1)


@pytest.mark.django_db(transaction=True)
def test_add_variant_to_cart_success(client, init_user_test):
    login_url = reverse('auth-login')
    data = {
        'username': 'test',
        'password': 'test',
    }
    login_response = client.post(login_url, data)
    access_token = login_response.json().get('token')
    url = reverse('user_variant')
    data = {
        'variant_id': 1,
        'quantity': 1
    }
    response = client.post(url, data, HTTP_AUTHORIZATION='Bearer {}'.format(access_token))
    assert response.status_code == status.HTTP_200_OK
