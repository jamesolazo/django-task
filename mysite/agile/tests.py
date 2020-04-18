from .models import Values, Principles
from .serializer import ValuesSerializer, PrincipleSerializer

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class ValuesListViewTestCase(APITestCase):
    def test_values_list(self):
        url = reverse('values-list')
        response = self.client.get(url)
        values = Values.objects.all()
        serializer = ValuesSerializer(values, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class PrincipleListViewTestCase(APITestCase):
    def test_principle_list(self):
        url = reverse('principle-list')
        response = self.client.get(url)
        principles = Principles.objects.all()
        serializer = PrincipleSerializer(principles, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)