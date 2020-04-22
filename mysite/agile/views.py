from .models import Values, Principles
from .serializer import ValuesSerializer, PrincipleSerializer

from rest_framework import generics


class ValuesList(generics.ListCreateAPIView):
    queryset = Values.objects.all()
    serializer_class = ValuesSerializer


class PrincipleList(generics.ListCreateAPIView):
    queryset = Principles.objects.all()
    serializer_class = PrincipleSerializer
