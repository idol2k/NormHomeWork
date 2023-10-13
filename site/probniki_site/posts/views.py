from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Posts, Comment
from .forms import PostsForm
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver

MAX_POSTS_PER_CATEGORY = {
    'категория1': 10,
    'категория2': 5,
    'категория3': 8,
}

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


def add_comment(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    author = request.user
    content = request.POST.get('content')

    comment = Comment(post=post, author=author, content=content)
    comment.save()
    return redirect('post_detail', post_id=post_id)

def post_comments(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_comments.html', {'post': post, 'comments': comments})

def change_status(request, post_id, status):
    post = get_object_or_404(Posts, id=post_id)
    comments = Comment.objects.filter(post=post)
    for comment in comments:
        comment.status = status
        comment.save()
    return HttpResponse('Статус комментариев успешно изменен.')

def create_post(request, title, content, category):
    post = Posts(title=title, content=content, category=category, created_date=timezone.now())
    post.save()
    return HttpResponse('Пост успешно создан.')

@receiver(pre_save, sender=Posts)
def check_max_posts(sender, instance, **kwargs):
    if instance.category in MAX_POSTS_PER_CATEGORY:
        max_posts = MAX_POSTS_PER_CATEGORY[instance.category]
    else:
        max_posts = 0
    posts_count = Posts.objects.filter(category=instance.category).count()
    if posts_count >= max_posts:
        oldest_post = Posts.objects.filter(category=instance.category).order_by('created_date').first()
        oldest_post.delete()