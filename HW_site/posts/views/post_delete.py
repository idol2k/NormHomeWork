from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from ..models import Posts

class DeletePost(View):
    def get(self, request, post_id):
        post = get_object_or_404(Posts, id=post_id)
        return render(request, 'delete_post.html', {'post': post})

    def post(self, request, post_id):
        post = get_object_or_404(Posts, id=post_id)
        post.delete()
        return redirect('all_posts')