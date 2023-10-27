from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Posts, Comment
from .forms import PostsForm
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views import View


class PostCreateView(View):
    def get(self, request):
        form = PostsForm()
        return render(request, 'post_create.html', {'form': form})

    def post(self, request):
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        return render(request, 'post_create.html', {'form': form})