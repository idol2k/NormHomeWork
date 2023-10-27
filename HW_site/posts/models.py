from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Posts(models.Model):
    object = None
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=255)
    category = models.TextField(max_length=100)
    created_at = timezone.now()


def __str__(self):
    return self.title and self.category


class Comment(models.Model):

    objects = None
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()
    status = models.CharField(max_length=100, choices=False)

    def __str__(self):
        return self.text
