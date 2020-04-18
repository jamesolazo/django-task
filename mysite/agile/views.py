from .models import Values, Principles

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK


class ValuesListView(APIView):
    def get(self, request):
        values = list(Values.objects.values())
        for value in values:
            value['created_at'] = value['created_at'].strftime("%Y-%m-%d %H:%I:%S")
            value['updated_at'] = value['updated_at'].strftime("%Y-%m-%d %H:%I:%S")

        return JsonResponse({
            'data': values,
            'status': HTTP_200_OK
        })


class PrincipleListView(APIView):
    def get(self, request):
        principles = list(Principles.objects.values())
        for principle in principles:
            principle['created_at'] = principle['created_at'].strftime("%Y-%m-%d %H:%I:%S")
            principle['updated_at'] = principle['updated_at'].strftime("%Y-%m-%d %H:%I:%S")

        return JsonResponse({
            'data': principles,
            'status': HTTP_200_OK
        })