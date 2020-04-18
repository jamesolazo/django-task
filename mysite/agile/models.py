from django.db import models


class Values(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Principles(models.Model):
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
