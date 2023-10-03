from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Posts
from .forms import PostsForm

def post_list(request):
    posts = Posts.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostsForm()
    return render(request, 'post_create.html', {'form': form})


def post_update(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if request.method == 'POST':
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostsForm(instance=post)
    return render(request, 'post_update.html', {'form': form, 'post': post})


def post_delete(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_delete.html', {'post': post})


def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return HttpResponse(f"Пост с id {post_id} существует")