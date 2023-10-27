from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views import View
from django import forms


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


class PostsForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)