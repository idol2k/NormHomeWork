from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from ..models import Posts
from ..forms import PostsForm


class PostUpdate(View):
    def get(self, request, post_id):
        post = get_object_or_404(Posts, id=post_id)
        form = PostsForm(instance=post)
        return render(request, 'update_post.html', {'form': form})

    def post(self, request, post_id):
        post = get_object_or_404(Posts, id=post_id)
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('all_posts')
        return render(request, 'update_post.html', {'form': form})