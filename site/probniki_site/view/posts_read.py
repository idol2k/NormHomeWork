from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Posts, Comment
from .forms import PostsForm
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views import View


class PostListView(View):
    def get(self, request):
        posts = Posts.objects.all()
        return render(request, 'posts/main.html', {'posts': posts})