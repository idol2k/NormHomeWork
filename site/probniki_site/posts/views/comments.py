from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django import forms
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views import View

MAX_POSTS_PER_CATEGORY = {
    'категория1': 10,
    'категория2': 5,
    'категория3': 8,
}


class PostDetailView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Posts, id=post_id)
        return HttpResponse(f"Пост с id {post_id} существует")


class AddCommentView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Posts, pk=post_id)
        author = request.user
        content = request.POST.get('content')

        comment = Comment(post=post, author=author, content=content)
        comment.save()
        return redirect('post_detail', post_id=post_id)

class PostCommentsView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Posts, pk=post_id)
        comments = Comment.objects.filter(post=post)
        return render(request, 'post_comments.html', {'post': post, 'comments': comments})


class ChangeStatusView(View):
    def post(self, request, post_id, status):
        post = get_object_or_404(Posts, id=post_id)
        comments = Comment.objects.filter(post=post)
        for comment in comments:
            comment.status = status
            comment.save()
        return HttpResponse('Статус комментариев успешно изменен.')

class PostsForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)



