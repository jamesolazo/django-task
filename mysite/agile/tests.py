import pytest

from django.urls import reverse

from rest_framework import status

from .models import Principles, Values
from .serializer import PrincipleSerializer, ValuesSerializer


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def principle_objects():
    return Principles.objects.all()


@pytest.fixture
def principle_serializer():
    return PrincipleSerializer


@pytest.fixture
def values_objects():
    return Values.objects.all()


@pytest.fixture
def values_serializer():
    return ValuesSerializer


@pytest.mark.django_db
def test_principle(api_client, principle_objects, principle_serializer):
    url = reverse("principle-list")
    response = api_client.get(url)
    serializer = principle_serializer(principle_objects, many=True)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data


@pytest.mark.django_db
def test_values(api_client, values_objects, values_serializer):
    url = reverse("values-list")
    response = api_client.get(url)
    serializer = values_serializer(values_objects, many=True)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data
