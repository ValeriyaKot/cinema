import pytest
import json
from rest_framework import status
from .conftest import DirectorFactory


@pytest.mark.django_db(transaction=True)
class TestDirector:
    url = '/directors/'

    def test_list(self, api_client):
        response = api_client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_create(self, api_client):
        director = DirectorFactory()
        director_data = {'first_name': director.first_name, 'last_name': director.last_name,
                         'country': director.country}
        response = api_client.post(self.url, data=director_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
