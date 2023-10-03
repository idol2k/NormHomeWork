from django.db import models

class Posts(models.Model):
    object = None
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=255)

def __str__(self):
    return self.title