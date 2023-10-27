from django.db import models
from django.contrib.auth.models import User



class Posts(models.Model):
    object = None
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=255)

def __str__(self):
    return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    objects = None
    status = models.CharField(max_length=50, default='active')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)








