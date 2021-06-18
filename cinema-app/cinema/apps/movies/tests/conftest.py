import factory
import pytest
from rest_framework.test import APIClient
# from apps.movies.models import Director


@pytest.fixture
def api_client():
    return APIClient()


class DirectorFactory(factory.django.DjangoModelFactory):

    # class Meta:
    #     model = Director

    id = 1
    first_name = 'Tom'
    last_name = 'West'
    country = 'USA'
