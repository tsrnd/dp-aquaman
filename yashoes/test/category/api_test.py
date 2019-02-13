import pytest
from django.urls import reverse
from rest_framework import status

from yashoes.model.category import Category


@pytest.fixture
def init_category_test():
    Category.objects.create(id=1, name='Nike')


@pytest.mark.django_db(transaction=True)
def test_get_categories_success(client, init_category_test):
    url = reverse('categories-list')
    response = client.get(url)
    response_test = {'data': [
        {
            'id': 1,
            'name': 'Nike',
            'brand_id': None,
            'sub_categories': []
        }
    ]
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == response_test
