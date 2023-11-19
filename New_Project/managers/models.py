from django.db import models


class ModelSerializer(models.Model):
    DoesNotExist = None
    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    comment = models.TextField(max_length=200)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name_comment = models.CharField(max_length=50)
    text_comment = models.TextField(max_length=150)
    category = models.CharField()


