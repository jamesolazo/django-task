from .models import Values, Principles
from .serializer import ValuesSerializer, PrincipleSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView


class ValuesListView(APIView):
    def get(self, request):
        try:
            values = Values.objects.all()
            serializer = ValuesSerializer(values, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PrincipleListView(APIView):
    def get(self, request):
        try:
            principles = Principles.objects.all()
            serializer = PrincipleSerializer(principles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)