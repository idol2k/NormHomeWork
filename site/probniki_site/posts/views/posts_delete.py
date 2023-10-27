from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views import View
from django import forms



class PostDeleteView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Posts, id=post_id)
        return render(request, 'post_delete.html', {'post': post})

    def post(self, post_id):
        post = get_object_or_404(Posts, id=post_id)
        post.delete()
        return redirect('post_list')
class PostsForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)