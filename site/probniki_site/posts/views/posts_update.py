from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views import View
from django import forms



class PostUpdateView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Posts, id=post_id)
        form = PostsForm(instance=post)
        return render(request, 'post_update.html', {'form': form, 'post': post})

    def post(self, request, post_id):
        post = get_object_or_404(Posts, id=post_id)
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        return render(request, 'post_update.html', {'form': form, 'post': post})



class PostsForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)