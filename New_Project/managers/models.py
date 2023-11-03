from django.db import models


class ModelSerializer(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=100)
    age = models.IntegerField()
