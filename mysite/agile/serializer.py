from .models import Values, Principles

from rest_framework import serializers


class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Values
        fields = ["id", "title", "description", "created_at"]


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principles
        fields = ["id", "description", "created_at"]
